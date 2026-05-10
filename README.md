# principios-solid

Exemplos do curso **Princípios SOLID em Python**: Melhore seu código.

Estrutura: cada princípio tem um par de diretórios — `{letra}s/` (violação) e `{letra}o/` (correto) — para estudar lado a lado.

---

# S — Single Responsibility Principle (Princípio da Responsabilidade Única)

> Uma classe deve ter apenas um motivo para mudar.

**Benefícios:**
- Facilidade de manutenção e evolução do código
- Código mais limpo e claro
- Facilidade para desenvolvimento de testes
- Reduz acoplamentos

## `s/` — violação

| Arquivo | O que faz |
|---------|-----------|
| [`s/exemplo_sem_srp.py`](s/exemplo_sem_srp.py) | Classe `ListRepositories` que **faz requisição HTTP E gera relatório** — duas responsabilidades na mesma classe |
| [`s/main.py`](s/main.py) | Já separa em `GithubClient` + `RepoParser`, mas ainda usa parser que imprime em vez de retornar |

## `o/` — aplicado corretamente

| Arquivo | Responsabilidade |
|---------|-----------------|
| [`o/github/client.py`](o/github/client.py) | **Só** faz requisições HTTP à API do GitHub |
| [`o/parser.py`](o/parser.py) | **Só** converte JSON bruto em objetos `Repo` |
| [`o/models/repo.py`](o/models/repo.py) | **Só** modela os dados do repositório |
| [`o/repo/reports/html_generator.py`](o/repo/reports/html_generator.py) | **Só** gera relatório HTML |
| [`o/repo/reports/markdown_generator.py`](o/repo/reports/markdown_generator.py) | **Só** gera relatório Markdown |
| [`o/repo/reports_generator.py`](o/repo/reports_generator.py) | Orquestra a geração de relatórios sem conhecer detalhes |

---

# O — Open-Closed Principle (Princípio Aberto-Fechado)

> Objetos ou entidades devem estar abertos para extensão, mas fechados para modificação.

Quando novos comportamentos e recursos precisam ser adicionados no software, devemos **estender** e não **alterar** o código fonte original.

## `o/` demonstra OCP

Em [`o/repo/reports_generator.py`](o/repo/reports_generator.py):

```python
class ReportsGenerator:
    @classmethod
    def build(cls, generator, repos):
        return generator.build(repos)
```

Para adicionar um novo formato (ex: PDF), **não precisa modificar** `ReportsGenerator` — basta criar uma nova classe com método `build()` e passá-la como parâmetro. O código está **fechado para modificação, aberto para extensão**.

Geradores disponíveis:
- [`o/repo/reports/html_generator.py`](o/repo/reports/html_generator.py)
- [`o/repo/reports/markdown_generator.py`](o/repo/reports/markdown_generator.py)

---

# L — Liskov Substitution Principle (Princípio da Substituição de Liskov)

> Se S é um subtipo de T, então objetos de T podem ser substituídos por objetos de S sem alterar as propriedades do programa.

Em outras palavras: uma subclasse deve ser capaz de substituir sua superclasse sem quebrar o código cliente.

## `ls/` — violações

| Arquivo | Violação |
|---------|----------|
| [`ls/repo/reports/base_generator.py`](ls/repo/reports/base_generator.py) | Classe base `ReportGenerator.build` define retorno como `str` |
| [`ls/repo/reports/html_generator.py`](ls/repo/reports/html_generator.py) | **Retorna `list[]`** em vez de `str` — viola o contrato da base |
| [`ls/repo/reports/markdown_generator.py`](ls/repo/reports/markdown_generator.py) | Adiciona `build_with_header(repos, header)` com **parâmetro extra** — não substitui `build` corretamente |
| [`ls/main.py`](ls/main.py) | Demonstra as violações em execução |

```python
# ls/repo/reports/html_generator.py
class HTMLGenerator(ReportGenerator):
    @classmethod
    def build(cls, repos):
        if not repos:
            return []                          # ❌ list, não str
        items = "..."
        return [f"<p>{items}"]                  # ❌ list, não str
```

## `lo/` — aplicado corretamente

| Arquivo | Descrição |
|---------|-----------|
| [`lo/repo/reports/base_generator.py`](lo/repo/reports/base_generator.py) | ABC com `@abstractmethod` definindo o contrato: `build(repos) -> str` |
| [`lo/repo/reports/html_generator.py`](lo/repo/reports/html_generator.py) | Implementa `build` com mesma assinatura e tipo de retorno |
| [`lo/repo/reports/markdown_generator.py`](lo/repo/reports/markdown_generator.py) | Implementa `build` com mesma assinatura e tipo de retorno |
| [`lo/main.py`](lo/main.py) | Demonstra substituição perfeita entre os geradores |

```python
# lo/repo/reports/html_generator.py
class HTMLGenerator(ReportGenerator):
    @classmethod
    def build(cls, repos):       # ✅ mesma assinatura
        items = "..."
        return f"<p>{items}"      # ✅ mesmo tipo de retorno: str
```

---

# I — Interface Segregation Principle (Princípio da Segregação de Interface)

> Uma classe não deve ser forçada a implementar interfaces que não utiliza.

É melhor ter **várias interfaces pequenas e específicas** do que uma interface grande e genérica.

## `is/` — violações

| Arquivo | Violação |
|---------|----------|
| [`is/repo/reports/report_generator.py`](is/repo/reports/report_generator.py) | Interface **gorda** com `build_html`, `build_markdown` e `save_to_file` |
| [`is/repo/reports/html_generator.py`](is/repo/reports/html_generator.py) | Forçado a implementar `build_markdown` e `save_to_file` — lança `NotImplementedError` |
| [`is/repo/reports/markdown_generator.py`](is/repo/reports/markdown_generator.py) | Forçado a implementar `build_html` e `save_to_file` — lança `NotImplementedError` |
| [`is/main.py`](is/main.py) | Demonstra as violações |

```python
# is/repo/reports/report_generator.py — INTERFACE GORDA
class ReportGenerator:
    def build_html(self, repos): ...
    def build_markdown(self, repos): ...
    def save_to_file(self, content, path): ...

# is/repo/reports/html_generator.py — FORÇADO a implementar o que não usa
class HTMLGenerator(ReportGenerator):
    def build_html(self, repos): ...
    def build_markdown(self, repos):
        raise NotImplementedError("HTMLGenerator nao suporta markdown")  # 😞
    def save_to_file(self, content, path):
        raise NotImplementedError("HTMLGenerator nao salva em arquivo")  # 😞
```

## `io/` — aplicado corretamente

Interfaces segregadas em interfaces pequenas e específicas:

| Arquivo | Interface |
|---------|-----------|
| [`io/repo/reports/formatter.py`](io/repo/reports/formatter.py) | `Formatter` — só `format(repos)` |
| [`io/repo/reports/saver.py`](io/repo/reports/saver.py) | `Saver` — só `save(content, path)` |
| [`io/repo/reports/html_formatter.py`](io/repo/reports/html_formatter.py) | Implementa **só** `Formatter` |
| [`io/repo/reports/markdown_formatter.py`](io/repo/reports/markdown_formatter.py) | Implementa **só** `Formatter` |
| [`io/repo/reports/file_saver.py`](io/repo/reports/file_saver.py) | Implementa **só** `Saver` |
| [`io/main.py`](io/main.py) | Demonstra o uso limpo |

```python
# io/repo/reports/formatter.py — INTERFACE PEQUENA
class Formatter(ABC):
    @abstractmethod
    def format(self, repos): ...

# io/repo/reports/html_formatter.py — implementa SÓ o que precisa
class HTMLFormatter(Formatter):
    def format(self, repos): ...   # ✅ só isso!
```

---

# D — Dependency Inversion Principle (Princípio da Inversão de Dependência)

> Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
> Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.

## `ds/` — violações

| Arquivo | Violação |
|---------|----------|
| [`ds/repo/reports_generator.py`](ds/repo/reports_generator.py) | `ReportsGenerator` **instancia diretamente** `HTMLGenerator` e `MarkdownGenerator` no construtor |
| [`ds/main.py`](ds/main.py) | Código cliente acoplado — para adicionar novo formato, precisa modificar `ReportsGenerator` |

```python
# ds/repo/reports_generator.py — ALTO NÍVEL DEPENDE DE BAIXO NÍVEL
class ReportsGenerator:
    def __init__(self):
        self._html = HTMLGenerator()       # ❌ acoplamento direto
        self._markdown = MarkdownGenerator() # ❌ acoplamento direto
```

## `do/` — aplicado corretamente

| Arquivo | Descrição |
|---------|-----------|
| [`do/repo/reports/report_generator.py`](do/repo/reports/report_generator.py) | Abstração `ReportGenerator` (ABC) |
| [`do/repo/reports/html_generator.py`](do/repo/reports/html_generator.py) | Implementa a abstração |
| [`do/repo/reports/markdown_generator.py`](do/repo/reports/markdown_generator.py) | Implementa a abstração |
| [`do/repo/reports_generator.py`](do/repo/reports_generator.py) | Depende da abstração, dependências injetadas |
| [`do/main.py`](do/main.py) | Injeção de dependência no ponto de entrada |

```python
# do/repo/reports_generator.py — DEPENDE DE ABSTRAÇÃO
class ReportsGenerator:
    def __init__(self, generators: Sequence[ReportGenerator]):  # ✅ injeção
        self._generators = generators

    def build_all(self, repos):
        return [g.build(repos) for g in self._generators]

# do/main.py — quem cria, injeta
generator = ReportsGenerator([HTMLGenerator(), MarkdownGenerator()])
# Quer adicionar PDF? Basta criar PDFGenerator(ReportGenerator) e passar na lista
```

---

## Como estudar

```bash
# Entre no diretório do princípio que quer estudar
cd principios-solid/ls    # ou lo, is, io, ds, do, s, o

# Cada diretório é auto-contido — rode o main
python main.py
```

Compare o par `{letra}s/` vs `{letra}o/` para ver a diferença entre a violação e a aplicação correta de cada princípio.

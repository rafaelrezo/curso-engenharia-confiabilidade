# Curso Engenharia de Confiabilidade

Repositório MkDocs com conceitos centrais e resumo capítulo a capítulo do
livro **Engenharia de Confiabilidade do Google**.

Site público: <https://rafaelrezo.github.io/curso-engenharia-confiabilidade/>

## Rodando localmente

```bash
make install
make run
```

Depois acesse `http://127.0.0.1:8001`.

Para usar outra porta:

```bash
make run PORT=8000
```

## Gerando o site estático

```bash
make build
```

## Validando em modo estrito

```bash
make strict
```

## Validando o conteúdo editorial

```bash
make check-content
```

## Regenerando a documentação

```bash
make generate
```

## Limpando artefatos

```bash
make clean
make clean-venv
```

## Organização

- `docs/conceitos-centrais.md`: mapa de referência dos conceitos de SRE.
- `docs/capitulos/`: resumos dos 25 capítulos consolidados.
- `docs/fonte-e-escopo.md`: fonte usada e limites do material.

## Referências

- Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard, eds. **Engenharia de Confiabilidade do Google**. Novatec, 2016.
- Google. **Site Reliability Engineering: How Google Runs Production Systems**. <https://sre.google/sre-book/>.

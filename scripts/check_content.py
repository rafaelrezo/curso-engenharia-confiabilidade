from pathlib import Path


REQUIRED_CHAPTER_SECTIONS = [
    "## Objetivos de aprendizagem",
    "## Síntese",
    "## Conceitos essenciais",
    "## Aplicação prática",
    "## Perguntas para revisão",
    "## Exercícios",
    "## Referências",
]

FORBIDDEN_STUDENT_PHRASES = [
    "No contexto de",
    "este conceito deve ser tratado",
    "este conceito sustenta a ideia central",
    "termo de vocabulário",
    "**O que é:**",
    "**Por que importa:**",
    "**Como aplicar:**",
    "**Armadilha comum:**",
    "Lesson Learned",
    "Explaining Like You're 15",
    "## Modelo mental",
    "## Cenário realista",
    "## Visão sistêmica",
    "## Mapa visual de estudo",
    "## Explicando como se você tivesse 15 anos",
    "## Como isso evoluiu depois de 2016",
    "Este capítulo mostra",
    "Nesta seção",
    "A segunda metade da introdução",
    "a segunda metade da introdução",
    "na seção anterior",
    "na próxima seção",
    "como vimos acima",
    "como veremos abaixo",
    "A Parte II",
    "A Parte III",
    "A Parte IV",
    "O valor do capítulo",
    "A prática do capítulo",
    "do capítulo",
    "O capítulo argumenta",
    "O capítulo define",
    "O capítulo apresenta",
    "O capítulo mostra",
    "O capítulo trata",
    "O capítulo discute",
    "O capítulo defende",
    "O capítulo descreve",
    "O capítulo aborda",
    "O capítulo explica",
    "O capítulo examina",
    "O capítulo compara",
]


def main() -> None:
    failures: list[str] = []
    chapter_paths = sorted(Path("docs/capitulos").glob("capitulo-*.md"))

    if len(chapter_paths) != 25:
        failures.append(f"Expected 25 chapter files, found {len(chapter_paths)}.")

    for path in chapter_paths:
        text = path.read_text(encoding="utf-8")
        missing = [section for section in REQUIRED_CHAPTER_SECTIONS if section not in text]
        if missing:
            failures.append(f"{path}: missing {', '.join(missing)}")
        forbidden = [phrase for phrase in FORBIDDEN_STUDENT_PHRASES if phrase in text]
        if forbidden:
            failures.append(f"{path}: forbidden mechanical wording {', '.join(forbidden)}")

    for path in sorted(Path("docs").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "## Referências" not in text:
            failures.append(f"{path}: missing ## Referências")

    if failures:
        print("STATUS = REWORK REQUIRED")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("STATUS = COMPLETE")
    print("A estrutura mínima dos capítulos está presente sem seções mecânicas obrigatórias.")


if __name__ == "__main__":
    main()

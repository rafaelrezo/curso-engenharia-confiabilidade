# Capítulo 24 - Lições aprendidas com outros mercados

## Objetivos de aprendizagem

- Explicar o problema de confiabilidade tratado pelo tema.
- Reconhecer onde o tema aparece em um serviço real.
- Aplicar o conceito em uma decisão operacional ou de engenharia.

## Síntese

SRE com mercados que lidam com risco, segurança e operação crítica. A confiabilidade em software pode aprender com checklists, cultura de reporte, investigação sem culpa, treinamento, redundância e padrões. A diferença é que software muda muito rápido, portanto precisa adaptar essas práticas a ciclos curtos e sistemas distribuídos.

Em uma frase: **Setores como saúde, aviação e energia mostram práticas de segurança que inspiram confiabilidade em software.**

## Por que isso importa

**aprendizado intersetorial** importa porque sistemas de produção são mantidos por pessoas, rotinas, decisões e relações entre equipes. Sem gestão explícita, mesmo boas práticas técnicas se degradam em filas de suporte, interrupções constantes e responsabilidades ambíguas.

## Conceitos essenciais

### **aprendizado intersetorial**

**aprendizado intersetorial**: É adaptar práticas de setores de alto risco para software, como checklists, treinamento, investigação sem culpa e reporte de quase-incidentes.

Uma forma simples de aplicar isso é: Comparar um processo interno com práticas de setores regulados.

### **segurança operacional**

**segurança operacional**: É a condição para responder incidentes sem medo de punição por decisões razoáveis. Sem isso, pessoas escondem falhas e atrasam aprendizado.

No dia a dia, isso aparece quando a equipe precisa introduzir checklist em uma operação crítica.

### **checklists**

**checklists**: É uma memória operacional externa. Ajuda a evitar esquecimentos em lançamentos, incidentes e mudanças repetidas.

Esse conceito fica concreto quando a equipe consegue incentivar reporte de quase-incidentes.

### **cultura de reporte**

**cultura de reporte**: É o ambiente em que pessoas relatam falhas, riscos e quase-incidentes sem medo de punição por decisões razoáveis. Sem reporte, a organização perde sinais precoces.

Uma forma simples de aplicar isso é: Comparar um processo interno com práticas de setores regulados.

### **adaptação a software**

**adaptação a software**: É ajustar práticas de segurança operacional ao ritmo de sistemas digitais, que mudam rápido, têm dependências distribuídas e permitem automação em escala.

No dia a dia, isso aparece quando a equipe precisa introduzir checklist em uma operação crítica.


## Aplicação prática

Para evitar burocracia, escolha um serviço concreto e execute uma ação pequena:

- Comparar um processo interno com práticas de setores regulados.
- Introduzir checklist em uma operação crítica.
- Incentivar reporte de quase-incidentes.

Depois da ação, procure uma evidência simples de melhoria: menos alertas
irrelevantes, recuperação mais rápida, dependência mais clara, deploy menos
arriscado, métrica mais confiável ou decisão mais fácil de explicar.

## Diagrama de apoio

```mermaid
flowchart LR
    Tema["Lições aprendidas com outros mercados"] --> C1["aprendizado intersetorial"]
    C1 --> C2["segurança operacional"]
    C2 --> C3["checklists"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

## Erros comuns

- Tratar o problema como falta de processo quando a causa é ambiguidade de responsabilidade.
- Criar reuniões, checklists ou treinamentos sem dono e sem revisão.
- Separar gestão de SRE da realidade técnica dos serviços em produção.

## Perguntas para revisão

1. Qual risco operacional **aprendizado intersetorial** ajuda a reduzir?
2. Que evidência mostraria que a prática foi aplicada com sucesso?
3. Como esse conceito mudaria uma decisão de release, plantão, arquitetura ou priorização?

## Exercícios

### Compreensão

Explique a ideia central em até cinco linhas, usando um serviço real como exemplo.

### Aplicação

Escolha um serviço real e execute uma das ações práticas.

### Análise

Liste duas formas de aplicar esse conceito de maneira superficial e explique o
risco de cada uma.

## Relação com práticas atuais

Gestão moderna de SRE aparece em onboarding estruturado, catálogos de serviço, revisões de prontidão, scorecards de confiabilidade, políticas de plantão e mecanismos de colaboração entre produto, plataforma e operação.

## Recursos complementares

- **Livro oficial online do Google SRE:** <https://sre.google/sre-book/>
- **The Site Reliability Workbook:** <https://sre.google/workbook/>
- **Google SRE Book - Lessons Learned from Other Industries:** <https://sre.google/sre-book/lessons-learned/>
- **Google SRE Resources:** <https://sre.google/resources/>

## Fechamento

Guarde a ideia principal: **Setores como saúde, aviação e energia mostram práticas de segurança que inspiram confiabilidade em software.**

Próximo: [Capítulo 25 - Conclusão](capitulo-25.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- **Google SRE Book - Lessons Learned from Other Industries:** <https://sre.google/sre-book/lessons-learned/>
- **Google Cloud Well-Architected Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

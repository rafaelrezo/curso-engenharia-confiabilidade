# Capítulo 22 - Comunicação e colaboração em SRE

## Objetivos de aprendizagem

- Identificar como **reunioes de produção** aparece em produção.
- Aplicar o procedimento do tema em uma jornada, mudança, incidente ou dependência real.
- Produzir um artefato prático: métrica, política, checklist, runbook ou plano de melhoria.

## Síntese

Reunioes de produção, composicao de equipes e técnicas de colaboração. Como SRE fica entre produto, infraestrutura e operação, precisa criar foruns, agendas, documentos e relacoes que mantenham todos alinhados. Comunicação eficaz reduz ambiguidades e permite decisões técnicas mais rápidas.

Em uma frase: **SRE depende de comunicação estruturada entre equipes com objetivos, incentivos e contextos diferentes.**

## Por que isso importa

**reunioes de produção** importa porque sistemas de produção são mantidos por pessoas, rotinas, decisões e relações entre equipes. Sem gestão explícita, mesmo boas práticas técnicas se degradam em filas de suporte, interrupções constantes e responsabilidades ambíguas.

## Conceitos essenciais

### **reunioes de produção**

**reunioes de produção**: São pontos de sincronização para decisões e riscos operacionais. Reuniões boas têm pauta, decisões registradas e próximos passos claros.

Uma forma simples de aplicar isso é: Definir pauta fixa para reuniao de produção.

### **colaboração entre equipes**

**colaboração entre equipes**: É alinhar times com responsabilidades diferentes. Em SRE, colaboração boa transforma conflito entre velocidade e estabilidade em decisão explícita.

No dia a dia, isso aparece quando a equipe precisa registrar decisões e pendencias operacionais.

### **agenda operacional**

**agenda operacional**: É o contrato da reunião. Uma agenda clara evita discussões abertas demais e mantém foco em produção, risco e decisão.

Esse conceito fica concreto quando a equipe consegue criar canal claro para negociacao de SLO e prioridades.

### **composicao de equipe**

**composicao de equipe**: É uma prática que transforma uma preocupação operacional em decisão concreta. Ela aparece quando a equipe precisa escolher entre aceitar risco, automatizar, simplificar, melhorar observabilidade, mudar o processo de release ou corrigir a causa raiz de um problema recorrente.

Uma forma simples de aplicar isso é: Definir pauta fixa para reuniao de produção.

### **alinhamento**

**alinhamento**: É uma prática que transforma uma preocupação operacional em decisão concreta. Ela aparece quando a equipe precisa escolher entre aceitar risco, automatizar, simplificar, melhorar observabilidade, mudar o processo de release ou corrigir a causa raiz de um problema recorrente.

No dia a dia, isso aparece quando a equipe precisa registrar decisões e pendencias operacionais.


## Aplicação prática

Escolha um serviço concreto e transforme o tema em uma ação verificável:

- Definir pauta fixa para reuniao de produção.
- Registrar decisões e pendencias operacionais.
- Criar canal claro para negociacao de SLO e prioridades.

Depois da ação, registre a evidência de melhoria: menos alertas irrelevantes,
recuperação mais rápida, dependência mais clara, deploy menos arriscado, métrica
mais confiável ou decisão mais fácil de explicar.

## Aprofundamento prático

Comunicação operacional precisa de fóruns previsíveis. Reunião de produção não deve ser uma conversa genérica; deve revisar risco, mudanças recentes, SLOs, incidentes, capacidade, dependências e ações pendentes.

Procedimento recomendado:

1. Mantenha pauta fixa e curta.
2. Traga dados: SLO, error budget, incidentes, top alertas e mudanças relevantes.
3. Registre decisões, donos e prazos.
4. Separe discussão técnica profunda para follow-up.
5. Revise pendências antigas e remova o que perdeu sentido.

Modelo de pauta:

```markdown
# Reunião de produção
SLOs em risco:
Mudanças relevantes:
Incidentes e quase-incidentes:
Top fontes de toil:
Dependências críticas:
Decisões tomadas:
Ações com dono e prazo:
```

A técnica é transformar conversa em memória operacional. Decisão que fica apenas no chat desaparece; decisão registrada pode ser cobrada, revisada e aprendida.

## Tradução para ferramentas modernas

**Ferramentas típicas:** ADRs, RFCs, reuniões de produção, service review docs, Slack/Teams, Google Docs, Confluence, Linear/Jira e dashboards compartilhados.

**Exemplo avançado:** implemente reunião de produção com pauta fixa: SLOs em risco, mudanças, incidentes, toil, dependências, decisões e ações com dono.

**Cuidado de projeto:** comunicação sem registro não escala. Decisão operacional precisa virar memória consultável.

## Exemplos e ferramentas do livro

O estudo de caso **Viceroy** aparece no livro para discutir colaboração em
SRE. A lição é que confiabilidade depende de relações de trabalho,
comunicação estruturada, decisões registradas e entendimento compartilhado
entre equipes.

No curso, conecte esse exemplo a reuniões de produção, documentos de decisão,
revisão de SLO, acompanhamento de ações e fóruns de alinhamento entre
produto, desenvolvimento, plataforma e SRE.

## Diagrama de apoio

```mermaid
flowchart LR
    Tema["Comunicação e colaboração em SRE"] --> C1["reunioes de produção"]
    C1 --> C2["colaboração entre equipes"]
    C2 --> C3["agenda operacional"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

## Erros comuns

- Tratar o problema como falta de processo quando a causa é ambiguidade de responsabilidade.
- Criar reuniões, checklists ou treinamentos sem dono e sem revisão.
- Separar gestão de SRE da realidade técnica dos serviços em produção.

## Perguntas para revisão

1. Qual risco operacional **reunioes de produção** ajuda a reduzir?
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
- **Google SRE Book - Communication and Collaboration in SRE:** <https://sre.google/sre-book/communication-and-collaboration/>
- **Google SRE Resources:** <https://sre.google/resources/>

## Fechamento

Guarde a ideia principal: **SRE depende de comunicação estruturada entre equipes com objetivos, incentivos e contextos diferentes.**

Próximo: [Capítulo 23 - O modelo de engajamento da SRE em evolução](capitulo-23.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- **Google SRE Book - Communication and Collaboration in SRE:** <https://sre.google/sre-book/communication-and-collaboration/>
- **Google Cloud Well-Architected Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

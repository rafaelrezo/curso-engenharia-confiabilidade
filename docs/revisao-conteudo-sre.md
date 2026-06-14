# Revisão de conteúdo SRE

Este documento consolida uma revisão editorial, técnica e pedagógica do curso
para orientar um plano de melhoria. O foco é formar profissionais em SRE de
forma prática, rápida e direta, considerando público leigo, mas sem reduzir a
profundidade técnica necessária para atuação profissional.

## Escopo da revisão

A análise cobriu:

- `docs/capitulos/capitulo-01.md` a `docs/capitulos/capitulo-25.md`;
- `docs/trilha-aprendizado.md`;
- `docs/conceitos-centrais.md`;
- `agents.md`, usado como referência interna de critérios editoriais e skills de autoria;
- referências atuais de SRE, cloud native, observabilidade, platform engineering,
  supply chain security, DORA e FinOps.

Um subagente revisor foi evocado para fazer uma leitura independente dos 25
capítulos. A síntese abaixo combina essa revisão com inspeção local do conteúdo
e checagem de fontes atuais.

## Skills evocados

Foram usados os skills internos definidos no próprio `agents.md`:

| Skill | Uso na revisão |
| --- | --- |
| S01 - Knowledge Extraction | Verificar se cada capítulo extrai conceito, problema, solução e impacto. |
| S02 - First Principles Thinking | Avaliar se o estudante entende por que a prática existe. |
| S07 - Practical Engineering | Checar se o capítulo gera ação prática e artefato profissional. |
| S09 - Industry Mapping | Verificar tradução para ferramentas e práticas atuais. |
| S10 - DevOps Mapping | Conectar SRE a DevOps, plataforma, cloud, segurança e CI/CD. |
| S12 - Bloom Taxonomy | Avaliar progressão de exercícios além de compreensão básica. |
| S13 - Visual Learning | Revisar qualidade de diagramas, tabelas e checklists. |
| S14 - Cognitive Load Reduction | Verificar clareza para público leigo. |
| S15 - Modern SRE Evolution | Medir atualidade em relação a práticas SRE em 2026. |

Também foi usado o skill local `find-skills` para buscar skill externo de SRE.
Foi encontrado `alexander-danilenko/ai-skills@sre-engineer`, mas ele não está
instalado. A revisão prosseguiu com os critérios locais do repositório.

## Diagnóstico executivo

O curso tem uma base conceitual boa e cobre bem o SRE Book clássico. Os
capítulos 01 a 07, 13, 14 e 16 são os mais maduros: explicam decisões
operacionais concretas, trazem exemplos e já conectam o livro a ferramentas
atuais.

A principal lacuna não é ausência de conteúdo, mas falta de prática acumulativa.
O curso precisa deixar de ser uma sequência de leituras e virar uma trilha de
produção de artefatos: mapa de serviço, SLO, alerta, dashboard, runbook,
pipeline, canário, teste de falha, postmortem, plano de restauração e roadmap.

Há capítulos com texto genérico ou reaproveitado, principalmente nos capítulos
08, 10, 11, 12, 15, 17 e 19 a 25. Isso reduz a sensação de formação
profissional. Também há problemas objetivos de revisão em capítulos
organizacionais, como termos sem acentuação (`reunioes`, `composicao`,
`priorizacao`) e definições pouco específicas.

## Lacunas transversais

### 1. Falta uma prática acumulativa única

O projeto final existe em `trilha-aprendizado.md`, mas os capítulos ainda não
constroem esse projeto de forma incremental. A melhoria mais importante é criar
um serviço didático único, por exemplo:

```text
checkout-api + banco + fila + worker + dashboard + pipeline
```

Cada capítulo deve adicionar um artefato profissional a esse mesmo serviço.
Isso reduz carga cognitiva, acelera a formação e cria portfólio verificável.

### 2. Exercícios são bons, mas pouco verificáveis

Todos os capítulos têm exercícios de compreensão, aplicação e análise. Falta
subir para avaliação e criação em capítulos-chave. Também faltam rubricas:
o que torna um SLO bom, um runbook aceitável, um postmortem completo ou um
plano de rollback pronto para produção.

### 3. Atualidade está presente, mas precisa ficar mais explícita

O curso já menciona OpenTelemetry, Kubernetes, GitOps, platform engineering,
SBOM, SLSA, feature flags, service mesh e DORA. Ainda assim, alguns temas de
2026 precisam aparecer com mais peso:

- OpenTelemetry como padrão consolidado de observabilidade, não só ferramenta;
- Kubernetes como plataforma comum para workloads modernos e de IA;
- reliability engineering para workloads de IA e LLMs;
- platform engineering com métricas de adoção, sucesso de tarefa e satisfação;
- supply chain security como parte da confiabilidade de release;
- custo de observabilidade, capacidade e FinOps como decisões de confiabilidade;
- governança de feature flags, flags antigas e kill switches;
- segurança operacional e resposta a incidentes integrada.

### 4. Diagramas precisam ensinar mais

Há bons diagramas nos capítulos iniciais, mas vários capítulos finais usam
fluxos genéricos. Substituir por diagramas operacionais reais: fluxo de
incidente, árvore de hipóteses, pipeline de release, arquitetura de failover,
matriz RACI, funil de triagem e processo de postmortem.

### 5. Linguagem precisa de revisão editorial nos capítulos finais

Capítulos 21 e 22 têm termos sem acento e definições genéricas. Isso é alta
prioridade editorial, mesmo quando a prioridade técnica do capítulo é média,
porque o público leigo precisa confiar no texto.

## Prioridades por capítulo

### Parte I - Fundamentos e princípios

| Capítulo | Diagnóstico | Prioridade | Melhorias necessárias | Artefato recomendado |
| --- | --- | --- | --- | --- |
| 01 - Introdução à SRE e produção | Sólido, abrangente e adequado para iniciantes. | Baixa | Incluir visão de carreira SRE em 2026 e explicar como o curso vira portfólio prático. | Mapa operacional de serviço com dependências, SLI inicial, modos de falha e dono. |
| 02 - Risco, SLO e error budget | Forte na conexão entre risco, SLO e decisão. | Baixa | Acrescentar cálculo guiado de burn rate multi-janela e exemplo OpenSLO/Sloth. | Especificação SLO em YAML com política de release e alerta de burn rate. |
| 03 - Toil | Bom, prático e bem contextualizado. | Baixa | Reforçar métricas de toil, ownership e risco de self-service sem suporte. | Auditoria de toil com ranking por custo mensal e ação proposta. |
| 04 - Monitoração distribuída | Atual e bem conectado a SLO, OpenTelemetry e Prometheus. | Média | Incluir cardinalidade, custo de observabilidade, exemplars e logs estruturados. | API instrumentada com OpenTelemetry, dashboard RED/USE e alerta por SLO. |
| 05 - Automação e release | Um dos melhores capítulos. | Baixa | Atualizar SLSA para v1.2, incluir provenance e attestation como confiabilidade de entrega. | Pipeline com artefato imutável, SBOM, assinatura, canário e rollback. |
| 06 - Simplicidade | Forte na diferença entre complexidade essencial e acidental. | Baixa | Adicionar métricas de remoção segura e governança de feature flags. | Inventário de flags, endpoints e dependências com plano de remoção reversível. |

### Parte II - Práticas

| Capítulo | Diagnóstico | Prioridade | Melhorias necessárias | Artefato recomendado |
| --- | --- | --- | --- | --- |
| 07 - Alertas e plantão | Claro e útil. | Média | Incluir métricas de saúde do plantão, handoff, escalonamento e limite de carga. | Revisão dos 10 alertas mais ruidosos com decisão página, ticket, dashboard ou remover. |
| 08 - Troubleshooting | Tema crítico, mas raso em método. | Alta | Detalhar árvore de hipóteses, linha do tempo, preservação de evidências e mudança segura. | Simulação com traces, logs, deploys e relatório de hipóteses testadas. |
| 09 - Incidentes e aprendizado | Boa base de coordenação e postmortem. | Média | Incluir taxonomia SEV, comunicação externa, status page, action items e acompanhamento. | Simulado SEV1 com comandante, documento vivo, atualização pública e postmortem. |
| 10 - Interrupções de serviço | Útil, mas genérico. | Alta | Aprofundar MTTA, MTTR, detecção pelo usuário, near misses, reincidência e tendências. | Catálogo mensal de incidentes com classificação, gráficos e backlog de confiabilidade. |
| 11 - Testes de confiabilidade | Tema bom, prática insuficiente. | Alta | Separar carga, resiliência, contrato, rollback, DR, chaos, sintéticos e produção. | Plano de chaos experiment com hipótese, escopo, abort criteria e métrica de sucesso. |
| 12 - Engenharia de software em SRE | Correto, mas estreito demais. | Alta | Tratar ferramenta SRE como produto interno com usuários, backlog, SLO, suporte e adoção. | PRD enxuto de ferramenta SRE com métrica de adoção, riscos e custo de manutenção. |
| 13 - Distribuição de carga | Bom e concreto. | Média | Incluir Gateway API/service mesh com cautela e revisar exemplos de configuração. | Desenho de failover regional com health checks por sintoma e capacidade de destino. |
| 14 - Sobrecarga e cascata | Forte em retries, limites e degradação. | Média | Incluir circuit breakers, bulkheads, load shedding e teste de retry storm. | Teste de carga comparando retries sem jitter e com jitter. |
| 15 - Consenso distribuído | Conceitualmente correto, mas superficial para atuação profissional. | Alta | Incluir Raft, etcd/Kubernetes control plane, quorum loss, leases, fencing tokens e trade-offs CAP. | Simulação de quorum/partição e runbook de perda de líder. |
| 16 - Agendamento e pipelines | Forte e aplicável. | Média | Adicionar backpressure, DLQ, reconciliação, mito do exactly-once e qualidade de dados. | Pipeline com estado, idempotência, reprocessamento e métrica de frescor/completude. |
| 17 - Integridade de dados | Bom núcleo, mas genérico nos blocos finais. | Alta | Aprofundar RPO/RTO, PITR, backups imutáveis, ransomware, corrupção silenciosa e validação pós-restore. | Game day de restauração com snapshot, checksum, RTO/RPO real e relatório de lacunas. |
| 18 - Lançamentos confiáveis | Bom tema, mas exercícios ainda genéricos. | Média | Transformar em PRR completo com SLOs de lançamento, risco, capacidade, rollback e limpeza de flags. | Checklist PRR e plano de canário com critérios de promoção e rollback. |

### Parte III - Gerenciamento

| Capítulo | Diagnóstico | Prioridade | Melhorias necessárias | Artefato recomendado |
| --- | --- | --- | --- | --- |
| 19 - Onboarding SRE | Útil, mas precisa de matriz real de competência. | Média | Detalhar trilha por nível, prontidão para plantão, shadowing e autonomia. | Matriz 30/60/90 com evidências, avaliação prática e checklist de shadowing. |
| 20 - Lidando com interrupções | Relevante, mas precisa focar melhor fatores humanos. | Alta | Separar interrupção cognitiva de interrupção de serviço; incluir WIP, canais e triagem. | Política de interrupções com canais, SLA interno, fila de triagem e métrica semanal. |
| 21 - Recuperação de sobrecarga operacional | Tem bom plano de 30 dias, mas definições são reaproveitadas. | Média | Separar sobrecarga de sistema e de equipe; incluir diagnóstico quantitativo e acordo com gestão. | Rescue plan de 30 dias com top alertas, top tickets, incidentes, toil e quick wins. |
| 22 - Comunicação e colaboração | Útil, mas exige revisão forte de linguagem. | Média | Corrigir acentuação; adicionar RFC/ADR, stakeholder map, comunicação assíncrona e conflito SLO vs prazo. | Pauta de reunião de produção e ADR de decisão operacional. |
| 23 - Modelo de engajamento SRE | Boa base, mas precisa distinguir modelos. | Média | Incluir SRE embedded, consultivo, platform, enabling, critérios de entrada/saída e limites de suporte. | Contrato de engajamento com RACI, SLOs, ownership, toil budget e revisão trimestral. |
| 24 - Lições de outros mercados | Bom gancho, superficial. | Média | Incluir Safety-II, near misses, premortem, cultura justa e adaptação ao ritmo de software. | Relatório de quase-incidente e checklist de failover inspirado em setores críticos. |
| 25 - Conclusão | Funcional, mas pouco forte para fechamento profissional. | Média | Sintetizar competências, propor capstone obrigatório e rubrica de maturidade SRE. | Capstone com SLO, dashboard, alerta, runbook, incidente simulado, postmortem e roadmap. |

## Melhorias de alta prioridade

1. Reescrever os capítulos 08, 10, 11, 12, 15, 17 e 20 para aumentar método,
   prática e profundidade.
2. Revisar linguagem e acentuação dos capítulos 21 e 22.
3. Criar um serviço didático incremental usado do início ao fim.
4. Criar labs executáveis e rubricas de avaliação.
5. Atualizar a camada 2026: OpenTelemetry graduado, SLSA v1.2, DORA 2025,
   Kubernetes para workloads modernos/IA, platform engineering mensurável e FinOps.

## Plano de melhoria sugerido

### Onda 1 - Correção editorial e confiança

Objetivo: remover ruído que prejudica credibilidade.

- Corrigir acentuação e termos sem revisão nos capítulos 21 e 22.
- Remover frases genéricas reaproveitadas.
- Revisar todos os diagramas que apenas repetem a estrutura do capítulo.
- Padronizar termos: SRE, SLI, SLO, SLA, error budget, toil, runbook,
  postmortem, rollback, rollout, canário, plantão e observabilidade.

Saída esperada: curso sem falhas editoriais visíveis e com linguagem mais
natural.

### Onda 2 - Trilha prática acumulativa

Objetivo: transformar leitura em formação profissional.

- Criar o serviço didático `checkout-api`.
- Definir artefato incremental por capítulo.
- Adicionar datasets ou cenários simulados: logs, métricas, traces, incidentes,
  deploys e tickets.
- Fazer o projeto final usar artefatos produzidos nos capítulos.

Saída esperada: estudante termina o curso com um dossiê SRE completo.

### Onda 3 - Profundidade técnica dos capítulos críticos

Objetivo: corrigir capítulos que hoje não bastam para prática profissional.

- Capítulo 08: troubleshooting com hipótese, evidência, linha do tempo e
  preservação de estado.
- Capítulo 10: analytics de incidentes, near misses, MTTA, MTTR e tendências.
- Capítulo 11: taxonomia de testes de confiabilidade e chaos engineering com
  abort criteria.
- Capítulo 12: engenharia de produto interno para ferramentas SRE.
- Capítulo 15: Raft, etcd, quorum loss, leases e fencing tokens.
- Capítulo 17: RPO/RTO, PITR, restore testado, corrupção silenciosa e backups
  imutáveis.
- Capítulo 20: interrupções humanas, triagem, WIP e canais de suporte.

Saída esperada: capítulos deixam de ser resumo e passam a ensinar execução.

### Onda 4 - Atualização 2026

Objetivo: alinhar o curso ao trabalho real de SRE em ambientes atuais.

- Tratar OpenTelemetry como padrão de instrumentação e telemetria.
- Inserir confiabilidade de workloads de IA: inferência, dependência de modelo,
  latência, custo, quotas, fallback e degradação.
- Atualizar release engineering com SLSA v1.2, provenance, attestation e
  verificação de artefato.
- Conectar platform engineering a métricas de adoção e experiência do
  desenvolvedor.
- Incluir FinOps como restrição operacional de capacidade, observabilidade e
  workloads de IA.

Saída esperada: o curso fica atual para SRE em 2026 sem virar catálogo de
ferramentas.

## Rubrica mínima por capítulo

Cada capítulo revisado deve responder:

- O estudante sabe explicar o problema em linguagem simples?
- O estudante sabe decidir quando aplicar a prática?
- Há pelo menos um exemplo concreto?
- Há pelo menos um erro comum que evita prática ruim?
- Há um artefato produzido ou melhorado?
- Há critério de qualidade para avaliar o artefato?
- A modernização é específica do tema, não uma lista solta de ferramentas?
- O capítulo ajuda o projeto final?

## Referências atuais para atualização

- Google SRE. **Site Reliability Engineering Book**: <https://sre.google/sre-book/>
- Google SRE. **Site Reliability Workbook**: <https://sre.google/workbook/>
- Google SRE. **Implementing SLOs**: <https://sre.google/workbook/implementing-slos/>
- Google SRE. **Alerting on SLOs**: <https://sre.google/workbook/alerting-on-slos/>
- OpenTelemetry. **Signals**: <https://opentelemetry.io/docs/concepts/signals/>
- OpenTelemetry. **OpenTelemetry is a CNCF Graduated Project**: <https://opentelemetry.io/blog/2026/otel-graduates/>
- CNCF. **OpenTelemetry Graduation Announcement**: <https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/>
- CNCF. **Annual Cloud Native Survey 2025**: <https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/>
- DORA. **State of AI-assisted Software Development 2025**: <https://dora.dev/dora-report-2025/>
- DORA. **Platform Engineering Capability**: <https://dora.dev/capabilities/platform-engineering/>
- SLSA. **Specification v1.2**: <https://slsa.dev/spec/v1.2/>
- SLSA. **Announcing SLSA v1.2**: <https://slsa.dev/blog/2025/11/announce-slsa-v1.2>
- Kubernetes. **Liveness, Readiness, and Startup Probes**: <https://kubernetes.io/docs/concepts/workloads/pods/probes/>
- Kubernetes. **Horizontal Pod Autoscaling**: <https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/>
- FinOps Foundation. **FinOps Framework**: <https://www.finops.org/framework/>

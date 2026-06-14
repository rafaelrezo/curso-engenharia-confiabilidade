# Rubricas de avaliação SRE

Estas rubricas definem o padrão mínimo para os artefatos produzidos no curso.
Elas ajudam o estudante a saber quando um exercício está pronto para uso
profissional e ajudam a manter os capítulos consistentes.

## Como usar

Para cada artefato, avalie três níveis:

| Nível | Interpretação |
| --- | --- |
| Insuficiente | O artefato existe, mas não orienta decisão operacional. |
| Aceitável | O artefato orienta uma decisão real e pode ser usado por outra pessoa. |
| Profissional | O artefato é claro, testável, revisável e conectado a métricas ou evidências. |

## SLO e error budget

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Jornada | Mede componente interno sem relação clara com usuário. | Mede uma jornada ou operação relevante. | Define eventos elegíveis, eventos bons e exclusões justificadas. |
| Janela | Não define janela ou usa período arbitrário. | Define janela de medição. | Explica por que a janela serve para resposta e governança. |
| Decisão | Não muda release, plantão ou prioridade. | Define consequência quando o orçamento está em risco. | Inclui política para orçamento saudável, burn rate alto e orçamento esgotado. |
| Fonte de dados | Usa métrica sem origem clara. | Aponta fonte de telemetria. | Define consulta, agregação, dono e riscos de medição. |

## Alerta

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Impacto | Alerta sobre métrica interna sem impacto claro. | Relaciona o sinal a usuário, SLO ou risco iminente. | Usa janela, severidade e burn rate ou condição equivalente. |
| Ação | Não diz o que fazer. | Indica primeira ação e dono. | Aponta runbook, contexto, dashboard e condição de escalonamento. |
| Ruído | Dispara com frequência sem revisão. | Tem critério para página, ticket ou dashboard. | Mede precisão, recorrência e revisão pós-incidente. |

## Runbook

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Escopo | Não define quando usar. | Define alerta, serviço e sintomas. | Define pré-condições, riscos e quando não usar. |
| Diagnóstico | Lista comandos soltos. | Traz primeiros passos de diagnóstico. | Organiza hipóteses, sinais esperados e links para dashboards. |
| Mitigação | Não orienta recuperação. | Descreve mitigação segura. | Inclui rollback, escalonamento, comunicação e validação pós-ação. |
| Manutenção | Não tem dono. | Tem dono e data de revisão. | Foi testado em simulado, incidente ou mudança real. |

## Postmortem

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Cultura | Procura culpados. | Descreve fatos sem culpa. | Explica condições sistêmicas e trade-offs reais. |
| Linha do tempo | Incompleta ou baseada em memória. | Registra eventos principais. | Inclui detecção, mitigação, comunicação e decisões com horários. |
| Ações | Lista desejos genéricos. | Define ações com dono e prazo. | Cada ação tem critério de conclusão e evidência de redução de risco. |
| Aprendizado | Fica isolado. | É compartilhado com a equipe. | Alimenta backlog, SLO, alertas, testes e treinamento. |

## Plano de release e rollback

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Artefato | Não identifica versão ou configuração. | Identifica versão, commit e mudança. | Usa artefato imutável, provenance, SBOM ou evidência equivalente. |
| Rollout | Faz deploy direto sem limite de exposição. | Define canário ou fase inicial. | Inclui critérios objetivos de promover, pausar e reverter. |
| Rollback | Existe só como intenção. | Descreve como voltar código ou configuração. | Foi testado e considera dados, schema, flags e dependências. |

## Teste de confiabilidade

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Hipótese | Executa falha sem pergunta clara. | Define hipótese e escopo. | Define métrica de sucesso, abort criteria e impacto máximo permitido. |
| Ambiente | Testa sem isolamento ou comunicação. | Define ambiente e janela. | Inclui comunicação, rollback, observabilidade e dono de decisão. |
| Resultado | Apenas relata que passou ou falhou. | Registra achado e ação. | Conecta resultado a SLO, runbook, alerta ou mudança de arquitetura. |

## Restauração e integridade de dados

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Objetivo | Não define RPO/RTO. | Define RPO e RTO esperados. | Mede RPO/RTO real em exercício de restauração. |
| Backup | Assume que backup existe. | Documenta fonte e frequência. | Testa restore, checksum, permissões e cenário de corrupção. |
| Validação | Não prova integridade. | Valida amostra de dados. | Valida invariantes de negócio e registra lacunas. |

## PRR e prontidão para produção

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Risco | Checklist genérico. | Lista riscos por jornada e dependência. | Prioriza riscos por impacto, probabilidade e detecção. |
| Capacidade | Não valida carga esperada. | Estima capacidade inicial. | Inclui teste, margem, autoscaling e plano para limite. |
| Operação | Não define plantão ou suporte. | Define dono e runbooks principais. | Inclui SLO, alertas, rollback, status, treinamento e critérios de lançamento. |

## Roadmap de confiabilidade

| Critério | Insuficiente | Aceitável | Profissional |
| --- | --- | --- | --- |
| Priorização | Lista melhorias sem ordem. | Ordena por risco e esforço. | Conecta cada item a SLO, incidente, toil, capacidade ou risco de negócio. |
| Evidência | Usa opinião. | Usa métricas ou exemplos. | Usa dados históricos, tendência e critério de sucesso. |
| Governança | Não define revisão. | Define dono e prazo. | Define cadência de revisão, trade-offs e decisão de parar ou continuar. |

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Implementing SLOs**. <https://sre.google/workbook/implementing-slos/>
- Google SRE. **Alerting on SLOs**. <https://sre.google/workbook/alerting-on-slos/>
- Google SRE. **Postmortem Culture**. <https://sre.google/sre-book/postmortem-culture/>
- Google SRE. **Canarying Releases**. <https://sre.google/workbook/canarying-releases/>

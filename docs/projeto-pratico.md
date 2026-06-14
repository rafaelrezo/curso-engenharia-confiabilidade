# Projeto prático - Checkout API

O curso usa um serviço didático único para transformar conceitos de SRE em
artefatos profissionais. O objetivo não é construir uma aplicação completa
primeiro, mas usar o mesmo contexto operacional ao longo dos capítulos para que
cada prática tenha continuidade.

## Serviço base

O serviço didático é uma plataforma simples de checkout:

```text
usuário -> gateway -> checkout-api -> banco de pedidos
                         |
                         +-> fila de pagamentos -> payment-worker -> provedor externo
                         |
                         +-> estoque-api
                         |
                         +-> observabilidade
```

## Componentes

| Componente | Responsabilidade | Risco principal |
| --- | --- | --- |
| `gateway` | Receber tráfego e aplicar roteamento. | Roteamento incorreto, latência ou perda de health check. |
| `checkout-api` | Validar carrinho, criar pedido e iniciar pagamento. | Erro alto, latência de cauda e falha em dependências. |
| `orders-db` | Guardar pedidos e status de pagamento. | Perda, corrupção, indisponibilidade ou restauração lenta. |
| `payment-queue` | Desacoplar checkout e processamento de pagamento. | Atraso, duplicidade, reprocessamento inseguro ou acúmulo. |
| `payment-worker` | Processar pagamentos de forma assíncrona. | Falha em retry, idempotência ruim ou integração instável. |
| `payment-provider` | Simular dependência externa. | Latência, erro intermitente, quota e indisponibilidade. |
| `inventory-api` | Reservar estoque. | Inconsistência e dependência lenta. |
| `telemetria` | Expor métricas, logs, traces e eventos de mudança. | Ruído, cardinalidade alta ou sinais desconectados do usuário. |

## Jornada crítica

A jornada crítica inicial é:

1. usuário envia carrinho válido;
2. `checkout-api` cria pedido;
3. pagamento é enfileirado;
4. worker processa pagamento;
5. usuário recebe confirmação ou estado pendente claro.

O curso deve medir essa jornada pelo resultado percebido pelo usuário, não só
pelo estado interno de máquinas.

## Modos de falha simulados

| Falha | Capítulos relacionados | Aprendizado esperado |
| --- | --- | --- |
| Aumento de erro 5xx no checkout | 02, 04, 07, 08, 09 | SLO, alerta, triagem, incidente e postmortem. |
| Provedor de pagamento lento | 04, 08, 13, 14 | Latência de cauda, traces, timeout, retry e degradação. |
| Fila acumulando mensagens | 04, 10, 16 | Saturação, atraso, backpressure e frescor. |
| Worker processando pagamento duplicado | 11, 16, 17 | Idempotência, teste de confiabilidade e integridade de dados. |
| Deploy com regressão parcial | 05, 07, 11, 18 | Canário, rollback, feature flag e critérios de parada. |
| Banco indisponível ou corrompido | 15, 17 | Estado crítico, restore, RPO/RTO e validação pós-recuperação. |
| Equipe com excesso de alertas e tickets | 03, 19, 20, 21, 22, 23 | Toil, plantão, interrupções, colaboração e modelo de engajamento. |

## Artefatos por capítulo

| Capítulo | Artefato incremental |
| --- | --- |
| 01 | Mapa operacional do `checkout-api`, donos, dependências e jornada crítica. |
| 02 | Documento de SLI, SLO, SLA interno e error budget da jornada de checkout. |
| 03 | Auditoria de toil com top tickets, tarefas manuais e proposta de remoção. |
| 04 | Dashboard mínimo com latência, tráfego, erros, saturação e eventos de deploy. |
| 05 | Pipeline de release com artefato versionado, canário, rollback e evidência. |
| 06 | Inventário de flags, endpoints, jobs e dependências candidatas a remoção. |
| 07 | Política de alertas e runbook do alerta `CheckoutHighErrorRate`. |
| 08 | Registro de investigação com linha do tempo, hipóteses e evidências. |
| 09 | Documento vivo de incidente, comunicação e postmortem sem culpa. |
| 10 | Catálogo mensal de incidentes e quase-incidentes com análise de tendência. |
| 11 | Plano de teste de confiabilidade com hipótese, escopo e critério de abortar. |
| 12 | PRD enxuto de uma ferramenta interna para reduzir toil ou melhorar decisão. |
| 13 | Desenho de roteamento, health checks e failover do checkout. |
| 14 | Política de timeout, retry, jitter, circuit breaker e degradação. |
| 15 | Documento de estados críticos, quorum, liderança e risco de split-brain. |
| 16 | Desenho de pipeline assíncrono com idempotência, backpressure e DLQ. |
| 17 | Plano de backup, restore, RPO, RTO e validação de integridade. |
| 18 | Production readiness review e plano de lançamento gradual. |
| 19 | Matriz 30/60/90 para formar uma pessoa nova no plantão do serviço. |
| 20 | Política de interrupções, canais e triagem de suporte operacional. |
| 21 | Rescue plan de 30 dias para serviço em sobrecarga operacional. |
| 22 | Pauta de reunião de produção e ADR de decisão operacional. |
| 23 | Contrato de engajamento SRE com RACI, ownership e limites de suporte. |
| 24 | Relatório de quase-incidente e checklist inspirado em setores críticos. |
| 25 | Dossiê final de confiabilidade e roadmap de maturidade do serviço. |

## Dossiê final

Ao final, o estudante deve entregar um dossiê SRE do `checkout-api` com:

- mapa de serviço e dependências;
- SLO e error budget;
- dashboard e política de alerta;
- runbook;
- pipeline e plano de rollback;
- teste de falha;
- catálogo de incidentes;
- postmortem;
- plano de restauração;
- modelo de operação e engajamento;
- roadmap de confiabilidade.

## Critério de qualidade

Um artefato é aceitável quando:

- deixa claro qual risco reduz;
- melhora uma decisão operacional real;
- tem dono, entrada, saída e evidência;
- pode ser entendido por uma pessoa nova;
- evita depender apenas de memória oral;
- conecta ferramenta, processo e comportamento esperado.

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Implementing SLOs**. <https://sre.google/workbook/implementing-slos/>
- Google SRE. **Alerting on SLOs**. <https://sre.google/workbook/alerting-on-slos/>
- OpenTelemetry. **Signals**. <https://opentelemetry.io/docs/concepts/signals/>
- Kubernetes. **Liveness, Readiness, and Startup Probes**. <https://kubernetes.io/docs/concepts/workloads/pods/probes/>

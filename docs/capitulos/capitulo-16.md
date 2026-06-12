# Capítulo 16 - Agendamento distribuído e pipelines confiáveis

## Objetivos de aprendizagem

- Explicar por que **jobs periódicos** e **pipelines** são sistemas distribuídos com estado.
- Aplicar idempotência, liderança, controle de duplicidade e monitoramento de completude.
- Projetar workflows que toleram atraso, falha parcial e reexecução.

## Síntese

Cron parece simples em uma máquina única, mas se torna um problema distribuído quando há múltiplas réplicas, failover, estado persistente e escala. Pipelines de dados ampliam o mesmo problema: etapas dependentes, carga irregular, reprocessamento, atraso, completude e corretude. A confiabilidade vem de tratar jobs e pipelines como workflows com estado explícito, execução idempotente e sinais de sucesso além de "o processo rodou".

Em uma frase: **agendamento e pipelines confiáveis tornam explícitos estado, liderança, idempotência, atraso e corretude do resultado**.

## Por que isso importa

Muitos serviços dependem de tarefas fora do caminho síncrono: fechamento financeiro, recomputação de índice, expiração de sessão, envio de relatório, compactação, treinamento de modelo, ETL e reconciliação de dados. Quando esses workflows falham silenciosamente, o usuário percebe dados atrasados, incompletos ou incorretos.

## Conceitos essenciais

### **Jobs periódicos como sistemas distribuídos**

Um **job periódico** precisa saber quando deve rodar, se já rodou, se falhou, se pode repetir e quem é responsável por executar. Em escala, essas perguntas exigem estado confiável.

Sem esse controle, a falha comum é dupla: execução duplicada quando há competição entre réplicas ou execução perdida durante failover.

### **Liderança e coordenação**

**Liderança** define qual instância toma decisões de agendamento. Coordenação por consenso ou armazenamento fortemente consistente ajuda a evitar que duas instâncias executem o mesmo trabalho de forma incompatível.

Nem todo job precisa de consenso sofisticado, mas todo job crítico precisa de uma regra clara contra duplicidade perigosa.

### **Idempotência**

**Idempotência** permite repetir uma execução sem causar dano. É uma das propriedades mais importantes para recuperação, porque falhas parciais são comuns: uma etapa pode concluir, registrar metade do estado e cair antes de confirmar sucesso.

Quando idempotência não é possível, a equipe precisa de deduplicação, transações, compensações ou reconciliação explícita.

### **Estado do workflow**

**Estado do workflow** descreve etapas pendentes, em execução, concluídas, atrasadas, falhas ou aguardando dependência. Esse estado deve ser observável e recuperável.

Logs soltos não bastam. A operação precisa saber o que está preso, há quanto tempo e qual impacto isso causa.

### **Pipelines com estágios**

**Pipelines** encadeiam estágios. Cada estágio pode ter volume, latência, dependências e critérios de qualidade diferentes. O sucesso do pipeline depende do resultado final, não apenas da execução de cada processo.

Monitorar apenas "job executou" é frágil. É preciso medir completude, frescor, contagem esperada, validade de dados e atraso por estágio.

### **Thundering herd**

**Thundering herd** ocorre quando muitos jobs ou clientes acordam ao mesmo tempo e criam pico artificial. Agendamentos em horários redondos, retries sincronizados e dependências compartilhadas podem causar esse padrão.

Espalhar horários, usar jitter e limitar concorrência reduz picos desnecessários.

## Aplicação prática

Escolha um job ou pipeline importante:

- Liste estados possíveis: pendente, rodando, concluído, falhou, atrasado e reexecutando.
- Verifique se a execução é idempotente ou se há deduplicação.
- Identifique quem lidera ou coordena execução em caso de múltiplas réplicas.
- Defina métricas de atraso, completude e corretude.
- Adicione jitter ou limites de concorrência se houver picos artificiais.

## Diagrama de apoio

```mermaid
flowchart LR
    Schedule["Agendamento"] --> Leader["Liderança / coordenação"]
    Leader --> State["Estado do job"]
    State --> Stage1["Estágio 1"]
    Stage1 --> Stage2["Estágio 2"]
    Stage2 --> Validate["Validação de completude"]
    Validate --> Done["Resultado confiável"]
    Stage2 -->|Falha| Retry["Reexecução idempotente"]
    Retry --> State
```

## Erros comuns

- Considerar job bem-sucedido só porque o processo iniciou.
- Ignorar execução duplicada ou perdida durante failover.
- Criar pipeline sem métrica de frescor, completude ou corretude.
- Usar retries sincronizados que geram thundering herd.
- Depender de intervenção manual para reprocessar falhas frequentes.

## Perguntas para revisão

1. Como a equipe sabe que um job crítico não foi perdido?
2. O que acontece se o mesmo job rodar duas vezes?
3. Qual métrica prova que o pipeline entregou dados corretos e completos?

## Exercícios

### Compreensão

Explique por que um cron distribuído precisa de estado e liderança.

### Aplicação

Modele um pipeline com três estágios e defina métricas para atraso, completude e corretude.

### Análise

Identifique um workflow que causaria impacto ao usuário mesmo sem derrubar APIs síncronas.

## Relação com práticas atuais

Hoje esses padrões aparecem em orquestradores de workflow, Kubernetes CronJobs, filas, ferramentas de data engineering, pipelines de ML, GitOps e rotinas de reconciliação. A ferramenta não elimina o problema: jobs críticos ainda precisam de estado visível, reexecução segura e validação do resultado entregue.

## Recursos complementares

- **Google SRE Book - Distributed Periodic Scheduling with Cron:** <https://sre.google/sre-book/distributed-periodic-scheduling/>
- **Google SRE Book - Data Processing Pipelines:** <https://sre.google/sre-book/data-processing-pipelines/>
- **OpenTelemetry Signals:** <https://opentelemetry.io/docs/concepts/signals/>

## Fechamento

Guarde a ideia principal: **workflows confiáveis não dependem de sorte no horário de execução; eles têm estado, coordenação e validação explícita**.

Próximo: [Capítulo 17 - Integridade de dados: o que você lê e o que você escreveu](capitulo-17.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Distributed Periodic Scheduling with Cron**. <https://sre.google/sre-book/distributed-periodic-scheduling/>
- Google SRE. **Data Processing Pipelines**. <https://sre.google/sre-book/data-processing-pipelines/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

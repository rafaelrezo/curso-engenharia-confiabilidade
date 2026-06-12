# Capítulo 18 - Lançamento de produtos confiáveis em escala

## Objetivos de aprendizagem

- Explicar o problema de confiabilidade tratado pelo tema.
- Reconhecer onde o tema aparece em um serviço real.
- Aplicar o conceito em uma decisão operacional ou de engenharia.

## Síntese

Launch Coordination Engineering como função que ajuda produtos a chegar a produção com confiabilidade. Checklists de arquitetura, dependências, integração, capacidade, modos de falha, comportamento de clientes, automação e rollout reduzem surpresa. Técnicas como flags e lançamentos em fases permitem aprender com risco limitado.

Em uma frase: **Lançamentos confiáveis exigem coordenação, checklists, rollouts graduais e análise de modos de falha.**

## Por que isso importa

**Launch Coordination Engineering** importa porque serviços reais falham sob mudança, carga, dependências lentas, estado distribuído e comportamento humano. A equipe reduz surpresa quando transforma esse risco em rotina operacional clara, sinais confiáveis e decisões treinadas antes da crise.

## Conceitos essenciais

### **Launch Coordination Engineering**

**Launch Coordination Engineering**: É a coordenação de lançamento com foco em riscos, dependências e prontidão operacional. Ela ajuda produto e engenharia a lançar sem improviso.

Uma forma simples de aplicar isso é: Criar checklist de lançamento para um serviço.

### **checklist de lançamento**

**checklist de lançamento**: É uma memória operacional externa. Ajuda a evitar esquecimentos em lançamentos, incidentes e mudanças repetidas.

No dia a dia, isso aparece quando a equipe precisa planejar fases e critérios de rollback.

### **rollout gradual**

**rollout gradual**: É a liberação gradual de uma mudança. Permite observar impacto em pequena escala antes de afetar todos os usuários.

Esse conceito fica concreto quando a equipe consegue incluir modos de falha e abusos de clientes no plano.

### **feature flags**

**feature flags**: Flags permitem ativar, desativar ou limitar funcionalidades sem novo deploy. Elas reduzem risco, mas precisam de ciclo de limpeza.

Uma forma simples de aplicar isso é: Criar checklist de lançamento para um serviço.

### **planejamento de capacidade**

**planejamento de capacidade**: É transformar intenção, demanda e restrições em capacidade e ações. Em SRE, planejamento ruim vira incidente futuro.

No dia a dia, isso aparece quando a equipe precisa planejar fases e critérios de rollback.


## Aplicação prática

Para evitar burocracia, escolha um serviço concreto e execute uma ação pequena:

- Criar checklist de lançamento para um serviço.
- Planejar fases e critérios de rollback.
- Incluir modos de falha e abusos de clientes no plano.

Depois da ação, procure uma evidência simples de melhoria: menos alertas
irrelevantes, recuperação mais rápida, dependência mais clara, deploy menos
arriscado, métrica mais confiável ou decisão mais fácil de explicar.

## Diagrama de apoio

```mermaid
flowchart LR
    Tema["Lançamento de produtos confiáveis em escala"] --> C1["Launch Coordination Engineering"]
    C1 --> C2["checklist de lançamento"]
    C2 --> C3["rollout gradual"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

## Erros comuns

- Aplicar a prática como checklist sem conectar a risco real do serviço.
- Criar documentação ou automação sem validar durante incidentes ou mudanças reais.
- Medir apenas sinais internos e esquecer o impacto percebido pelo usuário.

## Perguntas para revisão

1. Qual risco operacional **Launch Coordination Engineering** ajuda a reduzir?
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

Em ambientes atuais, este tema aparece em revisões de serviço, plataformas internas, pipelines, dashboards, políticas de rollout e práticas de cloud native. A tecnologia muda; o princípio continua sendo tornar risco, responsabilidade e evidência visíveis.

## Recursos complementares

- **Livro oficial online do Google SRE:** <https://sre.google/sre-book/>
- **The Site Reliability Workbook:** <https://sre.google/workbook/>
- **Google SRE Book - Reliable Product Launches at Scale:** <https://sre.google/sre-book/reliable-product-launches/>
- **Google SRE Book - Launch Coordination Checklist:** <https://sre.google/sre-book/launch-checklist/>
- **Site Reliability Workbook - Canarying Releases:** <https://sre.google/workbook/canarying-releases/>

## Fechamento

Guarde a ideia principal: **Lançamentos confiáveis exigem coordenação, checklists, rollouts graduais e análise de modos de falha.**

Próximo: [Capítulo 19 - Acelerando os SREs para chegar ao plantão e além](capitulo-19.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- **Google SRE Book - Reliable Product Launches at Scale:** <https://sre.google/sre-book/reliable-product-launches/>
- **Google SRE Book - Launch Coordination Checklist:** <https://sre.google/sre-book/launch-checklist/>
- **Google Cloud Well-Architected Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

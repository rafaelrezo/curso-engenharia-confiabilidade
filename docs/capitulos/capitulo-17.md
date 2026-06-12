# Capítulo 17 - Integridade de dados: o que você lê e o que você escreveu

## Objetivos de aprendizagem

- Explicar o problema de confiabilidade tratado pelo tema.
- Reconhecer onde o tema aparece em um serviço real.
- Aplicar o conceito em uma decisão operacional ou de engenharia.

## Síntese

O capítulo diferencia backup, arquivamento, replicação, deteccao precoce e recuperação. A prioridade é preservar disponibilidade por meio de integridade de dados verificável. Estrategias robustas combinam defesa em profundidade, remoção soft, backups recuperáveis, replicação, testes de restauracao e atitude de 'confiar, mas verificar'.

Em uma frase: **Backups só têm valor quando a recuperação é confiável, testada e alinhada a integridade percebida pelo usuário.**

## Por que isso importa

**integridade de dados** importa porque serviços reais falham sob mudança, carga, dependências lentas, estado distribuído e comportamento humano. A equipe reduz surpresa quando transforma esse risco em rotina operacional clara, sinais confiáveis e decisões treinadas antes da crise.

## Conceitos essenciais

### **integridade de dados**

**integridade de dados**: É a garantia de que dados permanecem corretos, completos e recuperáveis. Usuários percebem integridade pelo resultado, não pela arquitetura.

Uma forma simples de aplicar isso é: Testar restauracao de um backup real.

### **backup versus arquivamento**

**backup versus arquivamento**: É apenas uma parte da estratégia de recuperação. O que importa é conseguir restaurar dados corretos dentro do tempo necessário para o negócio.

No dia a dia, isso aparece quando a equipe precisa definir RPO e RTO para dados críticos.

### **recuperação**

**recuperação**: É restaurar serviço ou dados após falha. A estratégia só é confiável quando é testada e tem objetivo de tempo e perda aceitável.

Esse conceito fica concreto quando a equipe consegue adicionar deteccao de exclusao ou corrupcao silenciosa.

### **replicação**

**replicação**: É manter cópias de dados ou estado. Ela melhora disponibilidade, mas também pode replicar corrupção se não houver detecção e controle.

Uma forma simples de aplicar isso é: Testar restauracao de um backup real.

### **defesa em profundidade**

**defesa em profundidade**: É combinar camadas de prevenção, detecção e recuperação. Nenhuma camada isolada deve ser a única proteção de dados críticos.

No dia a dia, isso aparece quando a equipe precisa definir RPO e RTO para dados críticos.


## Aplicação prática

Para evitar burocracia, escolha um serviço concreto e execute uma ação pequena:

- Testar restauracao de um backup real.
- Definir RPO e RTO para dados críticos.
- Adicionar deteccao de exclusao ou corrupcao silenciosa.

Depois da ação, procure uma evidência simples de melhoria: menos alertas
irrelevantes, recuperação mais rápida, dependência mais clara, deploy menos
arriscado, métrica mais confiável ou decisão mais fácil de explicar.

## Diagrama de apoio

```mermaid
flowchart LR
    Tema["Integridade de dados: o que você lê e o que você escreveu"] --> C1["integridade de dados"]
    C1 --> C2["backup versus arquivamento"]
    C2 --> C3["recuperação"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

## Erros comuns

- Aplicar a prática como checklist sem conectar a risco real do serviço.
- Criar documentação ou automação sem validar durante incidentes ou mudanças reais.
- Medir apenas sinais internos e esquecer o impacto percebido pelo usuário.

## Perguntas para revisão

1. Qual risco operacional **integridade de dados** ajuda a reduzir?
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
- **Google SRE Book - Data Integrity:** <https://sre.google/sre-book/data-integrity/>

## Fechamento

Guarde a ideia principal: **Backups só têm valor quando a recuperação é confiável, testada e alinhada a integridade percebida pelo usuário.**

Próximo: [Capítulo 18 - Lançamento de produtos confiáveis em escala](capitulo-18.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- **Google SRE Book - Data Integrity:** <https://sre.google/sre-book/data-integrity/>
- **Google Cloud Well-Architected Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

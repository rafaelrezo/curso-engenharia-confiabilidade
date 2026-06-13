# Capítulo 20 - Lidando com interrupções

## Objetivos de aprendizagem

- Identificar como **carga operacional** aparece em produção.
- Aplicar o procedimento do tema em uma jornada, mudança, incidente ou dependência real.
- Produzir um artefato prático: métrica, política, checklist, runbook ou plano de melhoria.

## Síntese

Carga operacional sob a perspectiva humana. Sistemas complexos geram interrupções, mudanças de contexto e decisões sob pressão. Equipes melhores reduzem ruído, fornecem instruções claras, preservam fluxo cognitivo e projetam processos para que pessoas façam a tarefa certa no momento certo.

Em uma frase: **Interrupções cognitivas reduzem qualidade; processos devem proteger foco e orientar a ação.**

## Por que isso importa

**carga operacional** importa porque sistemas de produção são mantidos por pessoas, rotinas, decisões e relações entre equipes. Sem gestão explícita, mesmo boas práticas técnicas se degradam em filas de suporte, interrupções constantes e responsabilidades ambíguas.

## Conceitos essenciais

### **carga operacional**

**carga operacional**: É uma prática que transforma uma preocupação operacional em decisão concreta. Ela aparece quando a equipe precisa escolher entre aceitar risco, automatizar, simplificar, melhorar observabilidade, mudar o processo de release ou corrigir a causa raiz de um problema recorrente.

Uma forma simples de aplicar isso é: Medir fontes de interrupcao da equipe.

### **interrupções**

**interrupções**: É perda ou degradação relevante de serviço. Registrar interrupções permite medir tendência, impacto e causas recorrentes.

No dia a dia, isso aparece quando a equipe precisa separar canais urgentes de canais informativos.

### **fluxo cognitivo**

**fluxo cognitivo**: É a capacidade de manter atenção em uma tarefa complexa. Interrupções frequentes quebram raciocínio e aumentam erro operacional.

Esse conceito fica concreto quando a equipe consegue criar instruções claras para alertas críticos.

### **instrução acionável**

**instrução acionável**: É uma prática que transforma uma preocupação operacional em decisão concreta. Ela aparece quando a equipe precisa escolher entre aceitar risco, automatizar, simplificar, melhorar observabilidade, mudar o processo de release ou corrigir a causa raiz de um problema recorrente.

Uma forma simples de aplicar isso é: Medir fontes de interrupcao da equipe.

### **redução de ruído**

**redução de ruído**: É uma prática que transforma uma preocupação operacional em decisão concreta. Ela aparece quando a equipe precisa escolher entre aceitar risco, automatizar, simplificar, melhorar observabilidade, mudar o processo de release ou corrigir a causa raiz de um problema recorrente.

No dia a dia, isso aparece quando a equipe precisa separar canais urgentes de canais informativos.


## Aplicação prática

Escolha um serviço concreto e transforme o tema em uma ação verificável:

- Medir fontes de interrupcao da equipe.
- Separar canais urgentes de canais informativos.
- Criar instruções claras para alertas críticos.

Depois da ação, registre a evidência de melhoria: menos alertas irrelevantes,
recuperação mais rápida, dependência mais clara, deploy menos arriscado, métrica
mais confiável ou decisão mais fácil de explicar.

## Aprofundamento prático

Interrupções cognitivas são trabalho invisível. Mensagens soltas, alertas informativos, reuniões sem decisão e pedidos urgentes quebram fluxo e aumentam erro. O capítulo sobre interrupções ajuda a tratar atenção humana como recurso limitado.

Procedimento recomendado:

1. Meça fontes de interrupção por uma semana: alertas, chats, tickets, reuniões e pedidos diretos.
2. Classifique urgência real: agora, hoje, esta semana ou informativo.
3. Crie canais separados para página, suporte, dúvidas e anúncios.
4. Defina horário de triagem para trabalho não urgente.
5. Revise instruções de alertas para que a primeira ação seja clara.

Exemplo de política:

| Tipo | Canal | Resposta esperada |
| --- | --- | --- |
| Impacto em produção | Pager | Imediata |
| Degradação sem urgência | Ticket | Mesmo dia útil |
| Dúvida de uso | Canal de suporte | Próxima triagem |
| Anúncio | Canal informativo | Sem interrupção |

A boa gestão de interrupções não isola SRE do resto da empresa. Ela protege foco para que respostas urgentes sejam melhores.

## Diagrama de apoio

```mermaid
flowchart LR
    Tema["Lidando com interrupções"] --> C1["carga operacional"]
    C1 --> C2["interrupções"]
    C2 --> C3["fluxo cognitivo"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

## Erros comuns

- Tratar o problema como falta de processo quando a causa é ambiguidade de responsabilidade.
- Criar reuniões, checklists ou treinamentos sem dono e sem revisão.
- Separar gestão de SRE da realidade técnica dos serviços em produção.

## Perguntas para revisão

1. Qual risco operacional **carga operacional** ajuda a reduzir?
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

A prática moderna usa métricas, logs e traces com contexto compartilhado. Alertas devem representar impacto ou risco real para o usuário; o restante deve virar dashboard, análise assíncrona ou automação.

## Recursos complementares

- **Livro oficial online do Google SRE:** <https://sre.google/sre-book/>
- **The Site Reliability Workbook:** <https://sre.google/workbook/>
- **Google SRE Book - Dealing with Interrupts:** <https://sre.google/sre-book/dealing-with-interrupts/>
- **Google SRE Resources:** <https://sre.google/resources/>

## Fechamento

Guarde a ideia principal: **Interrupções cognitivas reduzem qualidade; processos devem proteger foco e orientar a ação.**

Próximo: [Capítulo 21 - Incluindo um SRE para se recuperar de uma sobrecarga operacional](capitulo-21.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- **Google SRE Book - Dealing with Interrupts:** <https://sre.google/sre-book/dealing-with-interrupts/>
- **Google Cloud Well-Architected Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

# Capítulo 06 - Simplicidade

## Objetivos de aprendizagem

- Explicar o problema de confiabilidade tratado pelo tema.
- Reconhecer onde o tema aparece em um serviço real.
- Aplicar o conceito em uma decisão operacional ou de engenharia.

## Síntese

Simplicidade como requisito de confiabilidade. Cada linha de código, feature, API ou dependência acrescenta custo operacional e superfície de falha. A simplicidade não significa imobilismo; significa preservar interfaces pequenas, modularidade, releases compreensíveis e disposição para remover código que não paga seu custo.

Em uma frase: **Sistemas mais simples são mais fáceis de operar, entender, alterar e recuperar.**

## Por que isso importa

Sem **estabilidade versus agilidade**, a equipe tende a discutir confiabilidade por opinião: um grupo pede mais velocidade, outro pede mais estabilidade, e ninguém consegue explicar qual risco está sendo aceito. A decisão melhora quando o risco vira critério técnico, mensurável e negociável.

## Conceitos essenciais

### **estabilidade versus agilidade**

**estabilidade versus agilidade**: É o equilíbrio entre mudar rápido e manter comportamento confiável. SRE transforma esse conflito em decisão baseada em SLO, risco e custo de falha.

Uma forma simples de aplicar isso é: Listar features pouco usadas que aumentam complexidade.

### **linhas de código negativas**

**linhas de código negativas**: É a ideia de que remover código pode aumentar valor. Menos código reduz caminhos de falha, manutenção, testes necessários e complexidade cognitiva.

No dia a dia, isso aparece quando a equipe precisa propor uma remoção segura de código ou configuração.

### **APIs mínimas**

**APIs mínimas**: São interfaces pequenas e focadas. APIs menores reduzem combinações possíveis, estados inválidos e acoplamento entre equipes.

Esse conceito fica concreto quando a equipe consegue revisar uma API buscando reduzir estados e exceções.

### **modularidade**

**modularidade**: É separar responsabilidades com limites claros. Um módulo bom pode falhar, evoluir ou ser substituído com menor impacto no resto do sistema.

Uma forma simples de aplicar isso é: Listar features pouco usadas que aumentam complexidade.

### **simplicidade em releases**

**simplicidade em releases**: É reduzir variáveis em cada lançamento. Mudanças menores e mais compreensíveis tornam detecção, rollback e aprendizado mais rápidos.

No dia a dia, isso aparece quando a equipe precisa propor uma remoção segura de código ou configuração.


## Aplicação prática

Para evitar burocracia, escolha um serviço concreto e execute uma ação pequena:

- Listar features pouco usadas que aumentam complexidade.
- Propor uma remoção segura de código ou configuração.
- Revisar uma API buscando reduzir estados e exceções.

Depois da ação, procure uma evidência simples de melhoria: menos alertas
irrelevantes, recuperação mais rápida, dependência mais clara, deploy menos
arriscado, métrica mais confiável ou decisão mais fácil de explicar.

## Diagrama de apoio

```mermaid
flowchart LR
    Tema["Simplicidade"] --> C1["estabilidade versus agilidade"]
    C1 --> C2["linhas de código negativas"]
    C2 --> C3["APIs mínimas"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

## Erros comuns

- Adicionar abstrações antes de remover complexidade acidental.
- Manter features ou APIs pouco usadas por medo de limpeza.
- Confundir simplicidade com falta de capacidade de evolução.

## Perguntas para revisão

1. Qual risco operacional **estabilidade versus agilidade** ajuda a reduzir?
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

Em sistemas atuais, simplicidade compete com microsserviços, múltiplas clouds, configuração dinâmica e pilhas de observabilidade. A recomendação prática é reduzir estados, dependências e exceções antes de adicionar mais plataforma.

## Recursos complementares

- **Livro oficial online do Google SRE:** <https://sre.google/sre-book/>
- **The Site Reliability Workbook:** <https://sre.google/workbook/>
- **Google SRE Book - Simplicity:** <https://sre.google/sre-book/simplicity/>
- **Site Reliability Workbook - Simplicity:** <https://sre.google/workbook/simplicity/>

## Fechamento

Guarde a ideia principal: **Sistemas mais simples são mais fáceis de operar, entender, alterar e recuperar.**

Próximo: [Capítulo 07 - Alertas acionáveis e plantão saudável](capitulo-07.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- **Google SRE Book - Simplicity:** <https://sre.google/sre-book/simplicity/>
- **Site Reliability Workbook - Simplicity:** <https://sre.google/workbook/simplicity/>
- **Google Cloud Well-Architected Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.

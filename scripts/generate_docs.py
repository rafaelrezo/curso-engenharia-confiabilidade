import re
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CHAPTERS_DIR = DOCS / "capitulos"


PT_BR_REPLACEMENTS = [
    (r"\bO capitulo\b", "O capítulo"),
    (r"\bEste capitulo\b", "Este capítulo"),
    (r"\bNo capitulo\b", "No capítulo"),
    (r"\bIntroducao\b", "Introdução"),
    (r"\bintroducao\b", "introdução"),
    (r"\bConclusao\b", "Conclusão"),
    (r"\bconclusao\b", "conclusão"),
    (r"\bPrincipios\b", "Princípios"),
    (r"\bprincipios\b", "princípios"),
    (r"\bPraticas\b", "Práticas"),
    (r"\bpraticas\b", "práticas"),
    (r"\bpratica\b", "prática"),
    (r"\bpratico\b", "prático"),
    (r"\bpraticos\b", "práticos"),
    (r"\bpraticas\b", "práticas"),
    (r"\bGerenciamento\b", "Gerenciamento"),
    (r"\bgerenciamento\b", "gerenciamento"),
    (r"\baplicacao\b", "aplicação"),
    (r"\bAplicacao\b", "Aplicação"),
    (r"\boperacao\b", "operação"),
    (r"\boperacoes\b", "operações"),
    (r"\bOperacoes\b", "Operações"),
    (r"\bconfiavel\b", "confiável"),
    (r"\bconfiaveis\b", "confiáveis"),
    (r"\bservico\b", "serviço"),
    (r"\bservicos\b", "serviços"),
    (r"\bServicos\b", "Serviços"),
    (r"\bintervencao\b", "intervenção"),
    (r"\bintervencoes\b", "intervenções"),
    (r"\bmensuravel\b", "mensurável"),
    (r"\bmensuraveis\b", "mensuráveis"),
    (r"\bdecisao\b", "decisão"),
    (r"\bdecisoes\b", "decisões"),
    (r"\bacao\b", "ação"),
    (r"\bacoes\b", "ações"),
    (r"\bmudanca\b", "mudança"),
    (r"\bmudancas\b", "mudanças"),
    (r"\blatencia\b", "latência"),
    (r"\beficiencia\b", "eficiência"),
    (r"\bmonitoracao\b", "monitoração"),
    (r"\bemergencia\b", "emergência"),
    (r"\bemergencias\b", "emergências"),
    (r"\bautomacao\b", "automação"),
    (r"\bAutomacao\b", "Automação"),
    (r"\bautomacoes\b", "automações"),
    (r"\bdependencia\b", "dependência"),
    (r"\bdependencias\b", "dependências"),
    (r"\bexperiencia\b", "experiência"),
    (r"\bexperiencias\b", "experiências"),
    (r"\busuario\b", "usuário"),
    (r"\busuarios\b", "usuários"),
    (r"\bUsuario\b", "Usuário"),
    (r"\bmetricas\b", "métricas"),
    (r"\bmetrica\b", "métrica"),
    (r"\btrafego\b", "tráfego"),
    (r"\btrafegos\b", "tráfegos"),
    (r"\bnivel\b", "nível"),
    (r"\bniveis\b", "níveis"),
    (r"\bmedicao\b", "medição"),
    (r"\bmedicoes\b", "medições"),
    (r"\bagregacao\b", "agregação"),
    (r"\bseries\b", "séries"),
    (r"\bserie\b", "série"),
    (r"\bequilibrio\b", "equilíbrio"),
    (r"\bexplícito\b", "explícito"),
    (r"\bexplicito\b", "explícito"),
    (r"\bexplicita\b", "explícita"),
    (r"\bexplicitas\b", "explícitas"),
    (r"\bclassico\b", "clássico"),
    (r"\bseparacao\b", "separação"),
    (r"\bdistribuidos\b", "distribuídos"),
    (r"\bdistribuido\b", "distribuído"),
    (r"\bdistribuicao\b", "distribuição"),
    (r"\bDistribuicao\b", "Distribuição"),
    (r"\bcritico\b", "crítico"),
    (r"\bcriticos\b", "críticos"),
    (r"\bperiodico\b", "periódico"),
    (r"\bperiodicos\b", "periódicos"),
    (r"\bcronograma\b", "cronograma"),
    (r"\bproducao\b", "produção"),
    (r"\bplantao\b", "plantão"),
    (r"\brodizios\b", "rodízios"),
    (r"\bsustentaveis\b", "sustentáveis"),
    (r"\bmanejavel\b", "manejável"),
    (r"\bdocumentacao\b", "documentação"),
    (r"\bremuneracao\b", "remuneração"),
    (r"\brequisicao\b", "requisição"),
    (r"\brequisicoes\b", "requisições"),
    (r"\bdirecao\b", "direção"),
    (r"\bdisponivel\b", "disponível"),
    (r"\bdisponiveis\b", "disponíveis"),
    (r"\bdisponibilidade\b", "disponibilidade"),
    (r"\bseguranca\b", "segurança"),
    (r"\bconfiguracao\b", "configuração"),
    (r"\bconfiguracoes\b", "configurações"),
    (r"\borquestracao\b", "orquestração"),
    (r"\bmaquinas\b", "máquinas"),
    (r"\bdiaria\b", "diária"),
    (r"\bcriticas\b", "críticas"),
    (r"\bcomunicacao\b", "comunicação"),
    (r"\bComunicacao\b", "Comunicação"),
    (r"\bcolaboracao\b", "colaboração"),
    (r"\blicoes\b", "lições"),
    (r"\bLicoes\b", "Lições"),
    (r"\balem\b", "além"),
    (r"\bvoce\b", "você"),
    (r"\ble\b", "lê"),
    (r"\blancamento\b", "lançamento"),
    (r"\blancamentos\b", "lançamentos"),
    (r"\bLancamento\b", "Lançamento"),
    (r"\bLancamentos\b", "Lançamentos"),
    (r"\bevolucao\b", "evolução"),
    (r"\bexposicao\b", "exposição"),
    (r"\breplicacao\b", "replicação"),
    (r"\brecuperacao\b", "recuperação"),
    (r"\bintegracao\b", "integração"),
    (r"\bvalidacao\b", "validação"),
    (r"\bobservavel\b", "observável"),
    (r"\bobservaveis\b", "observáveis"),
    (r"\bobservabilidade\b", "observabilidade"),
    (r"\bexecucao\b", "execução"),
    (r"\bcorrecao\b", "correção"),
    (r"\bcorrecoes\b", "correções"),
    (r"\bpadrao\b", "padrão"),
    (r"\bpadroes\b", "padrões"),
    (r"\bpadronizacao\b", "padronização"),
    (r"\banalise\b", "análise"),
    (r"\bevidencia\b", "evidência"),
    (r"\bevidencias\b", "evidências"),
    (r"\beliminacao\b", "eliminação"),
    (r"\baleatorias\b", "aleatórias"),
    (r"\bespaco\b", "espaço"),
    (r"\buteis\b", "úteis"),
    (r"\butil\b", "útil"),
    (r"\bhipotese\b", "hipótese"),
    (r"\bhipoteses\b", "hipóteses"),
    (r"\bdiagnostico\b", "diagnóstico"),
    (r"\btriagem\b", "triagem"),
    (r"\bavaliacao\b", "avaliação"),
    (r"\bavaliacoes\b", "avaliações"),
    (r"\binterrupcoes\b", "interrupções"),
    (r"\bInterrupcoes\b", "Interrupções"),
    (r"\borganizacao\b", "organização"),
    (r"\borganizacoes\b", "organizações"),
    (r"\btopologia\b", "topologia"),
    (r"\bnecessario\b", "necessário"),
    (r"\bnecessaria\b", "necessária"),
    (r"\bnecessarias\b", "necessárias"),
    (r"\bnecessarios\b", "necessários"),
    (r"\bpossivel\b", "possível"),
    (r"\bpossiveis\b", "possíveis"),
    (r"\bduravel\b", "durável"),
    (r"\bconsequencia\b", "consequência"),
    (r"\bconsequencias\b", "consequências"),
    (r"\btecnica\b", "técnica"),
    (r"\btecnicas\b", "técnicas"),
    (r"\btecnico\b", "técnico"),
    (r"\btecnicos\b", "técnicos"),
    (r"\bmaxima\b", "máxima"),
    (r"\brapidez\b", "rapidez"),
    (r"\bvisao\b", "visão"),
    (r"\bprovisao\b", "provisão"),
    (r"\bnao\b", "não"),
    (r"\bsao\b", "são"),
    (r"\btambem\b", "também"),
    (r"\brapido\b", "rápido"),
    (r"\brapida\b", "rápida"),
    (r"\brapidas\b", "rápidas"),
    (r"\brapidos\b", "rápidos"),
    (r"\bSRE e uma\b", "SRE é uma"),
    (r"\bSRE e a\b", "SRE é a"),
    (r"\bcentral e que\b", "central é que"),
    (r"\bmensagem pratica e que\b", "mensagem prática é que"),
    (r"\bnao e apenas\b", "não é apenas"),
    (r"\brisco e caro\b", "risco é caro"),
    (r"\boperacional e ruim\b", "operacional é ruim"),
    (r"\bautomacao e essencial\b", "automação é essencial"),
    (r"\bAutomação e essencial\b", "Automação é essencial"),
    (r"\brelease nao deve\b", "release não deve"),
    (r"\bA meta e\b", "A meta é"),
    (r"\ba meta e\b", "a meta é"),
    (r"\bA ideia e\b", "A ideia é"),
    (r"\ba ideia e\b", "a ideia é"),
    (r"\bO foco e\b", "O foco é"),
    (r"\bo foco e\b", "o foco é"),
    (r"\bO objetivo e\b", "O objetivo é"),
    (r"\bo objetivo e\b", "o objetivo é"),
    (r"\bO objetivo mais maduro e\b", "O objetivo mais maduro é"),
    (r"\bo objetivo mais maduro e\b", "o objetivo mais maduro é"),
    (r"\bA prioridade e\b", "A prioridade é"),
    (r"\ba prioridade e\b", "a prioridade é"),
    (r"\bA diferenca e\b", "A diferença é"),
    (r"\ba diferenca e\b", "a diferença é"),
    (r"\bA relacao\b", "A relação"),
    (r"\ba relacao\b", "a relação"),
    (r"\bprecisa de criterios\b", "precisa de critérios"),
    (r"\btolerancia\b", "tolerância"),
    (r"\bvariavel\b", "variável"),
    (r"\badministravel\b", "administrável"),
    (r"\bnegocio\b", "negócio"),
    (r"\beconomica\b", "econômica"),
    (r"\binutil\b", "inútil"),
    (r"\bpolitica\b", "política"),
    (r"\bacionaveis\b", "acionáveis"),
    (r"\bacionavel\b", "acionável"),
    (r"\bruidos\b", "ruídos"),
    (r"\bruido\b", "ruído"),
    (r"\bconsistencia\b", "consistência"),
    (r"\besforco\b", "esforço"),
    (r"\bTambem\b", "Também"),
    (r"\btambem\b", "também"),
    (r"\bintencao\b", "intenção"),
    (r"\bverificacoes\b", "verificações"),
    (r"\bautomaticos\b", "automáticos"),
    (r"\bpropria\b", "própria"),
    (r"\bhermeticas\b", "herméticas"),
    (r"\bimplantacao\b", "implantação"),
    (r"\bauditaveis\b", "auditáveis"),
    (r"\bverificavel\b", "verificável"),
    (r"\brepetivel\b", "repetível"),
    (r"\bescalavel\b", "escalável"),
    (r"\bfaceis\b", "fáceis"),
    (r"\bcodigo\b", "código"),
    (r"\bsuperficie\b", "superfície"),
    (r"\bcompreensiveis\b", "compreensíveis"),
    (r"\bdisposicao\b", "disposição"),
    (r"\bremocao\b", "remoção"),
    (r"\bminimas\b", "mínimas"),
    (r"\bexcecoes\b", "exceções"),
    (r"\brotulos\b", "rótulos"),
    (r"\bgeracao\b", "geração"),
    (r"\baplicacoes\b", "aplicações"),
    (r"\bprevisivel\b", "previsível"),
    (r"\bpapeis\b", "papéis"),
    (r"\bhistorico\b", "histórico"),
    (r"\bcoordenacao\b", "coordenação"),
    (r"\blideres\b", "líderes"),
    (r"\barea\b", "área"),
    (r"\bdelegacao\b", "delegação"),
    (r"\binstrucoes\b", "instruções"),
    (r"\binstrucao\b", "instrução"),
    (r"\bcondicoes\b", "condições"),
    (r"\bcontem\b", "contêm"),
    (r"\brastreaveis\b", "rastreáveis"),
    (r"\bmemoria\b", "memória"),
    (r"\breincidencia\b", "reincidência"),
    (r"\btendencias\b", "tendências"),
    (r"\bnecessario\b", "necessário"),
    (r"\bcenarios\b", "cenários"),
    (r"\badocao\b", "adoção"),
    (r"\bdinamicas\b", "dinâmicas"),
    (r"\bconstrui\b", "constrói"),
    (r"\breducao\b", "redução"),
    (r"\bapos\b", "após"),
    (r"\benderecos\b", "endereços"),
    (r"\bmilhoes\b", "milhões"),
    (r"\bconcentracao\b", "concentração"),
    (r"\bconexao\b", "conexão"),
    (r"\bsaude\b", "saúde"),
    (r"\butilizacao\b", "utilização"),
    (r"\bprevencao\b", "prevenção"),
    (r"\bdegradacao\b", "degradação"),
    (r"\beleicao\b", "eleição"),
    (r"\blider\b", "líder"),
    (r"\blocalizacao\b", "localização"),
    (r"\breplicas\b", "réplicas"),
    (r"\bidempotencia\b", "idempotência"),
    (r"\bexecucao\b", "execução"),
    (r"\bduplicada\b", "duplicada"),
    (r"\bestagios\b", "estágios"),
    (r"\bverificacao\b", "verificação"),
    (r"\brecuperaveis\b", "recuperáveis"),
    (r"\bLancamentos\b", "Lançamentos"),
    (r"\blancamentos\b", "lançamentos"),
    (r"\bfuncao\b", "função"),
    (r"\bTecnicas\b", "Técnicas"),
    (r"\btecnicas\b", "técnicas"),
    (r"\bbasicas\b", "básicas"),
    (r"\braciocinio\b", "raciocínio"),
    (r"\bestatistico\b", "estatístico"),
    (r"\bsimulacoes\b", "simulações"),
    (r"\bcontinuo\b", "contínuo"),
    (r"\bpressao\b", "pressão"),
    (r"\bfacam\b", "façam"),
    (r"\brelacao\b", "relação"),
    (r"\brevisao\b", "revisão"),
    (r"\bcriterios\b", "critérios"),
    (r"\bsaida\b", "saída"),
    (r"\bsaude\b", "saúde"),
    (r"\baviacao\b", "aviação"),
    (r"\badaptacao\b", "adaptação"),
    (r"\bpadroes\b", "padrões"),
    (r"\bunica\b", "única"),
    (r"\bja\b", "já"),
    (r"\btres\b", "três"),
    (r"\bprioritarias\b", "prioritárias"),
    (r"\bsaturacao\b", "saturação"),
    (r"\bdivergencias\b", "divergências"),
    (r"\bha necessidade\b", "há necessidade"),
    (r"\borganizacao so melhora\b", "organização só melhora"),
    (r"\bBackups so tem\b", "Backups só têm"),
    (r"\bbackups so tem\b", "backups só têm"),
    (r"\brecuperação e confiável\b", "recuperação é confiável"),
    (r"\bConfiabilidade e uma\b", "Confiabilidade é uma"),
    (r"\bconfiabilidade e uma\b", "confiabilidade é uma"),
    (r"\bToil e trabalho\b", "Toil é trabalho"),
    (r"\btoil e trabalho\b", "toil é trabalho"),
    (r"\bA mensagem prática e que\b", "A mensagem prática é que"),
    (r"\ba mensagem prática e que\b", "a mensagem prática é que"),
    (r"\bnão e propriedade\b", "não é propriedade"),
    (r"\bO ponto central e\b", "O ponto central é"),
    (r"\bo ponto central e\b", "o ponto central é"),
    (r"\bO objetivo não e\b", "O objetivo não é"),
    (r"\bo objetivo não e\b", "o objetivo não é"),
    (r"\bConsenso distribuído e necessário\b", "Consenso distribuído é necessário"),
    (r"\bconsenso distribuído e necessário\b", "consenso distribuído é necessário"),
    (r"\bplantão não e apenas\b", "plantão não é apenas"),
    (r"\bMonitoracao\b", "Monitoração"),
    (r"\bPlantao\b", "Plantão"),
    (r"\bsaudavel\b", "saudável"),
    (r"\bpsicologica\b", "psicológica"),
    (r"\brodizio\b", "rodízio"),
    (r"\bfacil\b", "fácil"),
    (r"\brejeicao\b", "rejeição"),
    (r"\bprotecao\b", "proteção"),
    (r"\bexplicitos\b", "explícitos"),
    (r"\blideranca\b", "liderança"),
    (r"\bmetodo\b", "método"),
    (r"\btestaveis\b", "testáveis"),
    (r"\bcritica\b", "crítica"),
    (r"\binvestigacao\b", "investigação"),
    (r"\bredundancia\b", "redundância"),
]


chapters = [
    {
        "number": 1,
        "part": "Parte I - Fundamentos e principios",
        "title": "Introducao",
        "central": "SRE e a aplicacao de engenharia de software ao trabalho historicamente tratado como operacoes.",
        "summary": "O capitulo apresenta a SRE como uma alternativa ao modelo classico de separacao entre desenvolvimento e operacoes. A ideia central e que servicos confiaveis em larga escala nao devem depender de trabalho manual crescente: SREs escrevem software, automatizam operacoes, reduzem intervencoes repetitivas e usam objetivos mensuraveis para equilibrar velocidade de mudanca e confiabilidade. O capitulo tambem introduz responsabilidades recorrentes de SRE: disponibilidade, latencia, desempenho, eficiencia, monitoracao, resposta a emergencias, gerenciamento de mudancas e planejamento de capacidade.",
        "concepts": ["SRE como engenharia de software aplicada a operacoes", "SLI, SLO e SLA", "toil e limite explicito para trabalho operacional", "error budget como mecanismo de equilibrio", "postmortems sem culpa", "automacao para reduzir dependencia humana"],
        "practice": ["Mapear tarefas operacionais repetitivas do seu ambiente.", "Definir um SLI simples para um fluxo critico.", "Transformar uma meta de confiabilidade em SLO inicial.", "Identificar quais decisoes de release hoje sao subjetivas e poderiam usar SLOs.", "Definir uma primeira lista de responsabilidades de confiabilidade para um servico real."],
    },
    {
        "number": 2,
        "part": "Parte I - Fundamentos e principios",
        "title": "O ambiente de producao do Google do ponto de vista de um SRE",
        "central": "A confiabilidade depende de entender o ecossistema de producao, nao apenas uma aplicacao isolada.",
        "summary": "O capitulo contextualiza o ambiente de producao do Google: hardware, sistemas de cluster, armazenamento, rede, servicos de lock, monitoracao, alertas e ferramentas de desenvolvimento. Em vez de tratar um servico como uma caixa isolada, o texto mostra como as camadas de infraestrutura, orquestracao e desenvolvimento influenciam a confiabilidade. O exemplo de um servico ilustra o caminho de uma requisicao e ajuda a relacionar conceitos de arquitetura com operacao diaria.",
        "concepts": ["datacenters e clusters como plataforma", "orquestracao de maquinas e jobs", "armazenamento e rede como dependencias criticas", "monitoracao integrada ao ambiente", "vida de uma requisicao"],
        "practice": ["Desenhar o caminho de uma requisicao em um sistema conhecido.", "Listar dependencias internas e externas que afetam disponibilidade.", "Separar riscos de aplicacao, infraestrutura, rede e dados."],
    },
    {
        "number": 3,
        "part": "Parte I - Fundamentos e principios",
        "title": "Aceitando os riscos",
        "central": "Confiabilidade e uma decisao economica e de produto, nao uma busca cega por 100%.",
        "summary": "O capitulo argumenta que eliminar todo risco e caro, lento e muitas vezes inutil para o usuario. SRE transforma risco em uma variavel administravel: mede falhas, entende tolerancia do produto e traduz disponibilidade desejada em uma provisao para erros. Essa provisao permite que as equipes gastem risco de modo consciente, acelerando mudancas enquanto permanecem dentro de limites aceitos pelo negocio.",
        "concepts": ["risco administrado", "tolerancia a falhas", "provisao para erros", "disponibilidade como decisao de produto", "trade-off entre confiabilidade e velocidade"],
        "practice": ["Escolher um servico e discutir qual nivel de disponibilidade realmente importa.", "Estimar impacto de falhas parciais versus falha total.", "Criar um rascunho de error budget mensal ou trimestral."],
    },
    {
        "number": 4,
        "part": "Parte I - Fundamentos e principios",
        "title": "Objetivos do nivel de servico",
        "central": "SLIs, SLOs e SLAs transformam confiabilidade em linguagem mensuravel e compartilhada.",
        "summary": "O capitulo define indicadores, objetivos e acordos de nivel de servico. SLIs medem aspectos do comportamento percebido pelo usuario; SLOs definem metas internas ou externas; SLAs acrescentam consequencias contratuais. A mensagem pratica e que boas metricas devem refletir o que os usuarios valorizam, ser coletadas de forma consistente e orientar decisoes operacionais, tecnicas e de produto.",
        "concepts": ["SLI", "SLO", "SLA", "agregacao e janelas de medicao", "expectativas explicitas de servico"],
        "practice": ["Definir 3 SLIs para uma API ou aplicacao.", "Escolher janelas de avaliacao para disponibilidade e latencia.", "Documentar uma politica de acao quando o SLO estiver em risco."],
    },
    {
        "number": 5,
        "part": "Parte I - Fundamentos e principios",
        "title": "Eliminando tarefas penosas",
        "central": "Toil e trabalho manual, repetitivo, reativo e escalavel linearmente com o servico; deve ser reduzido por engenharia.",
        "summary": "O capitulo define tarefas penosas como atividades operacionais que nao geram valor duravel, exigem intervencao humana e crescem com o tamanho do sistema. Nem todo trabalho operacional e ruim, mas toil excessivo rouba tempo de engenharia e impede evolucao. A pratica de SRE exige medir, limitar e substituir esse trabalho por automacao, ferramentas ou mudancas de design.",
        "concepts": ["toil", "trabalho operacional versus engenharia", "crescimento linear de carga manual", "limite de carga operacional", "automacao como investimento"],
        "practice": ["Classificar tickets recentes como toil ou engenharia.", "Calcular horas mensais gastas em tarefas repetitivas.", "Escolher uma tarefa de alto volume para automatizar primeiro."],
    },
    {
        "number": 6,
        "part": "Parte I - Fundamentos e principios",
        "title": "Monitorando sistemas distribuidos",
        "central": "Monitoracao deve alertar sobre sintomas relevantes para usuarios e apoiar diagnostico sem criar ruido.",
        "summary": "O capitulo separa causas de sintomas, monitoracao caixa-preta de caixa-branca e apresenta os quatro sinais de ouro: latencia, trafego, erros e saturacao. Um bom sistema de monitoracao deve acionar pessoas apenas quando ha necessidade de julgamento humano imediato. O restante deve virar dashboard, ticket, log ou automacao, reduzindo fadiga de alerta.",
        "concepts": ["sintomas versus causas", "caixa-preta e caixa-branca", "quatro sinais de ouro", "alertas acionaveis", "cauda de latencia"],
        "practice": ["Revisar alertas e remover os que nao exigem acao imediata.", "Criar um painel com latencia, trafego, erros e saturacao.", "Distinguir metricas de usuario de metricas internas."],
    },
    {
        "number": 7,
        "part": "Parte I - Fundamentos e principios",
        "title": "A evolucao da automacao no Google",
        "central": "Automacao confiavel evolui de scripts pontuais para plataformas que expressam intencao e corrigem estado.",
        "summary": "O capitulo mostra por que automacao e essencial: melhora consistencia, reduz tempo de resposta, economiza esforco e permite operar em escala. Tambem alerta que automacao superficial pode apenas congelar processos ruins. O objetivo mais maduro e construir sistemas que conhecem o estado desejado, detectam divergencias e aplicam correcoes idempotentes com confiabilidade.",
        "concepts": ["automacao idempotente", "estado desejado", "plataformas operacionais", "consistencia", "sistemas automaticos versus apenas automatizados"],
        "practice": ["Identificar automacoes frageis baseadas em passos manuais codificados.", "Descrever o estado desejado de um recurso de producao.", "Adicionar verificacoes antes e depois de uma rotina automatizada."],
    },
    {
        "number": 8,
        "part": "Parte I - Fundamentos e principios",
        "title": "Engenharia de release",
        "central": "Releases confiaveis exigem builds reproduziveis, politicas claras, automacao e separacao entre construir e implantar.",
        "summary": "O capitulo trata release engineering como disciplina propria. Builds hermeticas, empacotamento, testes, branching, implantacao continua e gerenciamento de configuracao reduzem risco e tornam mudancas auditaveis. A mensagem e que release nao deve depender de heroismo: o caminho para producao precisa ser padronizado, rapido, verificavel e repetivel.",
        "concepts": ["build hermetica", "implantacao continua", "branching", "empacotamento", "gerenciamento de configuracao"],
        "practice": ["Documentar o pipeline atual de build e deploy.", "Identificar entradas nao controladas que prejudicam reproducibilidade.", "Definir criterios minimos para promover uma versao."],
    },
    {
        "number": 9,
        "part": "Parte I - Fundamentos e principios",
        "title": "Simplicidade",
        "central": "Sistemas mais simples sao mais faceis de operar, entender, alterar e recuperar.",
        "summary": "O capitulo defende simplicidade como requisito de confiabilidade. Cada linha de codigo, feature, API ou dependencia acrescenta custo operacional e superficie de falha. A simplicidade nao significa imobilismo; significa preservar interfaces pequenas, modularidade, releases compreensiveis e disposicao para remover codigo que nao paga seu custo.",
        "concepts": ["estabilidade versus agilidade", "linhas de codigo negativas", "APIs minimas", "modularidade", "simplicidade em releases"],
        "practice": ["Listar features pouco usadas que aumentam complexidade.", "Propor uma remocao segura de codigo ou configuracao.", "Revisar uma API buscando reduzir estados e excecoes."],
    },
    {
        "number": 10,
        "part": "Parte II - Praticas",
        "title": "Alertas praticos a partir de dados de series temporais",
        "central": "Alertas devem ser derivados de series temporais bem modeladas e regras que representem impacto operacional real.",
        "summary": "O capitulo usa a evolucao do Borgmon para explicar coleta, rotulos, vetores, regras, armazenamento e geracao de alertas. O foco e transformar dados exportados por aplicacoes em sinais confiaveis para operacao. A qualidade da configuracao importa tanto quanto a coleta: alertas ruins geram fadiga, enquanto regras bem desenhadas permitem resposta rapida e previsivel.",
        "concepts": ["series temporais", "rotulos e vetores", "avaliacao de regras", "alertas caixa-preta", "configuracao de monitoracao"],
        "practice": ["Padronizar nomes e rotulos de metricas.", "Separar alertas de pagina de alertas por ticket.", "Criar uma regra baseada em taxa ou janela, nao apenas em valor instantaneo."],
    },
    {
        "number": 11,
        "part": "Parte II - Praticas",
        "title": "De plantao",
        "central": "Plantao saudavel equilibra carga, qualidade dos eventos, seguranca psicologica e aprendizado.",
        "summary": "O capitulo descreve como organizar rodizios de plantao sustentaveis. Um bom plantao nao e apenas escala de pessoas: exige volume manejavel de alertas, documentacao, treinamento, remuneracao ou reconhecimento, seguranca para tomar decisoes e mecanismos para evitar tanto sobrecarga quanto falta de pratica operacional.",
        "concepts": ["rodizio de plantao", "carga operacional", "qualidade dos alertas", "seguranca para responder incidentes", "equilibrio de volume"],
        "practice": ["Medir numero de paginas por turno.", "Revisar runbooks dos alertas mais frequentes.", "Definir criterio de prontidao para entrar no plantao."],
    },
    {
        "number": 12,
        "part": "Parte II - Praticas",
        "title": "Resolvendo problemas de modo eficiente",
        "central": "Troubleshooting eficaz combina metodo, hipoteses testaveis e aprendizado com resultados negativos.",
        "summary": "O capitulo apresenta uma abordagem disciplinada para investigar falhas: entender o relato, triar, analisar, diagnosticar, testar e tratar. A pratica valoriza evidencias, experimentos pequenos e a eliminacao de hipoteses. Resultados negativos sao uteis porque reduzem o espaco de busca e evitam mudancas aleatorias em producao.",
        "concepts": ["triagem", "hipoteses", "diagnostico", "experimentos controlados", "resultados negativos"],
        "practice": ["Registrar hipoteses antes de executar correcoes.", "Separar mitigacao imediata de correcao definitiva.", "Manter linha do tempo durante uma investigacao."],
    },
    {
        "number": 13,
        "part": "Parte II - Praticas",
        "title": "Resposta a emergencias",
        "central": "Equipes respondem melhor a emergencias quando treinam, documentam e aprendem antes da crise real.",
        "summary": "O capitulo discute falhas induzidas por testes, mudancas e processos, enfatizando que emergencias devem gerar aprendizado pratico. Resposta eficiente combina calma, papeis claros, historico de interrupcoes, perguntas do tipo 'e se?' e testes proativos. O objetivo nao e evitar todo problema, mas reduzir surpresa e melhorar recuperacao.",
        "concepts": ["resposta a emergencia", "treinamento proativo", "historico de interrupcoes", "testes de falha", "preparacao operacional"],
        "practice": ["Executar um exercicio de simulacao de incidente.", "Criar uma lista de cenarios 'e se?'.", "Transformar incidentes passados em testes ou alertas."],
    },
    {
        "number": 14,
        "part": "Parte II - Praticas",
        "title": "Administrando incidentes",
        "central": "Incidentes precisam de coordenacao explicita, comunicacao clara e separacao de responsabilidades.",
        "summary": "O capitulo mostra como incidentes ficam piores quando todos atacam o problema tecnico sem coordenacao. Um processo eficaz define comandante do incidente, lideres por area, comunicacao centralizada, documento vivo de estado e passagem clara de responsabilidade. A estrutura reduz caos e acelera a volta ao funcionamento normal.",
        "concepts": ["comando de incidente", "comunicacao durante crise", "documento vivo", "delegacao de papeis", "handoff"],
        "practice": ["Definir papeis padrao para incidentes severos.", "Criar um template de documento de incidente.", "Estabelecer quando declarar incidente formal."],
    },
    {
        "number": 15,
        "part": "Parte II - Praticas",
        "title": "Cultura de postmortem: aprendendo com o fracasso",
        "central": "Postmortems sem culpa transformam falhas em melhorias sistemicas.",
        "summary": "O capitulo descreve a filosofia de analisar incidentes sem buscar culpados. O foco e entender condicoes, decisoes, lacunas tecnicas e fatores organizacionais que permitiram a falha. Bons postmortems sao compartilhados, contem acoes rastreaveis e constroem memoria operacional para reduzir reincidencia.",
        "concepts": ["postmortem sem culpa", "causas sistemicas", "acoes corretivas", "compartilhamento de conhecimento", "melhoria continua"],
        "practice": ["Criar um template de postmortem.", "Revisar se acoes corretivas tem dono e prazo.", "Compartilhar aprendizados fora da equipe diretamente afetada."],
    },
    {
        "number": 16,
        "part": "Parte II - Praticas",
        "title": "Monitorando interrupcoes de servico",
        "central": "Medir interrupcoes ao longo do tempo cria base objetiva para melhorar confiabilidade.",
        "summary": "O capitulo apresenta mecanismos para registrar, agregar, rotular e analisar interrupcoes. A ideia e que uma organizacao so melhora confiabilidade de forma deliberada quando conhece sua linha de base e consegue acompanhar tendencias. Classificar interrupcoes tambem revela causas recorrentes e prioridades de engenharia.",
        "concepts": ["registro de interrupcoes", "agregacao", "rotulagem", "analise de tendencias", "linha de base"],
        "practice": ["Montar catalogo de incidentes dos ultimos meses.", "Classificar interrupcoes por causa e impacto.", "Criar indicador mensal de confiabilidade percebida."],
    },
    {
        "number": 17,
        "part": "Parte II - Praticas",
        "title": "Testes voltados a confiabilidade",
        "central": "Confiabilidade precisa ser testada em build, integracao, producao controlada e cenarios de desastre.",
        "summary": "O capitulo amplia a visao de testes alem dos testes tradicionais de software. Em sistemas distribuidos, e necessario validar comportamento sob falhas, rollouts, integracao, carga e recuperacao. Testar em escala exige ambientes, ferramentas e sondas que aproximem o sistema das condicoes reais de producao.",
        "concepts": ["testes tradicionais", "testes em producao", "testes de desastre", "sondas", "falha esperada em testes"],
        "practice": ["Adicionar testes de comportamento sob dependencia indisponivel.", "Planejar um teste de rollback.", "Criar uma sonda de producao para fluxo critico."],
    },
    {
        "number": 18,
        "part": "Parte II - Praticas",
        "title": "Engenharia de software em SRE",
        "central": "SRE tambem construi sistemas de software para resolver problemas operacionais estruturais.",
        "summary": "O capitulo usa um estudo de caso de planejamento de capacidade baseado em intencao para mostrar SRE como engenharia de software, nao apenas operacao. A equipe identifica um problema recorrente, modela requisitos, construi ferramenta, promove adocao e aprende com dinamicas organizacionais. O ponto central e reservar tempo e cultura para projetos de engenharia dentro de SRE.",
        "concepts": ["planejamento baseado em intencao", "ferramentas internas", "adocao organizacional", "tempo para desenvolvimento", "cultura de engenharia"],
        "practice": ["Escolher um problema operacional que mereca produto interno.", "Definir usuarios e requisitos de uma ferramenta de SRE.", "Medir adocao e reducao de carga apos entrega."],
    },
    {
        "number": 19,
        "part": "Parte II - Praticas",
        "title": "Distribuicao de carga no frontend",
        "central": "Balanceamento global precisa direcionar usuarios a pontos de entrada saudaveis e proximos sem depender apenas de capacidade bruta.",
        "summary": "O capitulo aborda distribuicao de trafego na borda usando mecanismos como DNS e enderecos IP virtuais. A meta e absorver milhoes de requisicoes com resiliencia, reduzindo latencia e evitando concentracao de carga. O desenho do frontend influencia tanto experiencia do usuario quanto capacidade de reagir a falhas regionais.",
        "concepts": ["balanceamento por DNS", "VIP", "roteamento global", "proximidade", "capacidade de entrada"],
        "practice": ["Mapear como usuarios chegam ao servico.", "Identificar pontos unicos de entrada.", "Definir comportamento esperado quando uma regiao falha."],
    },
    {
        "number": 20,
        "part": "Parte II - Praticas",
        "title": "Distribuicao de carga no datacenter",
        "central": "Dentro do datacenter, balanceamento precisa considerar saude, subconjuntos e politicas de escolha de backend.",
        "summary": "O capitulo discute algoritmos de distribuicao de carga para tarefas em um datacenter. Alem de round robin, sistemas reais precisam detectar tarefas ruins, limitar pools de conexao e escolher subconjuntos de backends para reduzir custo e aumentar estabilidade. Politicas de distribuicao devem reagir a carga, saude e topologia.",
        "concepts": ["controle de fluxo", "estado de incapacidade", "subconjuntos", "round robin ponderado", "least-loaded"],
        "practice": ["Verificar como clientes escolhem instancias de backend.", "Adicionar sinais de saude ao balanceamento.", "Avaliar se pools de conexao estao excessivamente amplos."],
    },
    {
        "number": 21,
        "part": "Parte II - Praticas",
        "title": "Tratando sobrecarga",
        "central": "Sobrecarga deve ser controlada com limites, throttling, prioridades e respostas explicitas.",
        "summary": "O capitulo mostra que queries por segundo nao bastam para entender capacidade: custo por requisicao, cliente, criticidade e utilizacao importam. Sistemas robustos impõem limites por cliente, fazem throttling do lado cliente, distinguem trafego critico e respondem corretamente a erros de sobrecarga. O objetivo e degradar de forma controlada em vez de colapsar.",
        "concepts": ["limites por cliente", "throttling", "criticidade", "sinais de utilizacao", "erros de sobrecarga"],
        "practice": ["Classificar tipos de trafego por criticidade.", "Definir resposta padrao para overload.", "Revisar politicas de retry para evitar amplificacao."],
    },
    {
        "number": 22,
        "part": "Parte II - Praticas",
        "title": "Tratando falhas em cascata",
        "central": "Falhas em cascata surgem quando respostas locais a falhas amplificam carga e derrubam dependencias.",
        "summary": "O capitulo explica causas comuns de cascata: sobrecarga, esgotamento de recursos, indisponibilidade de servicos, retentativas agressivas, filas mal geridas e caches frios. A prevencao passa por backoff com jitter, limites, rejeicao de carga, degradacao elegante, timeouts e testes que levem sistemas alem do ponto de falha para revelar comportamento real.",
        "concepts": ["falha em cascata", "backoff exponencial", "jitter", "degradacao elegante", "gerenciamento de filas"],
        "practice": ["Revisar retentativas entre servicos.", "Adicionar timeouts coerentes com SLO.", "Testar dependencia lenta ou indisponivel em ambiente controlado."],
    },
    {
        "number": 23,
        "part": "Parte II - Praticas",
        "title": "Administrando estados criticos: consenso distribuido para confiabilidade",
        "central": "Estado critico em sistemas distribuidos exige consenso para evitar split-brain e decisoes conflitantes.",
        "summary": "O capitulo explica por que consenso distribuido e necessario para locks, eleicao de lider, configuracoes, filas confiaveis e maquinas de estado replicadas. Protocolos como Paxos permitem coordenar decisoes apesar de falhas, mas trazem custo de latencia, quorum, localizacao de replicas e monitoracao cuidadosa. A confiabilidade do estado depende tanto do algoritmo quanto da implantacao.",
        "concepts": ["consenso distribuido", "Paxos", "quorum", "eleicao de lider", "split-brain"],
        "practice": ["Identificar estados que nao podem divergir.", "Documentar quorum e localizacao de replicas.", "Monitorar latencia e saude de sistemas de consenso."],
    },
    {
        "number": 24,
        "part": "Parte II - Praticas",
        "title": "Escalonamento periodico e distribuido com o cron",
        "central": "Agendamento distribuido confiavel precisa lidar com estado, lideranca, idempotencia e escala.",
        "summary": "O capitulo usa cron distribuido para mostrar que uma ferramenta simples se torna complexa em escala. Jobs periodicos precisam de idempotencia, monitoracao de estado, coordenacao por consenso, papeis de lider e seguidor, armazenamento confiavel e protecao contra execucao duplicada ou perdida. A confiabilidade vem de tornar explicitos os estados do job.",
        "concepts": ["cron distribuido", "idempotencia", "lider e seguidor", "estado de job", "Paxos aplicado"],
        "practice": ["Listar jobs periodicos criticos.", "Garantir que jobs possam ser repetidos sem dano.", "Adicionar monitoracao para atraso, falha e duplicidade."],
    },
    {
        "number": 25,
        "part": "Parte II - Praticas",
        "title": "Pipelines de processamento de dados",
        "central": "Pipelines confiaveis precisam coordenar estagios, carga irregular, continuidade e verificacao de corretude.",
        "summary": "O capitulo examina pipelines periodicos e distribuidos, incluindo problemas de thundering herd, padroes de carga e monitoracao insuficiente. Ao tratar workflow como um modelo com estado e etapas explicitas, fica mais facil controlar execucao, detectar atrasos, validar resultados e preservar continuidade do negocio mesmo com falhas parciais.",
        "concepts": ["pipeline periodico", "thundering herd", "workflow", "estagios de execucao", "continuidade de negocio"],
        "practice": ["Desenhar estagios e dependencias de um pipeline.", "Identificar horarios de pico causados por agendamento.", "Criar verificacoes de completude e corretude dos dados."],
    },
    {
        "number": 26,
        "part": "Parte II - Praticas",
        "title": "Integridade de dados: o que voce le e o que voce escreveu",
        "central": "Backups so tem valor quando a recuperacao e confiavel, testada e alinhada a integridade percebida pelo usuario.",
        "summary": "O capitulo diferencia backup, arquivamento, replicacao, deteccao precoce e recuperacao. A prioridade e preservar disponibilidade por meio de integridade de dados verificavel. Estrategias robustas combinam defesa em profundidade, remocao soft, backups recuperaveis, replicacao, testes de restauracao e atitude de 'confiar, mas verificar'.",
        "concepts": ["integridade de dados", "backup versus arquivamento", "recuperacao", "replicacao", "defesa em profundidade"],
        "practice": ["Testar restauracao de um backup real.", "Definir RPO e RTO para dados criticos.", "Adicionar deteccao de exclusao ou corrupcao silenciosa."],
    },
    {
        "number": 27,
        "part": "Parte II - Praticas",
        "title": "Lancamento de produtos confiaveis em escala",
        "central": "Lancamentos confiaveis exigem coordenacao, checklists, rollouts graduais e analise de modos de falha.",
        "summary": "O capitulo apresenta Launch Coordination Engineering como funcao que ajuda produtos a chegar a producao com confiabilidade. Checklists de arquitetura, dependencias, integracao, capacidade, modos de falha, comportamento de clientes, automacao e rollout reduzem surpresa. Tecnicas como flags e lancamentos em fases permitem aprender com risco limitado.",
        "concepts": ["Launch Coordination Engineering", "checklist de lancamento", "rollout gradual", "feature flags", "planejamento de capacidade"],
        "practice": ["Criar checklist de lancamento para um servico.", "Planejar fases e criterios de rollback.", "Incluir modos de falha e abusos de clientes no plano."],
    },
    {
        "number": 28,
        "part": "Parte III - Gerenciamento",
        "title": "Acelerando os SREs para chegar ao plantao e alem",
        "central": "Formar SREs exige trilhas de aprendizado, pratica supervisionada e exposicao progressiva a sistemas reais.",
        "summary": "O capitulo trata onboarding e desenvolvimento continuo de SREs. Novos membros precisam aprender arquitetura, engenharia reversa, raciocinio estatistico, improviso controlado, leitura de postmortems, simulacoes e acompanhamento de plantao. A meta e formar autonomia operacional sem depender de aprendizado acidental durante crises.",
        "concepts": ["onboarding de SRE", "engenharia reversa", "raciocinio estatistico", "simulacoes de desastre", "aprendizado continuo"],
        "practice": ["Criar trilha de 30/60/90 dias para SRE.", "Usar postmortems como material de treinamento.", "Planejar shadowing antes do plantao independente."],
    },
    {
        "number": 29,
        "part": "Parte III - Gerenciamento",
        "title": "Lidando com interrupcoes",
        "central": "Interrupcoes cognitivas reduzem qualidade; processos devem proteger foco e orientar a acao.",
        "summary": "O capitulo discute carga operacional sob a perspectiva humana. Sistemas complexos geram interrupcoes, mudancas de contexto e decisoes sob pressao. Equipes melhores reduzem ruido, fornecem instrucoes claras, preservam fluxo cognitivo e projetam processos para que pessoas facam a tarefa certa no momento certo.",
        "concepts": ["carga operacional", "interrupcoes", "fluxo cognitivo", "instrucao acionavel", "reducao de ruido"],
        "practice": ["Medir fontes de interrupcao da equipe.", "Separar canais urgentes de canais informativos.", "Criar instrucoes claras para alertas criticos."],
    },
    {
        "number": 30,
        "part": "Parte III - Gerenciamento",
        "title": "Incluindo um SRE para se recuperar de uma sobrecarga operacional",
        "central": "Recuperar uma equipe sobrecarregada exige entender contexto, compartilhar diagnostico e conduzir mudancas basicas primeiro.",
        "summary": "O capitulo descreve como um SRE pode ajudar um servico em crise operacional. O processo comeca por conhecer o servico, identificar fontes de estresse, documentar o contexto e classificar problemas. Depois, a equipe ataca fundamentos: monitoracao, runbooks, bugs recorrentes, automacao e comunicacao do raciocinio para conquistar alinhamento.",
        "concepts": ["sobrecarga operacional", "diagnostico de estresse", "contexto compartilhado", "mudancas basicas", "priorizacao"],
        "practice": ["Mapear principais causas de estresse operacional.", "Escrever diagnostico compartilhado para a equipe.", "Priorizar correcoes simples que reduzem alertas ou tickets."],
    },
    {
        "number": 31,
        "part": "Parte III - Gerenciamento",
        "title": "Comunicacao e colaboracao em SRE",
        "central": "SRE depende de comunicacao estruturada entre equipes com objetivos, incentivos e contextos diferentes.",
        "summary": "O capitulo aborda reunioes de producao, composicao de equipes e tecnicas de colaboracao. Como SRE fica entre produto, infraestrutura e operacao, precisa criar foruns, agendas, documentos e relacoes que mantenham todos alinhados. Comunicacao eficaz reduz ambiguidades e permite decisoes tecnicas mais rapidas.",
        "concepts": ["reunioes de producao", "colaboracao entre equipes", "agenda operacional", "composicao de equipe", "alinhamento"],
        "practice": ["Definir pauta fixa para reuniao de producao.", "Registrar decisoes e pendencias operacionais.", "Criar canal claro para negociacao de SLO e prioridades."],
    },
    {
        "number": 32,
        "part": "Parte III - Gerenciamento",
        "title": "O modelo de engajamento da SRE em evolucao",
        "central": "O relacionamento entre SRE e equipes de produto precisa de criterios claros de entrada, saida e responsabilidade.",
        "summary": "O capitulo discute como SRE decide quando se engajar com um servico e como esse modelo evolui. A relacao deve deixar explicitos requisitos de confiabilidade, maturidade operacional, responsabilidades, limites e mecanismos de revisao. Isso evita que SRE vire uma fila de suporte e preserva foco em engenharia de impacto.",
        "concepts": ["modelo de engajamento", "criterios de entrada", "responsabilidade compartilhada", "maturidade operacional", "revisao de servico"],
        "practice": ["Definir criterios para SRE aceitar um servico.", "Criar checklist de prontidao operacional.", "Estabelecer revisoes periodicas de engajamento."],
    },
    {
        "number": 33,
        "part": "Parte III - Gerenciamento",
        "title": "Licoes aprendidas com outros mercados",
        "central": "Setores como saude, aviacao e energia mostram praticas de seguranca que inspiram confiabilidade em software.",
        "summary": "O capitulo compara SRE com mercados que lidam com risco, seguranca e operacao critica. A confiabilidade em software pode aprender com checklists, cultura de reporte, investigacao sem culpa, treinamento, redundancia e padroes. A diferenca e que software muda muito rapido, portanto precisa adaptar essas praticas a ciclos curtos e sistemas distribuidos.",
        "concepts": ["aprendizado intersetorial", "seguranca operacional", "checklists", "cultura de reporte", "adaptacao a software"],
        "practice": ["Comparar um processo interno com praticas de setores regulados.", "Introduzir checklist em uma operacao critica.", "Incentivar reporte de quase-incidentes."],
    },
    {
        "number": 34,
        "part": "Parte III - Gerenciamento",
        "title": "Conclusao",
        "central": "SRE e uma disciplina pratica que combina engenharia, operacao, produto e cultura para construir servicos confiaveis.",
        "summary": "O capitulo final reforca que SRE nasceu de necessidades reais de operar servicos em escala e amadureceu como conjunto de principios, praticas e modelos organizacionais. A confiabilidade nao e propriedade de uma unica equipe: ela emerge de escolhas de arquitetura, automacao, lancamento, resposta a incidentes, aprendizado e comunicacao.",
        "concepts": ["SRE como disciplina", "confiabilidade como responsabilidade compartilhada", "aprendizado continuo", "engenharia aplicada a operacao", "escala"],
        "practice": ["Revisar quais praticas do curso ja existem na organizacao.", "Escolher tres lacunas prioritarias de confiabilidade.", "Montar um plano de melhoria incremental."],
    },
]


def slug(number: int) -> str:
    return f"capitulo-{number:02d}.md"


DISPLAY_SEQUENCE = [
    1,
    3,
    5,
    6,
    7,
    9,
    10,
    12,
    13,
    16,
    17,
    18,
    19,
    21,
    23,
    24,
    26,
    27,
    *range(28, 35),
]
PART_NAV = {
    "Parte I - Fundamentos e princípios": [1, 3, 5, 6, 7, 9],
    "Parte II - Práticas": [10, 12, 13, 16, 17, 18, 19, 21, 23, 24, 26, 27],
    "Parte III - Gerenciamento": list(range(28, 35)),
}


def display_number(chapter_number: int) -> int | None:
    if chapter_number == 2:
        return None
    if chapter_number == 4:
        chapter_number = 3
    if chapter_number == 8:
        chapter_number = 7
    if chapter_number == 11:
        chapter_number = 10
    if chapter_number in {14, 15}:
        chapter_number = 13
    if chapter_number == 20:
        chapter_number = 19
    if chapter_number == 22:
        chapter_number = 21
    if chapter_number == 25:
        chapter_number = 24
    if chapter_number not in DISPLAY_SEQUENCE:
        return None
    return DISPLAY_SEQUENCE.index(chapter_number) + 1


def display_slug(chapter_number: int) -> str:
    number = display_number(chapter_number)
    if number is None:
        raise ValueError("The original chapter 02 was consolidated into chapter 01.")
    return slug(number)


def display_title(chapter: dict) -> str:
    if chapter["number"] == 1:
        return "Introdução à SRE e ao ambiente de produção"
    if chapter["number"] in {3, 4}:
        return "Risco, objetivos de serviço e error budget"
    if chapter["number"] in {7, 8}:
        return "Automação operacional e engenharia de release"
    if chapter["number"] in {10, 11}:
        return "Alertas acionáveis e plantão saudável"
    if chapter["number"] in {13, 14, 15}:
        return "Resposta a incidentes e aprendizado operacional"
    if chapter["number"] in {19, 20}:
        return "Distribuição de carga na borda e no datacenter"
    if chapter["number"] in {21, 22}:
        return "Sobrecarga, retentativas e falhas em cascata"
    if chapter["number"] in {24, 25}:
        return "Agendamento distribuído e pipelines confiáveis"
    return normalize_pt_br(chapter["title"])


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def table(rows: list[tuple[str, str]]) -> str:
    body = "\n".join(f"| {left} | {right} |" for left, right in rows)
    return f"| Item | Aplicação |\n| --- | --- |\n{body}"


def next_chapter(chapter: dict) -> str:
    number = chapter["number"]
    if number not in DISPLAY_SEQUENCE:
        raise ValueError(f"Chapter {number} is not a display representative.")
    index = DISPLAY_SEQUENCE.index(number)
    if index == len(DISPLAY_SEQUENCE) - 1:
        return "Este é o capítulo final. Revise os conceitos centrais e transforme os exercícios em um plano de melhoria para um serviço real."
    next_number = DISPLAY_SEQUENCE[index + 1]
    nxt = chapters[next_number - 1]
    visible_number = display_number(nxt["number"])
    return f"Próximo: [Capítulo {visible_number:02d} - {display_title(nxt)}]({display_slug(nxt['number'])})."


def mental_model(chapter: dict) -> str:
    concept_text = " ".join(chapter["concepts"]).lower()
    if chapter["number"] == 1 or "sre" in concept_text:
        return "SRE é uma ponte entre engenharia de software e operação: em vez de atravessar carregando trabalho manual, a equipe constrói uma passagem mais segura para todos usarem."
    if "slo" in concept_text or "sli" in concept_text:
        return "SLI é como um termômetro: ele não cura o paciente, mas mostra se algo importante mudou. SLO é a temperatura-alvo que define quando agir."
    if "toil" in concept_text or "tarefa" in concept_text:
        return "Toil é dívida operacional: quanto mais você ignora, mais juros a equipe paga em trabalho repetitivo."
    if "postmortem" in concept_text:
        return "Postmortem é investigação de acidente: o objetivo é entender o sistema, não encontrar um culpado conveniente."
    if "consenso" in concept_text:
        return "Consenso distribuído é uma votação com regras rígidas para evitar que partes diferentes do sistema tomem decisões incompatíveis."
    if "integridade" in concept_text or "backup" in concept_text:
        return "Integridade de dados é recibo e cofre ao mesmo tempo: você precisa provar o que aconteceu e conseguir recuperar o que importa."
    return f"Pense em **{chapter['concepts'][0]}** como uma alavanca de confiabilidade: ela transforma um problema operacional recorrente em uma decisão explícita de engenharia."


def industry_rows(chapter: dict) -> list[tuple[str, str]]:
    title = chapter["title"].lower()
    rows = [
        ("Kubernetes", "Executar serviços, configurar probes, controlar rollouts e isolar recursos."),
        ("OpenTelemetry", "Coletar traces, métricas e logs com instrumentação padronizada."),
        ("Prometheus", "Coletar séries temporais e avaliar regras de alerta."),
        ("Grafana", "Construir dashboards para análise operacional."),
        ("GitOps", "Versionar mudanças operacionais e tornar deploys auditáveis."),
    ]
    if any(word in title for word in ["incidente", "emerg", "plantao", "postmortem"]):
        rows.extend([
            ("PagerDuty ou Opsgenie", "Organizar escalas, acionamentos e escalonamentos."),
            ("Statuspage", "Comunicar impacto para usuários e stakeholders."),
        ])
    if any(word in title for word in ["release", "lancamento"]):
        rows.extend([
            ("Argo CD ou Flux", "Aplicar GitOps em rollouts e reconciliação de estado."),
            ("Feature flags", "Liberar mudanças gradualmente e reduzir risco de lançamento."),
        ])
    if any(word in title for word in ["dados", "pipeline", "cron"]):
        rows.extend([
            ("Airflow ou Workflows", "Orquestrar tarefas, dependências e reexecuções."),
            ("Object storage", "Guardar artefatos e dados de recuperação."),
        ])
    return rows


def modern_evolution() -> str:
    return (
        "Depois de 2016, a prática de SRE passou a conviver mais diretamente com Kubernetes, "
        "serviços gerenciados de nuvem, GitOps, OpenTelemetry, service meshes e plataformas "
        "internas de engenharia. O princípio não mudou: confiabilidade continua sendo tratada "
        "com objetivos mensuráveis, automação e aprendizado. O que mudou foi o ambiente: hoje "
        "muitas decisões operacionais são expressas em configuração declarativa, pipelines, "
        "políticas de plataforma e telemetria padronizada. Em sistemas com IA, o mesmo raciocínio "
        "também precisa considerar qualidade de dados, degradação de modelo, custo de inferência "
        "e comportamento não determinístico."
    )


def eli15(chapter: dict) -> str:
    return (
        f"Imagine que você cuida de um serviço usado por outras pessoas todos os dias. "
        f"O capítulo ensina a olhar para **{chapter['title']}** como uma forma de evitar "
        f"surpresas ruins. Em vez de esperar quebrar e correr para consertar, você mede o que "
        f"importa, combina limites, treina respostas e melhora o sistema aos poucos. A ideia "
        f"não é deixar tudo perfeito. É saber o que pode falhar, quanto risco é aceitável e "
        f"como recuperar rápido quando algo der errado."
    )


def normalize_pt_br(text: str) -> str:
    for pattern, replacement in PT_BR_REPLACEMENTS:
        text = re.sub(pattern, replacement, text)
    return text


def student_facing_summary(chapter: dict) -> str:
    text = chapter["summary"].strip()
    replacements = [
        (r"^O capitulo mostra como ", ""),
        (r"^O capitulo discute como ", ""),
        (r"^O capitulo descreve como ", ""),
        (r"^O capitulo explica por que ", ""),
        (r"^O capitulo mostra por que ", ""),
        (r"^O capitulo trata ", ""),
        (r"^O capitulo argumenta que ", ""),
        (r"^O capitulo define ", ""),
        (r"^O capitulo apresenta ", ""),
        (r"^O capitulo contextualiza ", ""),
        (r"^O capitulo separa ", ""),
        (r"^O capitulo mostra que ", ""),
        (r"^O capitulo mostra ", ""),
        (r"^O capitulo trata ", ""),
        (r"^O capitulo discute ", ""),
        (r"^O capitulo defende ", ""),
        (r"^O capitulo descreve ", ""),
        (r"^O capitulo aborda ", ""),
        (r"^O capitulo explica ", ""),
        (r"^O capitulo examina ", ""),
        (r"^O capitulo compara ", ""),
        (r"^O capitulo usa ", "Um exemplo importante usa "),
        (r"^O capitulo final reforca que ", ""),
        (r"^O capítulo mostra como ", ""),
        (r"^O capítulo discute como ", ""),
        (r"^O capítulo descreve como ", ""),
        (r"^O capítulo explica por que ", ""),
        (r"^O capítulo mostra por que ", ""),
        (r"^O capítulo argumenta que ", ""),
        (r"^O capítulo define ", ""),
        (r"^O capítulo apresenta ", ""),
        (r"^O capítulo contextualiza ", ""),
        (r"^O capítulo separa ", ""),
        (r"^O capítulo mostra que ", ""),
        (r"^O capítulo mostra ", ""),
        (r"^O capítulo trata ", ""),
        (r"^O capítulo discute ", ""),
        (r"^O capítulo defende ", ""),
        (r"^O capítulo descreve ", ""),
        (r"^O capítulo aborda ", ""),
        (r"^O capítulo explica ", ""),
        (r"^O capítulo examina ", ""),
        (r"^O capítulo compara ", ""),
        (r"^O capítulo usa ", "Um exemplo importante usa "),
        (r"^O capítulo final reforca que ", ""),
        (r"^O capítulo final reforça que ", ""),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    if text and text[0].islower():
        text = text[0].upper() + text[1:]
    return text


def concept_explanation(concept: str, chapter: dict) -> str:
    c = concept.lower()
    explanations = [
        ("onboarding", "É o processo de formar autonomia operacional com trilha, contexto, prática supervisionada e exposição progressiva ao serviço. Em SRE, bom onboarding reduz aprendizado acidental durante crises."),
        ("engenharia reversa", "É a capacidade de entender um sistema existente a partir de código, telemetria, arquitetura, histórico de incidentes e comportamento em produção. Ela ajuda novos SREs a descobrir como o serviço realmente funciona."),
        ("raciocinio estatistico", "É usar probabilidade, distribuição, amostragem e tendência para interpretar sinais operacionais. Sem esse raciocínio, médias escondem caudas, variação vira ruído e decisões de capacidade ficam frágeis."),
        ("simulacoes de desastre", "São exercícios controlados para praticar resposta, validar runbooks e revelar lacunas antes de uma falha real. O objetivo é treinar julgamento, comunicação e recuperação."),
        ("aprendizado continuo", "É transformar incidentes, revisões, plantões e mudanças em melhoria acumulada. A equipe aprende quando registra decisões, atualiza práticas e mede se a mudança reduziu risco."),
        ("comando de incidente", "É a função que coordena resposta durante uma crise. O comandante não precisa resolver cada detalhe técnico; precisa manter prioridade, delegação, comunicação e linha do tempo claras."),
        ("delegacao de papeis", "É distribuir responsabilidades explícitas durante uma resposta. Separar coordenação, comunicação, investigação e execução evita disputa por controle e reduz trabalho duplicado."),
        ("modelo de engajamento", "É o acordo que define quando SRE entra, permanece ou sai da operação de um serviço. Ele protege a equipe contra suporte ilimitado e deixa responsabilidades visíveis."),
        ("criterios de entrada", "São requisitos mínimos para um serviço receber apoio de SRE, como SLOs, observabilidade, runbooks, rollback, ownership e capacidade de responder incidentes."),
        ("responsabilidade compartilhada", "É a divisão explícita de obrigações entre SRE, produto, plataforma e desenvolvimento. Confiabilidade melhora quando todos sabem quais decisões continuam sob seu controle."),
        ("maturidade operacional", "É o grau em que um serviço consegue ser operado com risco conhecido: alertas úteis, documentação viva, deploy reversível, dependências entendidas e incidentes aprendidos."),
        ("revisao de servico", "É uma avaliação periódica da saúde operacional do serviço. Ela verifica SLOs, incidentes, toil, dependências, capacidade, riscos e ações pendentes."),
        ("aprendizado intersetorial", "É adaptar práticas de setores de alto risco para software, como checklists, treinamento, investigação sem culpa e reporte de quase-incidentes."),
        ("cultura de reporte", "É o ambiente em que pessoas relatam falhas, riscos e quase-incidentes sem medo de punição por decisões razoáveis. Sem reporte, a organização perde sinais precoces."),
        ("adaptacao a software", "É ajustar práticas de segurança operacional ao ritmo de sistemas digitais, que mudam rápido, têm dependências distribuídas e permitem automação em escala."),
        ("confiabilidade como responsabilidade compartilhada", "É reconhecer que confiabilidade emerge de arquitetura, produto, operação, plataforma, segurança e gestão. SRE orienta a prática, mas não carrega sozinho todo o risco."),
        ("engenharia aplicada a operacao", "É usar software, automação, design de sistemas, testes e métricas para reduzir trabalho manual e tornar produção mais previsível."),
        ("escala", "É o crescimento de tráfego, serviços, equipes, dados e mudanças. Em SRE, escala exige mecanismos que não dependam de esforço humano proporcional."),
        ("trade-off", "É a escolha explícita entre dois objetivos válidos: mudar rápido e preservar estabilidade. SRE torna essa escolha defensável com SLOs, error budgets e análise de impacto."),
        ("sintomas versus causas", "Sintomas descrevem o que o usuário percebe; causas explicam por que o sistema chegou lá. Alertas devem priorizar sintomas, enquanto dashboards e investigação ajudam a chegar às causas."),
        ("caixa-preta e caixa-branca", "Monitoração caixa-preta observa o serviço por fora, como o usuário perceberia. Monitoração caixa-branca usa sinais internos, como filas, saturação, erros e dependências, para diagnóstico."),
        ("alertas acionaveis", "São alertas que exigem ação humana imediata e clara. Se uma notificação não muda uma decisão agora, ela deve virar dashboard, ticket, automação ou revisão assíncrona."),
        ("build hermetica", "É uma build que depende apenas de entradas declaradas e controladas. Isso melhora reprodutibilidade, auditoria e confiança de que o artefato promovido é o mesmo que foi testado."),
        ("simplicidade em releases", "É reduzir variáveis em cada lançamento. Mudanças menores e mais compreensíveis tornam detecção, rollback e aprendizado mais rápidos."),
        ("estabilidade versus agilidade", "É o equilíbrio entre mudar rápido e manter comportamento confiável. SRE transforma esse conflito em decisão baseada em SLO, risco e custo de falha."),
        ("linhas de codigo negativas", "É a ideia de que remover código pode aumentar valor. Menos código reduz caminhos de falha, manutenção, testes necessários e complexidade cognitiva."),
        ("apis minimas", "São interfaces pequenas e focadas. APIs menores reduzem combinações possíveis, estados inválidos e acoplamento entre equipes."),
        ("sre", "É a disciplina que aplica engenharia de software à operação de serviços. O objetivo é tornar confiabilidade uma propriedade construída no sistema, não apenas um esforço manual de suporte."),
        ("sli, slo e sla", "SLI é a métrica que mede a experiência do serviço, como taxa de sucesso ou latência. SLO é a meta definida para essa métrica. SLA é o compromisso externo, normalmente contratual, que pode ter consequências quando não é cumprido."),
        ("toil e limite", "Toil é trabalho manual, repetitivo, reativo e sem aprendizado durável. O limite explícito existe para impedir que esse trabalho consuma o tempo de engenharia necessário para corrigir causas, automatizar e simplificar o serviço."),
        ("limite explicito", "É uma regra de proteção para preservar tempo de engenharia. Se a equipe passa tempo demais em tickets, acionamentos e tarefas manuais, o serviço precisa mudar: automatizar, corrigir causa raiz, simplificar operação ou devolver parte do trabalho para a equipe responsável pelo produto."),
        ("datacenter", "É o ambiente físico e lógico onde computação, rede e armazenamento se combinam. Para SRE, entender o datacenter ajuda a enxergar falhas que não aparecem no código da aplicação."),
        ("cluster", "É um conjunto de máquinas tratado como plataforma compartilhada. Ele permite distribuir trabalho, mas exige agendamento, isolamento, monitoramento e recuperação."),
        ("orquestr", "É coordenar onde e como workloads executam. Uma boa orquestração reduz trabalho manual e permite reagir a falhas de máquina, deploys e demanda."),
        ("armazen", "É a camada que preserva dados e estado. Sua confiabilidade depende de replicação, consistência, recuperação e entendimento de modos de falha."),
        ("rede", "É o tecido que conecta usuários, serviços e dependências. Problemas de rede podem parecer falhas de aplicação, por isso precisam de sinais próprios."),
        ("lock", "É um mecanismo para coordenar acesso a um recurso compartilhado. Em sistemas distribuídos, locks precisam lidar com falhas, tempo e liderança para evitar decisões concorrentes."),
        ("vida de uma requisicao", "É o caminho completo percorrido por uma chamada do usuário até a resposta. Mapear esse caminho revela dependências, pontos de latência e locais de falha."),
        ("sli", "É a medição objetiva de um comportamento do serviço, como taxa de sucesso, latência ou frescor de dados. Sem SLI, a equipe discute confiabilidade por opinião; com SLI, discute por evidência."),
        ("slo", "É a meta que define qual nível de serviço é bom o suficiente. Um SLO bem escolhido protege a experiência do usuário e evita tanto negligência quanto perfeccionismo caro."),
        ("sla", "É o compromisso externo, normalmente com consequência contratual. Ele deve ser mais conservador que o SLO interno, porque envolve promessa formal para clientes."),
        ("error budget", "É o orçamento de risco derivado do SLO. Ele dá uma regra prática para negociar velocidade e estabilidade: enquanto há orçamento, a equipe pode assumir risco; quando ele acaba, a prioridade vira confiabilidade."),
        ("provisao", "É o orçamento de risco aceito para um período. Ele traduz indisponibilidade permitida em uma regra concreta para priorizar release, correção e estabilização."),
        ("risco", "É a chance de um serviço não entregar o comportamento esperado e o impacto dessa falha. Em SRE, risco não é ignorado nem eliminado a qualquer custo; ele é medido e administrado."),
        ("tolerancia", "É o quanto usuários, produto e negócio aceitam degradação antes que a experiência deixe de ser adequada. Ela orienta SLOs, prioridades e investimento em redundância."),
        ("disponibilidade", "É a capacidade do serviço estar utilizável quando o usuário precisa. A medida deve refletir a experiência real, não apenas se um processo está ligado."),
        ("toil", "É trabalho manual, repetitivo, reativo e sem aprendizado durável. O problema não é fazer operação; o problema é repetir a mesma operação até ela consumir a capacidade de engenharia."),
        ("trabalho operacional versus engenharia", "Trabalho operacional mantém o serviço funcionando agora. Engenharia muda o sistema para reduzir trabalho futuro, eliminar repetição ou tornar falhas menos prováveis."),
        ("carga manual", "É trabalho humano que cresce junto com tráfego, número de usuários ou quantidade de serviços. Se nada mudar, a equipe precisa crescer linearmente para manter o mesmo nível de operação."),
        ("limite de carga operacional", "É uma barreira explícita para impedir que a equipe vire apenas suporte reativo. Quando o limite é ultrapassado, o sistema precisa devolver trabalho ao produto, automatizar ou reduzir escopo."),
        ("automacao", "É investimento para remover repetição, reduzir variação humana e tornar a operação mais rápida. Boa automação é idempotente, observável e segura para repetir."),
        ("estado desejado", "É a descrição de como o sistema deveria estar. Automação madura compara estado atual com estado desejado e reconcilia diferenças."),
        ("plataformas operacionais", "São bases compartilhadas que transformam operação repetida em capacidade reutilizável. Elas reduzem variação entre equipes e tornam boas práticas mais fáceis de adotar."),
        ("consistencia", "É a previsibilidade de executar a mesma operação com o mesmo resultado esperado. Em operação, consistência reduz erro humano e facilita auditoria."),
        ("sistemas automaticos", "São sistemas que detectam e corrigem parte dos problemas sem intervenção humana. O objetivo é reduzir dependência de plantão para casos repetitivos."),
        ("build hermetica", "É uma build que depende apenas de entradas declaradas e controladas. Isso melhora reprodutibilidade e reduz surpresas entre ambientes."),
        ("implantacao continua", "É a capacidade de levar mudanças à produção com frequência e segurança. Depende de testes, rollback, observabilidade e critérios claros de promoção."),
        ("branching", "É a estratégia para organizar linhas de desenvolvimento. Estratégias simples reduzem conflito, atraso e diferença entre o que foi testado e o que será implantado."),
        ("empacotamento", "É transformar software e metadados em artefato versionado. Bons pacotes tornam deploys repetíveis e investigáveis."),
        ("gerenciamento de configuracao", "É controlar parâmetros que mudam comportamento do sistema. Configuração deve ser versionada, revisável e segura para rollback."),
        ("estabilidade versus agilidade", "É o equilíbrio entre mudar rápido e preservar comportamento confiável. SRE torna esse conflito explícito com SLOs, error budgets e processos leves."),
        ("tedio", "É a preferência por soluções previsíveis e pouco surpreendentes. Sistemas entediantes são mais fáceis de operar e recuperar."),
        ("linhas de codigo negativas", "É a ideia de que remover código pode aumentar valor. Menos código reduz caminhos de falha, manutenção e complexidade cognitiva."),
        ("apis minimas", "São interfaces pequenas e focadas. APIs menores reduzem combinações possíveis, estados inválidos e acoplamento entre equipes."),
        ("modularidade", "É separar responsabilidades com limites claros. Um módulo bom pode falhar, evoluir ou ser substituído com menor impacto no resto do sistema."),
        ("simplicidade em releases", "É reduzir variáveis em cada lançamento. Quanto menor e mais compreensível a mudança, mais fácil detectar, reverter e aprender."),
        ("monitor", "É a prática de transformar comportamento do sistema em sinais úteis. O objetivo não é coletar tudo; é produzir evidência para detectar impacto, diagnosticar e decidir."),
        ("alerta", "É um chamado à ação. Um alerta bom exige resposta humana agora; se não exige, deve virar dashboard, ticket ou automação."),
        ("caixa-preta", "Observa o serviço por fora, como um usuário ou cliente veria. É útil para detectar sintomas e validar experiência real."),
        ("caixa-branca", "Observa sinais internos, como filas, saturação, erros e dependências. É útil para diagnóstico e prevenção."),
        ("quatro sinais", "São latência, tráfego, erros e saturação. Eles formam uma base mínima para entender saúde de serviços online."),
        ("latencia", "É o tempo percebido para concluir uma operação. Em confiabilidade, caudas como p95 e p99 costumam importar mais que médias."),
        ("trafego", "É a demanda recebida pelo serviço. Entender tráfego ajuda a separar falha, mudança de padrão de uso e falta de capacidade."),
        ("erros", "São respostas ou comportamentos que não entregam o resultado esperado. A taxa de erro deve ser analisada junto com volume e impacto."),
        ("saturacao", "É o quanto o serviço está próximo do limite de um recurso, como CPU, memória, conexões, filas ou disco."),
        ("series temporais", "São medições registradas ao longo do tempo. Elas permitem ver tendências, correlações, janelas de erro e impacto de mudanças."),
        ("rotulos", "São dimensões adicionadas às métricas. Bons rótulos ajudam a filtrar por serviço, região, versão ou cliente sem criar cardinalidade descontrolada."),
        ("vetores", "São conjuntos de séries temporais relacionados. Eles permitem comparar múltiplas instâncias, regiões ou códigos de resposta."),
        ("janelas", "São períodos usados para calcular uma métrica. A janela muda a interpretação: minutos detectam incidentes rápidos; semanas mostram tendência."),
        ("expectativas", "São acordos claros sobre o que o serviço promete entregar. Sem expectativa explícita, cada equipe usa um critério diferente de sucesso."),
        ("plantao", "É a responsabilidade organizada de responder a eventos urgentes. Plantão saudável depende de alertas bons, runbooks e volume sustentável."),
        ("rodizio", "É a escala que distribui plantão entre pessoas. Deve equilibrar descanso, aprendizado, cobertura e exposição suficiente a problemas reais."),
        ("seguranca", "É a condição para responder incidentes sem medo de punição por decisões razoáveis. Sem isso, pessoas escondem falhas e atrasam aprendizado."),
        ("triagem", "É separar o que é urgente, importante e incerto. Uma boa triagem evita investigar detalhes enquanto usuários continuam impactados."),
        ("diagnostico", "É formar e testar hipóteses sobre a causa do problema. Ele deve ser guiado por evidências, não por tentativa aleatória."),
        ("hipotes", "É uma explicação testável para o problema. Hipóteses boas podem ser confirmadas ou descartadas rapidamente."),
        ("emerg", "É uma situação em que impacto, urgência e incerteza exigem resposta coordenada. Treino e papéis claros reduzem improviso perigoso."),
        ("incidente", "É um evento que degrada ou ameaça a experiência do usuário. Gerenciamento de incidentes coordena pessoas, comunicação e mitigação."),
        ("documento vivo", "É o registro em tempo real do que se sabe, decidiu e fez durante um incidente. Ele evita perda de contexto e melhora handoff."),
        ("handoff", "É a passagem explícita de responsabilidade. Deve deixar claro quem está no comando, qual é o estado e quais ações continuam abertas."),
        ("interrup", "É perda ou degradação relevante de serviço. Registrar interrupções permite medir tendência, impacto e causas recorrentes."),
        ("agregacao", "É combinar eventos ou métricas para enxergar padrões. Sem agregação, a equipe vê casos isolados e perde tendências."),
        ("atribuicao", "É associar rótulos ou causas a eventos. Ajuda a responder perguntas como onde ocorreu, quem foi afetado e que tipo de falha se repetiu."),
        ("analise", "É transformar dados operacionais em entendimento. A análise procura padrões, correlações e causas prováveis, não apenas números bonitos."),
        ("beneficios inesperados", "São ganhos que surgem quando a organização mede melhor. Dados de interrupção podem revelar dependências, gargalos e riscos antes invisíveis."),
        ("linha de base", "É o estado normal usado para comparar melhorias ou regressões. Sem baseline, a equipe não sabe se está melhorando."),
        ("teste", "É uma forma controlada de descobrir se o sistema se comporta como esperado. Para confiabilidade, testes precisam incluir falhas, carga e recuperação."),
        ("sondas", "São verificações ativas que simulam comportamentos importantes. Elas detectam problemas que métricas internas podem não revelar."),
        ("planejamento", "É transformar intenção, demanda e restrições em capacidade e ações. Em SRE, planejamento ruim vira incidente futuro."),
        ("ferramentas internas", "São produtos criados para reduzir esforço operacional recorrente. Elas precisam de adoção, manutenção e integração ao fluxo real da equipe."),
        ("adocao", "É o uso efetivo da prática ou ferramenta pela organização. Sem adoção, a solução existe no repositório, mas não muda confiabilidade."),
        ("dns", "É um mecanismo comum de direcionamento de usuários. Em confiabilidade, influencia failover, latência e distribuição geográfica."),
        ("vip", "É um endereço virtual usado para direcionar tráfego a backends. Ele simplifica entrada, mas precisa de saúde e roteamento corretos."),
        ("balanceamento", "É distribuir carga entre recursos disponíveis. Bom balanceamento considera saúde, proximidade, custo, capacidade e comportamento de clientes."),
        ("controle de fluxo", "É limitar quanto trabalho entra em uma parte do sistema. Ele protege dependências e evita que sobrecarga vire falha em cascata."),
        ("throttling", "É reduzir ou rejeitar requisições antes que o sistema colapse. Pode acontecer no cliente, no servidor ou em gateways."),
        ("criticidade", "É a prioridade relativa de tráfegos ou operações. Em sobrecarga, requisições críticas devem ser preservadas antes de trabalho menos importante."),
        ("sobrecarga", "É quando demanda excede capacidade útil. O sistema precisa degradar de forma planejada em vez de falhar de forma caótica."),
        ("cascata", "É quando uma falha local aumenta carga ou erro em outras partes até derrubar o sistema. Retentativas sem controle são causa comum."),
        ("backoff", "É esperar progressivamente mais antes de tentar de novo. Ele reduz amplificação de carga durante falhas."),
        ("jitter", "É variação aleatória adicionada a tempos de espera. Evita que muitos clientes tentem novamente ao mesmo tempo."),
        ("degradacao", "É reduzir funcionalidade de forma controlada para preservar o núcleo do serviço. É melhor entregar menos do que colapsar tudo."),
        ("consenso", "É o mecanismo que permite a várias réplicas concordarem sobre uma decisão crítica. Ele evita estados contraditórios em temas como liderança, locks e configuração."),
        ("paxos", "É uma família de protocolos de consenso. O ponto prático é permitir decisão confiável mesmo quando processos ou máquinas falham."),
        ("quorum", "É o conjunto mínimo de réplicas necessário para aceitar uma decisão. Ele equilibra disponibilidade e segurança do estado."),
        ("split-brain", "É quando partes do sistema acreditam ter autoridade ao mesmo tempo. Pode causar corrupção, perda de dados ou decisões conflitantes."),
        ("cron", "É agendamento periódico. Em larga escala, precisa lidar com duplicidade, atraso, falha, liderança e idempotência."),
        ("idempot", "É a propriedade de repetir uma operação sem causar efeito colateral indesejado. É essencial para retries, jobs e automação segura."),
        ("pipeline", "É uma sequência de etapas de processamento. Confiabilidade depende de estado, reexecução, observabilidade e validação de resultados."),
        ("workflow", "É a representação explícita de etapas, dependências e estado de execução. Ajuda a entender onde um pipeline parou e como retomar."),
        ("estagios", "São partes sequenciais ou paralelas de um processamento. Cada estágio precisa declarar entrada, saída, erro e condição de reexecução."),
        ("continuidade", "É manter o processo útil mesmo com falhas parciais. Em pipelines, significa detectar atraso, reprocessar e preservar dados corretos."),
        ("carga irregular", "É variação de demanda ao longo do tempo. Ela pode criar picos artificiais, filas e atrasos se todos os trabalhos forem agendados juntos."),
        ("thundering herd", "É quando muitos processos disparam ao mesmo tempo e sobrecarregam dependências. Espalhar horários e controlar concorrência reduz o risco."),
        ("integridade", "É a garantia de que dados permanecem corretos, completos e recuperáveis. Usuários percebem integridade pelo resultado, não pela arquitetura."),
        ("backup", "É apenas uma parte da estratégia de recuperação. O que importa é conseguir restaurar dados corretos dentro do tempo necessário para o negócio."),
        ("replicacao", "É manter cópias de dados ou estado. Ela melhora disponibilidade, mas também pode replicar corrupção se não houver detecção e controle."),
        ("rollout", "É a liberação gradual de uma mudança. Permite observar impacto em pequena escala antes de afetar todos os usuários."),
        ("launch coordination", "É a coordenação de lançamento com foco em riscos, dependências e prontidão operacional. Ela ajuda produto e engenharia a lançar sem improviso."),
        ("feature", "Flags permitem ativar, desativar ou limitar funcionalidades sem novo deploy. Elas reduzem risco, mas precisam de ciclo de limpeza."),
        ("checklist", "É uma memória operacional externa. Ajuda a evitar esquecimentos em lançamentos, incidentes e mudanças repetidas."),
        ("onboarding", "É o processo de formar autonomia. Em SRE, deve incluir arquitetura, incidentes passados, shadowing e prática operacional."),
        ("comunicacao", "É infraestrutura de coordenação. Sem comunicação clara, equipes tomam decisões incompatíveis durante mudanças e incidentes."),
        ("reunioes", "São pontos de sincronização para decisões e riscos operacionais. Reuniões boas têm pauta, decisões registradas e próximos passos claros."),
        ("agenda", "É o contrato da reunião. Uma agenda clara evita discussões abertas demais e mantém foco em produção, risco e decisão."),
        ("composicao da equipe", "É a combinação de habilidades e responsabilidades. Em SRE, mistura engenharia de software, sistemas, operação e comunicação."),
        ("tecnicas", "São práticas de colaboração, documentação e tomada de decisão. Elas tornam trabalho entre equipes menos dependente de relações informais."),
        ("colaboracao", "É alinhar times com responsabilidades diferentes. Em SRE, colaboração boa transforma conflito entre velocidade e estabilidade em decisão explícita."),
        ("engajamento", "É o modelo de entrada, saída e responsabilidade entre SRE e equipes de produto. Evita que SRE vire apenas fila de suporte."),
        ("mercados", "Comparar com outros setores ajuda a importar práticas como checklists, investigação sem culpa e treinamento, adaptando ao ritmo do software."),
        ("maquinas imperfeitas", "É o reconhecimento de que pessoas e sistemas falham. Bons processos reduzem carga cognitiva e tornam a ação correta mais fácil."),
        ("fluxo cognitivo", "É a capacidade de manter atenção em uma tarefa complexa. Interrupções frequentes quebram raciocínio e aumentam erro operacional."),
        ("reduzindo as interrupcoes", "É projetar canais, alertas e processos para proteger foco. Menos interrupção melhora qualidade de diagnóstico e engenharia."),
        ("fazer bem uma tarefa", "É limitar multitarefa durante trabalho crítico. Em incidentes, clareza de papel ajuda cada pessoa a executar uma função por vez."),
        ("subconjuntos", "São grupos menores de backends usados por clientes. Reduzem conexões totais e tornam balanceamento mais controlável."),
        ("estado de incapacidade", "É um sinal de que uma tarefa não deve receber tráfego. Ajuda load balancers a evitar backends vivos, mas incapazes de servir bem."),
        ("round robin", "É distribuir requisições em sequência. É simples, mas pode ignorar diferenças de carga, custo e saúde entre backends."),
        ("least-loaded", "É escolher backends menos carregados. Ajuda quando a carga por requisição varia, mas depende de sinais de utilização confiáveis."),
        ("arquivamentos", "São retenções de longo prazo com finalidade diferente de recuperação operacional rápida. Arquivo não substitui backup testado."),
        ("recuperacao", "É restaurar serviço ou dados após falha. A estratégia só é confiável quando é testada e tem objetivo de tempo e perda aceitável."),
        ("defesa em profundidade", "É combinar camadas de prevenção, detecção e recuperação. Nenhuma camada isolada deve ser a única proteção de dados críticos."),
    ]
    for key, value in explanations:
        if key in c:
            return value
    if len(concept) <= 4 and concept.isupper():
        return (
            f"É uma sigla operacional importante no tema do capítulo. Antes de automatizar, "
            f"a equipe precisa concordar sobre seu significado, onde aparece no sistema e "
            f"qual decisão ela orienta."
        )
    return (
        "É uma prática que transforma uma preocupação operacional em decisão concreta. "
        "Ela aparece quando a equipe precisa escolher entre aceitar risco, automatizar, "
        "simplificar, melhorar observabilidade, mudar o processo de release ou corrigir a "
        "causa raiz de um problema recorrente."
    )


def concept_deep_dive(chapter: dict) -> str:
    blocks = []
    for index, concept in enumerate(chapter["concepts"]):
        practice = chapter["practice"][index % len(chapter["practice"])]
        if index % 3 == 0:
            bridge = f"Uma forma simples de aplicar isso é: {practice}"
        elif index % 3 == 1:
            bridge = f"No dia a dia, isso aparece quando a equipe precisa {practice[0].lower() + practice[1:]}"
        else:
            bridge = f"Esse conceito fica concreto quando a equipe consegue {practice[0].lower() + practice[1:]}"
        blocks.append(
            f"""### **{concept}**

**{concept}**: {concept_explanation(concept, chapter)}

{bridge}
"""
        )
    return "\n".join(blocks)


def worked_example(chapter: dict) -> str:
    first = chapter["concepts"][0]
    return f"""Imagine uma API de pagamentos com deploy diário.

1. A equipe escolhe **{first}** como foco da semana.
2. Ela identifica um fluxo crítico: autorização de pagamento.
3. Define uma evidência simples: taxa de sucesso, latência p95, número de alertas ou tempo de recuperação.
4. Faz uma mudança pequena: melhora um alerta, adiciona um runbook, ajusta um timeout ou cria uma métrica.
5. Na retrospectiva, compara o antes e o depois.

O objetivo do exemplo não é resolver toda a confiabilidade do serviço. É criar um ciclo curto de aprendizado: observar, decidir, mudar e verificar.
"""


def common_mistakes(chapter: dict) -> str:
    return bullets([
        "Copiar práticas de outra organização sem adaptar ao risco e ao tamanho do serviço.",
        "Criar documentação ou processo sem dono, sem revisão e sem uso durante incidentes reais.",
        "Medir apenas sinais internos e esquecer o que o usuário percebe.",
        "Automatizar uma rotina ruim antes de entender por que ela existe.",
        "Tratar confiabilidade como responsabilidade exclusiva de SRE, e não como propriedade compartilhada.",
    ])


def fast_learning_guide(chapter: dict) -> str:
    return f"""Leia este capítulo em três passadas:

1. **Primeira passada:** entenda a ideia central: {chapter["central"]}
2. **Segunda passada:** explique cada conceito-chave usando um serviço que você conhece.
3. **Terceira passada:** escolha uma ação pequena da seção **Aplicando amanhã** e transforme em tarefa prática.

Para aprendizado rápido, não tente memorizar todos os termos. Foque em responder:

- Que risco este conceito reduz?
- Que decisão ele melhora?
- Que evidência mostra que ele funcionou?
"""


def diagram_block(chapter: dict) -> str:
    concepts = chapter["concepts"][:4]
    if len(concepts) < 3:
        return ""
    labels = [normalize_pt_br(concept).replace('"', "'") for concept in concepts]
    return f"""## Diagrama de apoio

```mermaid
flowchart LR
    Tema["{chapter['title']}"] --> C1["{labels[0]}"]
    C1 --> C2["{labels[1]}"]
    C2 --> C3["{labels[2]}"]
    C3 --> Decisao["Decisão operacional"]
    Decisao --> Acao["Melhoria no serviço"]
```

"""


CHAPTER_SOURCE_LINKS = {
    3: [
        ("Google SRE Book - Embracing Risk", "https://sre.google/sre-book/embracing-risk/"),
        ("Site Reliability Workbook - Implementing SLOs", "https://sre.google/workbook/implementing-slos/"),
    ],
    4: [
        ("Google SRE Book - Service Level Objectives", "https://sre.google/sre-book/service-level-objectives/"),
        ("Site Reliability Workbook - Implementing SLOs", "https://sre.google/workbook/implementing-slos/"),
        ("Site Reliability Workbook - Alerting on SLOs", "https://sre.google/workbook/alerting-on-slos/"),
    ],
    5: [
        ("Google SRE Book - Eliminating Toil", "https://sre.google/sre-book/eliminating-toil/"),
        ("Site Reliability Workbook - Eliminating Toil", "https://sre.google/workbook/eliminating-toil/"),
    ],
    6: [
        ("Google SRE Book - Monitoring Distributed Systems", "https://sre.google/sre-book/monitoring-distributed-systems/"),
        ("Site Reliability Workbook - Monitoring", "https://sre.google/workbook/monitoring/"),
        ("OpenTelemetry - Signals", "https://opentelemetry.io/docs/concepts/signals/"),
    ],
    7: [
        ("Google SRE Book - The Evolution of Automation at Google", "https://sre.google/sre-book/automation-at-google/"),
        ("Google SRE Book - Introduction", "https://sre.google/sre-book/introduction/"),
    ],
    8: [
        ("Google SRE Book - Release Engineering", "https://sre.google/sre-book/release-engineering/"),
        ("Site Reliability Workbook - Canarying Releases", "https://sre.google/workbook/canarying-releases/"),
    ],
    9: [
        ("Google SRE Book - Simplicity", "https://sre.google/sre-book/simplicity/"),
        ("Site Reliability Workbook - Simplicity", "https://sre.google/workbook/simplicity/"),
    ],
    10: [("Google SRE Book - Practical Alerting", "https://sre.google/sre-book/practical-alerting/")],
    11: [
        ("Google SRE Book - Being On-Call", "https://sre.google/sre-book/being-on-call/"),
        ("Site Reliability Workbook - On-Call", "https://sre.google/workbook/on-call/"),
    ],
    12: [("Google SRE Book - Effective Troubleshooting", "https://sre.google/sre-book/effective-troubleshooting/")],
    13: [
        ("Google SRE Book - Emergency Response", "https://sre.google/sre-book/emergency-response/"),
        ("Site Reliability Workbook - Incident Response", "https://sre.google/workbook/incident-response/"),
    ],
    14: [
        ("Google SRE Book - Managing Incidents", "https://sre.google/sre-book/managing-incidents/"),
        ("Google SRE Book - Example Incident State Document", "https://sre.google/sre-book/example-incident-state-document/"),
    ],
    15: [
        ("Google SRE Book - Postmortem Culture", "https://sre.google/sre-book/postmortem-culture/"),
        ("Site Reliability Workbook - Postmortem Culture", "https://sre.google/workbook/postmortem-culture/"),
    ],
    16: [("Google SRE Book - Tracking Outages", "https://sre.google/sre-book/tracking-outages/")],
    17: [("Google SRE Book - Testing for Reliability", "https://sre.google/sre-book/testing-reliability/")],
    18: [("Google SRE Book - Software Engineering in SRE", "https://sre.google/sre-book/software-engineering-in-sre/")],
    19: [("Google SRE Book - Load Balancing at the Frontend", "https://sre.google/sre-book/load-balancing-frontend/")],
    20: [("Google SRE Book - Load Balancing in the Datacenter", "https://sre.google/sre-book/load-balancing-datacenter/")],
    21: [("Google SRE Book - Handling Overload", "https://sre.google/sre-book/handling-overload/")],
    22: [("Google SRE Book - Addressing Cascading Failures", "https://sre.google/sre-book/addressing-cascading-failures/")],
    23: [("Google SRE Book - Managing Critical State", "https://sre.google/sre-book/managing-critical-state/")],
    24: [("Google SRE Book - Distributed Periodic Scheduling with Cron", "https://sre.google/sre-book/distributed-periodic-scheduling/")],
    25: [("Google SRE Book - Data Processing Pipelines", "https://sre.google/sre-book/data-processing-pipelines/")],
    26: [("Google SRE Book - Data Integrity", "https://sre.google/sre-book/data-integrity/")],
    27: [
        ("Google SRE Book - Reliable Product Launches at Scale", "https://sre.google/sre-book/reliable-product-launches/"),
        ("Google SRE Book - Launch Coordination Checklist", "https://sre.google/sre-book/launch-checklist/"),
    ],
    28: [("Google SRE Book - Accelerating SREs to On-Call and Beyond", "https://sre.google/sre-book/accelerating-sre-on-call/")],
    29: [("Google SRE Book - Dealing with Interrupts", "https://sre.google/sre-book/dealing-with-interrupts/")],
    30: [("Google SRE Book - Operational Overload", "https://sre.google/sre-book/operational-overload/")],
    31: [("Google SRE Book - Communication and Collaboration in SRE", "https://sre.google/sre-book/communication-and-collaboration/")],
    32: [
        ("Google SRE Book - The Evolving SRE Engagement Model", "https://sre.google/sre-book/evolving-sre-engagement-model/"),
        ("Site Reliability Workbook - SRE Engagement Model", "https://sre.google/workbook/engagement-model/"),
    ],
    33: [("Google SRE Book - Lessons Learned from Other Industries", "https://sre.google/sre-book/lessons-learned/")],
    34: [
        ("Google SRE Book - Part V Conclusions", "https://sre.google/sre-book/part-V-conclusions/"),
        ("Google SRE Book - Service Best Practices", "https://sre.google/sre-book/service-best-practices/"),
    ],
}


MODERN_LINKS = [
    ("Google Cloud Well-Architected Framework", "https://docs.cloud.google.com/architecture/framework"),
    ("AWS Well-Architected Reliability Pillar", "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html"),
    ("Azure Well-Architected Reliability", "https://learn.microsoft.com/en-us/azure/well-architected/reliability/"),
    ("DORA Research Program", "https://dora.dev/research/"),
    ("OpenTelemetry Signals", "https://opentelemetry.io/docs/concepts/signals/"),
]


def link_lines(links: list[tuple[str, str]]) -> str:
    lines = []
    for label, url in links:
        if "**" in label:
            lines.append(f"- {label}. <{url}>")
        else:
            lines.append(f"- **{label}:** <{url}>")
    return "\n".join(lines)


def chapter_links(chapter: dict) -> list[tuple[str, str]]:
    return CHAPTER_SOURCE_LINKS.get(chapter["number"], [])


def why_it_matters(chapter: dict) -> str:
    number = chapter["number"]
    first = chapter["concepts"][0]
    if 3 <= number <= 9:
        return (
            f"Sem **{first}**, a equipe tende a discutir confiabilidade por opinião: "
            "um grupo pede mais velocidade, outro pede mais estabilidade, e ninguém "
            "consegue explicar qual risco está sendo aceito. A decisão melhora quando "
            "o risco vira critério técnico, mensurável e negociável."
        )
    if 10 <= number <= 27:
        return (
            f"**{first}** importa porque serviços reais falham sob mudança, carga, "
            "dependências lentas, estado distribuído e comportamento humano. A equipe "
            "reduz surpresa quando transforma esse risco em rotina operacional clara, "
            "sinais confiáveis e decisões treinadas antes da crise."
        )
    return (
        f"**{first}** importa porque sistemas de produção são mantidos por pessoas, "
        "rotinas, decisões e relações entre equipes. Sem gestão explícita, mesmo boas "
        "práticas técnicas se degradam em filas de suporte, interrupções constantes e "
        "responsabilidades ambíguas."
    )


def current_practice(chapter: dict) -> str:
    number = chapter["number"]
    title = chapter["title"].lower()
    if number in {3, 4}:
        return (
            "Hoje, **SLOs** e **error budgets** aparecem em revisões de arquitetura, "
            "plataformas internas, políticas de rollout e alertas por queima de orçamento. "
            "A prática moderna é começar por jornadas críticas do usuário, medir poucos "
            "indicadores confiáveis e usar esses objetivos para orientar release, incidentes "
            "e priorização de trabalho."
        )
    if number == 5:
        return (
            "Em plataformas cloud native, **toil** costuma aparecer em tickets repetitivos, "
            "ajustes manuais de infraestrutura, aprovações operacionais e alertas que não "
            "geram decisão. Engenharia de plataforma, GitOps e automações idempotentes são "
            "úteis quando removem a causa do trabalho manual, não apenas aceleram uma rotina ruim."
        )
    if number == 6:
        return (
            "A prática atual combina monitoração e **observabilidade**. Métricas continuam "
            "essenciais para SLOs e alertas; logs e traces ajudam a investigar sistemas "
            "distribuídos. OpenTelemetry consolidou uma linguagem comum para instrumentar "
            "aplicações sem prender a equipe a uma única ferramenta."
        )
    if number == 7:
        return (
            "Automação moderna aparece em controladores Kubernetes, GitOps, pipelines, "
            "políticas de plataforma e reconciliação de estado desejado. Automação confiável "
            "precisa conhecer intenção, validar resultado e "
            "falhar de modo observável."
        )
    if number == 8:
        return (
            "Release engineering hoje envolve CI/CD, builds reprodutíveis, SBOMs, "
            "assinatura de artefatos, canários, feature flags e rollback automatizado. "
            "A tecnologia varia; a disciplina continua sendo tornar mudanças pequenas, "
            "auditáveis, testáveis e reversíveis."
        )
    if number == 9:
        return (
            "Em sistemas atuais, simplicidade compete com microsserviços, múltiplas clouds, "
            "configuração dinâmica e pilhas de observabilidade. A recomendação prática é "
            "reduzir estados, dependências e exceções antes de adicionar mais plataforma."
        )
    if any(word in title for word in ["monitor", "alertas", "interrup"]):
        return (
            "A prática moderna usa métricas, logs e traces com contexto compartilhado. "
            "Alertas devem representar impacto ou risco real para o usuário; o restante "
            "deve virar dashboard, análise assíncrona ou automação."
        )
    if any(word in title for word in ["plantão", "incidente", "emerg", "postmortem"]):
        return (
            "Ferramentas de incident management ajudam com escala, escalonamento e linha "
            "do tempo, mas não substituem papéis claros, comunicação objetiva e postmortems "
            "com ações rastreáveis."
        )
    if any(word in title for word in ["release", "lançamento", "teste"]):
        return (
            "Rollouts graduais, canários, feature flags e validações automatizadas reduzem "
            "o raio de impacto de mudanças. A prática só funciona quando há métricas de "
            "saúde, critérios de promoção e rollback exercitado."
        )
    if number >= 28:
        return (
            "Gestão moderna de SRE aparece em onboarding estruturado, catálogos de serviço, "
            "revisões de prontidão, scorecards de confiabilidade, políticas de plantão e "
            "mecanismos de colaboração entre produto, plataforma e operação."
        )
    return (
        "Em ambientes atuais, este tema aparece em revisões de serviço, plataformas internas, "
        "pipelines, dashboards, políticas de rollout e práticas de cloud native. A tecnologia "
        "muda; o princípio continua sendo tornar risco, responsabilidade e evidência visíveis."
    )


def chapter_specific_mistakes(chapter: dict) -> list[str]:
    number = chapter["number"]
    by_number = {
        3: [
            "Tratar 100% de disponibilidade como meta moral, sem discutir custo e expectativa do usuário.",
            "Usar error budget como desculpa para descuido, e não como limite de risco.",
            "Comparar serviços diferentes com a mesma meta sem considerar impacto e mercado.",
        ],
        4: [
            "Escolher SLIs porque são fáceis de coletar, não porque refletem experiência do usuário.",
            "Definir SLO sem janela de medição, fonte de dados e consequência operacional.",
            "Confundir SLA contratual com meta interna de engenharia.",
        ],
        5: [
            "Chamar todo trabalho chato de toil.",
            "Automatizar uma rotina ruim sem remover a causa do trabalho repetitivo.",
            "Aceitar que plantão e tickets consumam todo o tempo de engenharia.",
        ],
        6: [
            "Alertar sobre causas internas sem impacto real para usuários.",
            "Construir dashboards enormes que não ajudam diagnóstico.",
            "Usar média de latência e esconder caudas relevantes como p95 ou p99.",
        ],
        7: [
            "Confundir script com automação confiável.",
            "Criar automação que não registra, valida ou expõe falhas.",
            "Codificar passos manuais frágeis sem declarar estado desejado.",
        ],
        8: [
            "Depender de uma pessoa para construir ou promover releases.",
            "Misturar build, configuração e deploy sem rastreabilidade.",
            "Fazer rollout sem critério objetivo de rollback.",
        ],
        9: [
            "Adicionar abstrações antes de remover complexidade acidental.",
            "Manter features ou APIs pouco usadas por medo de limpeza.",
            "Confundir simplicidade com falta de capacidade de evolução.",
        ],
    }
    if number in by_number:
        return by_number[number]
    if number >= 28:
        return [
            "Tratar o problema como falta de processo quando a causa é ambiguidade de responsabilidade.",
            "Criar reuniões, checklists ou treinamentos sem dono e sem revisão.",
            "Separar gestão de SRE da realidade técnica dos serviços em produção.",
        ]
    return [
        "Aplicar a prática como checklist sem conectar a risco real do serviço.",
        "Criar documentação ou automação sem validar durante incidentes ou mudanças reais.",
        "Medir apenas sinais internos e esquecer o impacto percebido pelo usuário.",
    ]


def review_questions(chapter: dict) -> list[str]:
    first = chapter["concepts"][0]
    return [
        f"Qual risco operacional **{first}** ajuda a reduzir?",
        "Que evidência mostraria que a prática foi aplicada com sucesso?",
        "Como esse conceito mudaria uma decisão de release, plantão, arquitetura ou priorização?",
    ]


def resources_block(chapter: dict) -> str:
    links = [
        ("Livro oficial online do Google SRE", "https://sre.google/sre-book/"),
        ("The Site Reliability Workbook", "https://sre.google/workbook/"),
        *chapter_links(chapter),
    ]
    if chapter["number"] in {4, 6, 10, 16}:
        links.append(("OpenTelemetry Signals", "https://opentelemetry.io/docs/concepts/signals/"))
    if chapter["number"] in {8, 17, 27}:
        links.append(("Site Reliability Workbook - Canarying Releases", "https://sre.google/workbook/canarying-releases/"))
    if chapter["number"] in {28, 29, 30, 31, 32, 33, 34}:
        links.append(("Google SRE Resources", "https://sre.google/resources/"))
    return "## Recursos complementares\n\n" + link_lines(links) + "\n"


def references_block(chapter: dict) -> str:
    links = [
        ("Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016", "https://sre.google/sre-book/"),
        ("Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018", "https://sre.google/workbook/"),
        *chapter_links(chapter),
    ]
    if 3 <= chapter["number"] <= 34:
        links.extend(MODERN_LINKS[:2])
    lines = link_lines(links)
    return f"""## Referências

{lines}
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = dedent(content).strip() + "\n"
    if path.suffix == ".md":
        text = normalize_pt_br(text)
    path.write_text(text, encoding="utf-8")


def chapter_one_page() -> str:
    return """# Capítulo 01 - Introdução

## Objetivos de aprendizagem

- Entender SRE como engenharia de software aplicada à operação de serviços.
- Explicar por que trabalho operacional precisa de limite explícito.
- Diferenciar SLI, SLO, SLA, error budget e toil.
- Relacionar métricas, metas, automação e postmortems.
- Identificar sinais de que uma equipe está operando de forma reativa demais.

## Problema que este tema resolve

Serviços não se mantêm confiáveis apenas porque há pessoas de plantão. Quando tráfego, dependências e frequência de mudança crescem, tarefas manuais também crescem. A equipe começa a passar mais tempo respondendo incidentes, executando procedimentos repetidos e desbloqueando releases do que melhorando o sistema.

SRE surge para quebrar esse ciclo. A ideia central é operar produção com mentalidade de engenharia: medir o que importa, automatizar o repetitivo, reduzir risco de mudança e aprender com falhas.

## Conceitos-chave

- SRE como engenharia de software aplicada a operações.
- SLIs e SLOs como base objetiva para falar de confiabilidade.
- Limite explícito para trabalho operacional.
- Error budget como mecanismo de equilíbrio entre velocidade e estabilidade.
- Postmortems sem culpa.
- Automação para reduzir dependência humana.

## Fundamentos

Antes de avançar, vale fixar o vocabulário mínimo. Estes termos aparecem ao longo de todo o curso e precisam ser entendidos como ferramentas de decisão, não como siglas decorativas.

| Conceito | Explicação |
| --- | --- |
| Serviço | Sistema oferecido a usuários ou a outros sistemas, como uma API, uma aplicação web, um pipeline ou uma plataforma interna. |
| Produção | Ambiente real em que o serviço atende usuários, integrações e processos de negócio. |
| SRE | Disciplina que usa engenharia de software para operar serviços confiáveis em escala. |
| Confiabilidade | Capacidade de entregar o comportamento esperado quando o usuário precisa. Não significa perfeição; significa atender expectativas explícitas. |
| SLI | Indicador de nível de serviço. É uma métrica que mede a experiência real, como taxa de sucesso, latência, disponibilidade ou frescor de dados. |
| SLO | Objetivo de nível de serviço. É a meta definida para um SLI, por exemplo: 99,9% das requisições devem terminar com sucesso em 30 dias. |
| SLA | Acordo de nível de serviço. É um compromisso externo, geralmente contratual, com consequências se não for cumprido. |
| Error budget | Orçamento de erro. É a margem de falha aceitável criada pelo SLO; se o SLO é 99,9%, a margem restante é o risco que pode ser gasto no período. |
| Toil | Trabalho manual, repetitivo, reativo e sem aprendizado duradouro. Reiniciar processos toda semana, aprovar mudanças triviais manualmente ou responder sempre ao mesmo alerta são exemplos comuns. |
| Incidente | Evento que degrada ou interrompe o serviço e exige resposta coordenada. |
| Postmortem | Análise de incidente orientada a aprendizado, sem busca por culpados, com ações de melhoria rastreáveis. |
| Release ou deploy | Processo de levar uma mudança para produção. |
| Rollback | Retorno seguro para uma versão ou configuração anterior quando uma mudança causa problema. |
| Runbook | Guia operacional com passos claros para diagnosticar ou resolver uma situação conhecida. |
| Automação | Uso de software para executar, validar ou corrigir tarefas operacionais com menos intervenção humana. |
| Observabilidade | Capacidade de entender o estado do serviço por sinais como métricas, logs e traces. |
| Idempotência | Propriedade de uma ação que pode ser repetida sem causar dano adicional, como executar duas vezes uma correção que deixa o sistema no mesmo estado final. |

Um exemplo simples ajuda a conectar os termos. Se uma API de pagamentos mede a porcentagem de transações bem-sucedidas, essa métrica é um SLI. Se a equipe decide que 99,95% das transações devem funcionar em uma janela de 30 dias, isso é um SLO. A diferença entre essa meta e 100% é o error budget. Quando a equipe gasta esse orçamento com falhas, ela reduz a velocidade de mudanças e prioriza estabilidade. Se alguém precisa reiniciar manualmente um componente todos os dias para manter o SLO, esse trabalho é toil e deve virar correção ou automação.

## Conceitos intermediários

- Operação e desenvolvimento precisam negociar risco com base em dados.
- O trabalho operacional repetitivo não pode consumir todo o tempo da equipe.
- Mudanças devem ser rápidas, mas precisam respeitar os SLOs do serviço.
- Incidentes são fonte de aprendizado quando analisados sem culpa.

## Conceitos avançados

- Error budgets transformam confiabilidade em mecanismo de governança técnica.
- Automação madura elimina classes inteiras de trabalho manual, não apenas acelera cliques.
- SRE saudável devolve sinais ruins para arquitetura, produto e plataforma.
- A equipe precisa proteger tempo de engenharia para evitar virar suporte reativo.

## Explicação

O capítulo apresenta SRE como uma resposta ao conflito clássico entre desenvolvimento e operações. Desenvolvimento quer lançar funcionalidades. Operações quer reduzir risco em produção. Sem uma regra comum, essa tensão vira burocracia, bloqueios ou releases arriscados.

A proposta de SRE é tornar essa tensão explícita e mensurável. Primeiro a equipe escolhe SLIs que representem a experiência do usuário: sucesso de requisições, latência, disponibilidade, durabilidade ou frescor de dados. Depois define SLOs para esses indicadores. Esses objetivos geram um orçamento de erro. Enquanto há orçamento, a equipe pode aceitar mudanças com risco controlado. Quando o orçamento acaba, estabilizar passa a ser mais importante que lançar.

Essa lógica só funciona se SRE tiver tempo para engenharia. Se a equipe fica presa em tickets, acionamentos e tarefas manuais, ela perde a capacidade de melhorar o serviço. O nome desse trabalho repetitivo é toil. Por isso o limite de trabalho operacional é uma ideia central: ele protege o tempo necessário para corrigir causas, automatizar e simplificar.

## Guia de estudo rápido

Para estudar este capítulo, foque em quatro perguntas:

1. Que trabalho operacional está crescendo junto com o serviço?
2. Como sabemos se o usuário está recebendo um serviço aceitável?
3. Quanto risco de mudança ainda podemos assumir?
4. Que tarefa repetitiva deveria virar automação ou correção definitiva?

## Aprofundamento dos conceitos-chave

### SRE como engenharia de software aplicada a operações

SRE não é apenas uma equipe com acesso a produção. É uma forma de operar serviços usando as ferramentas da engenharia: código, revisão, testes, automação, métricas e análise de falhas.

O objetivo é reduzir dependência de intervenção manual. Pessoas continuam essenciais, mas devem gastar menos tempo repetindo procedimentos e mais tempo melhorando o sistema.

### SLI, SLO e SLA

SLI, SLO e SLA formam uma sequência. O SLI mede um comportamento real. O SLO define qual resultado é bom o suficiente. O SLA transforma parte dessa promessa em compromisso externo.

Uma API pode ter um SLI de disponibilidade calculado pela porcentagem de requisições HTTP bem-sucedidas. O SLO pode exigir 99,9% de sucesso em 30 dias. O SLA, quando existe, costuma ser mais conservador, porque envolve clientes, contrato e compensações.

O erro comum é medir o que é fácil, não o que importa. CPU alta pode ser útil para diagnóstico, mas raramente descreve a experiência do usuário. Para SLO, prefira indicadores ligados ao que o usuário percebe: conseguir autenticar, pagar, pesquisar, enviar mensagem, receber resultado ou recuperar dados.

### Toil e limite explícito para trabalho operacional

Toil é trabalho operacional que se repete, depende de ação humana e não cria melhoria duradoura. Ele pode parecer inevitável no começo, mas vira um problema estrutural quando cresce junto com o número de usuários, serviços ou deploys.

Nem todo trabalho operacional é ruim. Investigar um incidente novo pode gerar aprendizado. Acompanhar um lançamento crítico pode ser prudente. O problema é repetir a mesma ação manualmente sem mudar o sistema. Quando isso acontece, a equipe paga a mesma conta várias vezes.

Um limite explícito para trabalho operacional impede que SRE vire uma fila permanente de tarefas manuais. Quando tickets, acionamentos e procedimentos repetidos consomem tempo demais, o serviço está mostrando que precisa de investimento técnico.

Esse investimento pode ser automação, melhoria de monitoramento, correção de bug, simplificação de release, mudança de arquitetura ou devolução de responsabilidade para a equipe que mantém o produto. Se o trabalho repetitivo não é limitado, ele ocupa o espaço da engenharia.

### Error budget como mecanismo de equilíbrio

O error budget conecta confiabilidade e velocidade. Se um serviço promete determinado SLO, a diferença entre a meta e a perfeição é a margem de falha que pode ser gasta. Um SLO de 99,9% em 30 dias aceita cerca de 0,1% de falhas nesse período. Essa margem não é autorização para descuido; é um limite explícito para tomar risco com consciência.

Essa margem ajuda a decidir. Com orçamento disponível, releases podem continuar. Com orçamento esgotado, a equipe precisa reduzir risco, corrigir problemas e recuperar confiabilidade.

### Postmortems sem culpa

Postmortems sem culpa procuram entender como a falha aconteceu, não quem pode ser culpado. A pergunta útil é: quais condições técnicas, humanas e organizacionais permitiram o incidente?

Um bom postmortem gera ações concretas. Ele pode mudar um alerta, um trecho de código, um teste, um runbook, uma automação, um processo de release ou uma decisão de arquitetura. Sem ação rastreável, o documento vira apenas registro histórico.

### Automação para reduzir dependência humana

Automação em SRE deve remover repetição e reduzir erro operacional. Um script pode ajudar, mas automação madura é mais que script: ela é segura para repetir, registra o que fez e se integra ao fluxo normal da equipe.

Automatizar uma rotina ruim pode tornar o problema mais rápido, não melhor. Primeiro entenda a causa do trabalho manual; depois automatize o caminho correto.

## Modelo mental

SRE é como uma equipe de manutenção que não apenas conserta falhas. Ela mede desgaste, define limites seguros, troca peças frágeis e melhora o projeto para que o sistema precise de menos intervenção no futuro.

## Cenário realista

Uma API de pagamentos exige acompanhamento manual em quase todo deploy. Quando algo falha, o alerta chega tarde e a investigação depende de uma pessoa específica. Esse cenário mistura risco de mudança, poucos sinais de diagnóstico e toil.

A equipe começa definindo dois SLIs: taxa de sucesso das transações e latência de autorização. Em seguida cria um SLO inicial para cada indicador, revisa alertas, documenta um runbook para falhas conhecidas, automatiza rollback e transforma incidentes em postmortems com ações rastreáveis. O resultado esperado não é perfeição imediata, mas redução progressiva de trabalho manual e decisões mais claras sobre risco.

## Visão sistêmica

```mermaid
flowchart LR
    Change[Mudanças] --> Risk[Risco]
    Risk --> SLI[SLI mede experiência]
    SLI --> SLO[SLO define meta]
    SLO --> Budget[Error budget]
    Budget --> Decision{Há orçamento?}
    Decision -->|Sim| Release[Release controlado]
    Decision -->|Não| Stabilize[Estabilizar serviço]
    Stabilize --> Engineering[Automação e correção de causa raiz]
    Engineering --> SLO
```

## Mapa visual de estudo

```mermaid
flowchart TB
    SRE[SRE] --> SLI[SLI]
    SLI --> SLO[SLO]
    SRE --> Toil[Toil]
    SRE --> Automation[Automação]
    SLO --> Budget[Error budget]
    Budget --> Releases[Decisões de release]
    Toil --> Engineering[Tempo para engenharia]
    Incidents[Incidentes] --> Postmortems[Postmortems sem culpa]
    Postmortems --> Engineering
    Automation --> LessToil[Menos trabalho manual]
```

## Exemplo guiado

Imagine que a equipe reinicia manualmente workers travados várias vezes por semana.

1. Classifique a atividade como toil.
2. Meça frequência, duração e impacto.
3. Investigue a causa: bug, falta de limite, dependência lenta ou configuração.
4. Corrija a causa ou crie recuperação automática segura.
5. Verifique se os acionamentos diminuíram.

O objetivo não é reiniciar mais rápido. O objetivo é tornar o reinício manual desnecessário.

## Erros comuns

- Chamar uma equipe de SRE, mas usá-la apenas como suporte de produção.
- Usar SLO sem definir antes um SLI mensurável.
- Criar SLOs que ninguém usa para tomar decisões.
- Automatizar sintomas sem corrigir causa raiz.
- Usar postmortem para encontrar culpados.
- Ignorar toil porque “sempre foi assim”.

## Aplicando amanhã

- Liste as cinco tarefas operacionais mais repetidas da equipe.
- Escolha um fluxo crítico e defina um SLI simples.
- Identifique um alerta que não exige ação humana imediata.
- Escolha um incidente recente e extraia uma ação preventiva.
- Defina qual tipo de mudança deve parar quando o error budget acabar.

## Mapeamento na indústria

| Prática | Onde aparece |
| --- | --- |
| SLI | Métricas de experiência do usuário, como sucesso, latência e frescor. |
| SLO | Revisões de serviço, dashboards e acordos internos. |
| SLA | Contratos, termos comerciais e compromissos externos. |
| Error budget | Decisões de release e priorização de confiabilidade. |
| Redução de toil | Backlog de plataforma e automação operacional. |
| Postmortem | Gestão de incidentes e melhoria contínua. |
| Automação | CI/CD, ou integração e entrega contínuas; GitOps, que aplica mudanças a partir de repositórios versionados; rollback, runbooks executáveis e correção automática de falhas conhecidas. |

## Relação com DevOps e Kubernetes

SRE e DevOps compartilham a busca por colaboração entre desenvolvimento e operação. DevOps é um conjunto de práticas culturais e técnicas para aproximar quem constrói software de quem opera produção. SRE adiciona uma disciplina explícita de metas, orçamento de risco e responsabilidade operacional.

Em Kubernetes, plataforma usada para executar aplicações em containers, esses conceitos aparecem em probes, que são checagens de saúde; limites de recursos; rollouts, que controlam implantação gradual; métricas; alertas; autoscaling, que ajusta capacidade automaticamente; e políticas de deploy. Kubernetes não entrega confiabilidade sozinho; ele fornece mecanismos que precisam ser usados com bons SLOs, automação e revisão operacional.

## Explicando como se você tivesse 15 anos

SRE é cuidar de um sistema para que ele funcione bem sem depender de alguém consertando tudo manualmente o tempo todo. A equipe mede se o serviço está bom, combina quanto erro é aceitável, automatiza tarefas repetidas e aprende com falhas. Quando algo quebra, a pergunta principal é: como mudamos o sistema para isso não acontecer de novo?

## Perguntas de entrevista

1. O que diferencia SRE de uma equipe tradicional de operações?
2. Por que 100% de disponibilidade quase nunca é a meta correta?
3. Como error budget ajuda a equilibrar release e estabilidade?
4. Como você identificaria toil em uma equipe?
5. O que torna um postmortem útil?

## Exercícios

### Compreensão

Explique SRE em até cinco linhas sem usar a palavra DevOps.

### Aplicação

Escolha um serviço e defina um SLI simples para disponibilidade ou latência.

### Análise

Liste três tarefas repetitivas da operação e indique qual delas deveria virar automação primeiro.

### Avaliação

Escolha um alerta real e avalie se ele deveria acionar uma pessoa imediatamente.

### Criação

Crie uma política curta para o que acontece quando o error budget de um serviço acaba.

## Como isso evoluiu depois de 2016

Depois de 2016, SRE passou a ser aplicado em ambientes com Kubernetes, cloud pública, GitOps, OpenTelemetry e plataformas internas. OpenTelemetry padroniza a coleta de métricas, logs e traces para entender o comportamento de sistemas distribuídos. A essência continua a mesma: medir experiência, controlar risco, reduzir toil e aprender com falhas.

Hoje muitas práticas são expressas como configuração declarativa, pipelines, políticas de plataforma e telemetria padronizada, ou seja, sinais técnicos coletados de forma consistente para análise operacional.

## Recomendação de vídeo

- **Google SRE Video Gallery:** <https://sre.google/resources/videos/>

Por que este recurso é útil? A galeria reúne palestras que mostram como SRE é praticado em serviços reais.

## Leitura complementar

- **Livro oficial online do Google SRE:** <https://sre.google/sre-book/>
- **The Site Reliability Workbook:** <https://sre.google/workbook/>

Por que este recurso é útil? O livro apresenta fundamentos; o workbook ajuda a transformar fundamentos em prática.

## Documentação oficial

- **Kubernetes Documentation:** <https://kubernetes.io/docs/>
- **OpenTelemetry Documentation:** <https://opentelemetry.io/docs/>
- **Prometheus Documentation:** <https://prometheus.io/docs/introduction/overview/>

Por que este recurso é útil? Essas documentações mostram ferramentas modernas usadas para aplicar SRE em ambientes cloud native.

## Recursos visuais

- **Google SRE Resources:** <https://sre.google/resources/>
- **CNCF Landscape:** <https://landscape.cncf.io/>

Por que este recurso é útil? Eles ajudam a visualizar práticas, ferramentas e plataformas relacionadas à confiabilidade.

## Principais aprendizados

- SRE aplica engenharia de software à operação de serviços.
- Confiabilidade precisa de SLIs, SLOs e decisões explícitas.
- Error budget transforma risco em mecanismo de decisão.
- Toil excessivo reduz a capacidade de melhorar o sistema.
- Postmortems sem culpa transformam incidentes em aprendizado.

## Próximo capítulo

Próximo: [Capítulo 02 - O ambiente de produção do Google do ponto de vista de um SRE](capitulo-02.md).

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_risk_slo_page() -> str:
    next_link = next_chapter(chapters[2])
    return f"""# Capítulo 02 - Risco, objetivos de serviço e error budget

## Objetivos de aprendizagem

- Explicar por que confiabilidade absoluta raramente é a meta correta.
- Transformar risco aceito em **SLIs**, **SLOs**, **SLAs** e **error budgets**.
- Usar objetivos de serviço para orientar releases, incidentes e priorização.

## Síntese

**Confiabilidade** é uma decisão econômica, técnica e de produto. Um serviço não precisa ser perfeito; ele precisa ser confiável o suficiente para a expectativa do usuário e para o risco aceito pelo negócio. A disciplina de SRE torna essa conversa objetiva ao medir a experiência real com **SLIs**, definir metas com **SLOs**, separar compromissos externos com **SLAs** e administrar a margem de falha com **error budgets**.

Em uma frase: **risco só vira engenharia quando é medido, aceito explicitamente e conectado a decisões de operação e produto**.

## Por que isso importa

Sem um objetivo mensurável, confiabilidade vira disputa de opinião. Produto pode querer lançar mais rápido, engenharia pode querer estabilizar, suporte pode sentir a dor do usuário e liderança pode cobrar disponibilidade sem dizer quanto risco aceita pagar. **SLOs** resolvem parte dessa tensão porque criam uma linguagem comum: qual experiência importa, qual nível é bom o suficiente e o que acontece quando a margem de erro está acabando.

## Conceitos essenciais

### **Risco administrado**

**Risco administrado** é a decisão explícita de aceitar alguma chance de falha porque eliminar todo risco seria caro, lento ou desnecessário para o usuário. O ponto não é tratar falhas como normais demais; é reconhecer que todo serviço opera dentro de limites econômicos, técnicos e humanos.

Um serviço de busca, uma API de pagamento e um sistema interno de relatórios não precisam do mesmo nível de confiabilidade. A pergunta correta é: qual falha o usuário percebe, qual impacto ela causa e quanto investimento faz sentido para reduzi-la?

### **SLI**

**SLI** é o indicador que mede uma experiência relevante do serviço. Bons SLIs medem comportamento percebido pelo usuário: sucesso de requisição, latência, disponibilidade, durabilidade, frescor de dados ou completude de processamento.

Métricas internas continuam úteis para diagnóstico, mas não substituem o SLI. CPU alta pode explicar um problema; taxa de checkout bem-sucedido mostra se o usuário foi atendido.

### **SLO**

**SLO** é a meta para um SLI em uma janela de tempo. Ele define o que é bom o suficiente. Um SLO de 99,9% em 30 dias é uma decisão diferente de 99,99% em 7 dias, porque muda a margem de erro, a velocidade de reação e o custo de cumprir a promessa.

Um SLO bom precisa ter fonte de dados, janela, método de cálculo, dono e consequência operacional. Sem consequência, o SLO vira decoração de dashboard.

### **SLA**

**SLA** é o compromisso externo, normalmente contratual, com consequências quando a promessa não é cumprida. Ele deve ser tratado com mais cautela que o SLO interno, porque envolve expectativa formal de clientes, suporte, jurídico e negócio.

O erro comum é começar pelo SLA. A equipe deve primeiro entender o comportamento real do serviço, definir SLOs internos saudáveis e só então decidir que promessa externa faz sentido.

### **Error budget**

**Error budget** é a margem de falha permitida pelo SLO. Se a meta é 99,9%, a diferença até 100% é o orçamento que pode ser consumido por incidentes, degradações e mudanças arriscadas dentro da janela.

O valor do error budget está na decisão. Com orçamento saudável, a equipe pode continuar mudando com risco controlado. Com orçamento queimando rápido, releases arriscados devem desacelerar e trabalho de confiabilidade ganha prioridade.

### **Janelas de medição e queima de orçamento**

Janelas curtas mostram incidentes rápidos; janelas longas mostram tendência. Alertar por **burn rate**, ou taxa de queima do orçamento, evita esperar o mês acabar para descobrir que o SLO já ficou irrecuperável.

Na prática, a equipe precisa combinar sinais rápidos para resposta e sinais longos para governança. Um alerta deve acordar alguém quando a queima do orçamento indica impacto real ou risco iminente.

## Aplicação prática

Escolha um serviço e execute uma análise enxuta:

- Defina uma jornada crítica do usuário.
- Escolha 1 ou 2 **SLIs** diretamente ligados a essa jornada.
- Proponha um **SLO** com janela e fonte de dados.
- Calcule o **error budget** aproximado.
- Escreva uma regra simples para quando releases devem desacelerar.

## Diagrama de apoio

```mermaid
flowchart LR
    Usuario["Experiência do usuário"] --> SLI["SLI"]
    SLI --> SLO["SLO"]
    SLO --> Budget["Error budget"]
    Budget --> Decisao{{"Orçamento saudável?"}}
    Decisao -->|Sim| Mudanca["Mudança com risco controlado"]
    Decisao -->|Não| Estabilizar["Priorizar confiabilidade"]
    SLA["SLA"] -. compromisso externo .-> SLO
```

## Erros comuns

- Tratar 100% de disponibilidade como meta padrão.
- Definir **SLIs** a partir do que é fácil medir, não do que o usuário percebe.
- Criar **SLOs** sem consequência prática.
- Confundir **SLA** com objetivo interno de engenharia.
- Usar **error budget** como desculpa para descuido, e não como limite de risco.

## Perguntas para revisão

1. Qual experiência do usuário mais precisa de um SLI no seu serviço?
2. O SLO atual, se existir, muda alguma decisão de release ou priorização?
3. O que a equipe faria se metade do error budget fosse consumida nos primeiros dias da janela?

## Exercícios

### Compreensão

Explique a diferença entre **SLI**, **SLO**, **SLA** e **error budget** usando uma API real ou imaginária.

### Aplicação

Crie um SLO inicial para uma jornada crítica e descreva a fonte de dados usada para medi-lo.

### Análise

Liste duas situações em que aumentar a confiabilidade pode não ser o melhor investimento naquele momento.

## Relação com práticas atuais

Hoje, SLOs aparecem em plataformas internas, revisões de arquitetura, alertas por burn rate, políticas de rollout e relatórios de confiabilidade. A prática moderna é começar pequeno: poucos SLIs bons, SLOs ligados à jornada do usuário e decisões claras quando o orçamento de erro está em risco.

## Recursos complementares

- **Google SRE Book - Embracing Risk:** <https://sre.google/sre-book/embracing-risk/>
- **Google SRE Book - Service Level Objectives:** <https://sre.google/sre-book/service-level-objectives/>
- **Site Reliability Workbook - Implementing SLOs:** <https://sre.google/workbook/implementing-slos/>
- **Site Reliability Workbook - Alerting on SLOs:** <https://sre.google/workbook/alerting-on-slos/>

## Fechamento

Guarde a ideia principal: **SLOs transformam risco aceito em uma regra operacional para equilibrar velocidade e estabilidade**.

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Embracing Risk**. <https://sre.google/sre-book/embracing-risk/>
- Google SRE. **Service Level Objectives**. <https://sre.google/sre-book/service-level-objectives/>
- Google SRE. **Implementing SLOs**. <https://sre.google/workbook/implementing-slos/>
- Google SRE. **Alerting on SLOs**. <https://sre.google/workbook/alerting-on-slos/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_automation_release_page() -> str:
    next_link = next_chapter(chapters[6])
    return f"""# Capítulo 05 - Automação operacional e engenharia de release

## Objetivos de aprendizagem

- Explicar como **automação confiável** reduz trabalho manual e risco de mudança.
- Relacionar estado desejado, builds reprodutíveis, configuração, rollout e rollback.
- Avaliar se um pipeline de release é auditável, repetível e seguro para produção.

## Síntese

Automação em SRE não é apenas escrever scripts. O objetivo é transformar intenção operacional em sistemas que validam pré-condições, executam mudanças de forma repetível, observam resultado e permitem recuperação. **Engenharia de release** aplica o mesmo raciocínio ao caminho até produção: builds reprodutíveis, artefatos versionados, configuração controlada, rollouts graduais e rollback claro.

Em uma frase: **automação e release engineering formam a cadeia que leva mudanças para produção com controle, evidência e reversibilidade**.

## Por que isso importa

Grande parte dos incidentes nasce em mudança: deploy, configuração, migração, dependência, capacidade ou rotina operacional executada de forma diferente do esperado. Automação confiável reduz variação humana; engenharia de release reduz ambiguidade sobre o que foi construído, testado, implantado e revertido.

## Conceitos essenciais

### **Automação idempotente**

**Automação idempotente** é segura para repetir. Se uma rotina falha no meio e precisa rodar de novo, ela não deve duplicar efeito, corromper estado ou depender de memória humana para saber onde parou.

Esse princípio vale para scripts, controladores, jobs, runbooks executáveis, migrações e correções automáticas.

### **Estado desejado**

**Estado desejado** descreve como o sistema deve estar. Automação madura compara estado atual com estado desejado, calcula a diferença e reconcilia o ambiente. Essa lógica aparece em controladores Kubernetes, GitOps, infraestrutura como código e plataformas internas.

O ganho é reduzir passos manuais e tornar a operação mais auditável: a pergunta deixa de ser "quem clicou onde?" e passa a ser "qual estado declaramos e o que reconciliou?".

### **Builds reprodutíveis**

**Builds reprodutíveis** reduzem surpresa entre desenvolvimento, teste e produção. Entradas devem ser declaradas, dependências devem ser controladas e o artefato promovido precisa ser rastreável.

Sem isso, a equipe não sabe se está implantando o que testou. Investigar incidentes também fica mais difícil porque o artefato real pode depender de estado externo ou passos não registrados.

### **Separação entre construir, configurar e implantar**

Construir software, configurar comportamento e implantar em produção são decisões diferentes. Misturar tudo em um processo opaco aumenta risco: uma mudança simples de configuração pode virar build nova; um deploy pode carregar parâmetro inesperado; um rollback pode voltar código mas manter configuração quebrada.

Separar essas etapas melhora revisão, auditoria e recuperação.

### **Rollout, canário e rollback**

**Rollout** é a liberação gradual de uma mudança. **Canário** limita exposição inicial para detectar regressões com menor impacto. **Rollback** precisa ser exercitado antes da crise, não descoberto durante o incidente.

Essas práticas dependem de sinais confiáveis: taxa de erro, latência, saturação, eventos de negócio e feedback de usuários. Sem observabilidade da mudança, rollout gradual vira apenas deploy lento.

### **Observabilidade da mudança**

Toda automação que muda produção precisa deixar rastros: quem pediu, qual versão, qual configuração, quais validações passaram, qual impacto foi observado e como reverter. Logs, métricas, traces, eventos de deploy e anotações em dashboards ajudam a conectar causa e efeito.

## Aplicação prática

Escolha um pipeline ou rotina operacional e revise:

- O artefato é versionado e rastreável?
- As entradas da build são declaradas?
- Configuração e código podem ser revertidos separadamente?
- O rollout tem fases e critérios objetivos?
- O rollback foi testado recentemente?
- A automação registra o que fez e expõe falhas?

## Diagrama de apoio

```mermaid
flowchart LR
    Intent["Intenção"] --> Build["Build reprodutível"]
    Build --> Artifact["Artefato versionado"]
    Artifact --> Config["Configuração controlada"]
    Config --> Rollout["Rollout gradual"]
    Rollout --> Signals["Sinais de saúde"]
    Signals --> Decision{{"Promover ou reverter?"}}
    Decision -->|Promover| Prod["Produção ampliada"]
    Decision -->|Reverter| Rollback["Rollback"]
```

## Erros comuns

- Confundir script com automação confiável.
- Automatizar uma rotina ruim sem entender causa e pré-condições.
- Depender de uma pessoa para construir, promover ou reverter releases.
- Misturar build, configuração e deploy em um processo sem rastreabilidade.
- Fazer canário sem métrica que indique sucesso ou falha.

## Perguntas para revisão

1. Qual parte do caminho para produção ainda depende de ação manual frágil?
2. O rollback atual reverte código, configuração e dados na ordem correta?
3. Que sinal provaria que um rollout deve parar antes de atingir todos os usuários?

## Exercícios

### Compreensão

Explique por que automação idempotente é diferente de "script que roda rápido".

### Aplicação

Desenhe o caminho de uma mudança desde commit até produção e marque onde há validação, aprovação, rollout e rollback.

### Análise

Escolha um incidente causado por mudança e identifique qual etapa da cadeia deveria ter detectado ou limitado o impacto.

## Relação com práticas atuais

Em ambientes modernos, essa cadeia aparece em CI/CD, GitOps, Kubernetes, infraestrutura como código, feature flags, canários, progressive delivery, SBOMs e assinatura de artefatos. A tecnologia muda, mas o princípio permanece: mudanças confiáveis precisam ser pequenas, rastreáveis, observáveis e reversíveis.

## Recursos complementares

- **Google SRE Book - The Evolution of Automation at Google:** <https://sre.google/sre-book/automation-at-google/>
- **Google SRE Book - Release Engineering:** <https://sre.google/sre-book/release-engineering/>
- **Site Reliability Workbook - Canarying Releases:** <https://sre.google/workbook/canarying-releases/>

## Fechamento

Guarde a ideia principal: **boa automação expressa intenção e engenharia de release torna a mudança segura para chegar a produção**.

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **The Evolution of Automation at Google**. <https://sre.google/sre-book/automation-at-google/>
- Google SRE. **Release Engineering**. <https://sre.google/sre-book/release-engineering/>
- Google SRE. **Canarying Releases**. <https://sre.google/workbook/canarying-releases/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_alerting_oncall_page() -> str:
    next_link = next_chapter(chapters[9])
    return f"""# Capítulo 07 - Alertas acionáveis e plantão saudável

## Objetivos de aprendizagem

- Explicar como **alertas acionáveis** determinam a qualidade do **plantão**.
- Diferenciar página urgente, ticket, dashboard e investigação assíncrona.
- Projetar uma rotina de plantão sustentável, com runbooks, escalonamento e carga manejável.

## Síntese

Alertas e plantão não são práticas independentes. Um alerta ruim interrompe pessoas, reduz confiança no sistema de monitoração e degrada a qualidade da resposta. Um plantão saudável depende de sinais que representem impacto real, regras bem modeladas, documentação útil, volume suportável e segurança para tomar decisões em produção.

Em uma frase: **alertas só devem acordar pessoas quando exigem julgamento humano imediato, e o plantão precisa ser desenhado para responder bem sem destruir a equipe**.

## Por que isso importa

Equipes não falham apenas por falta de métricas; elas falham porque são interrompidas por sinais ruins, sem contexto, sem runbook e sem critério de urgência. A consequência é fadiga de alerta, resposta lenta, decisões defensivas e perda de confiança. SRE trata detecção e plantão juntos porque a experiência operacional começa no sinal que chama uma pessoa.

## Conceitos essenciais

### **Séries temporais**

**Séries temporais** registram valores ao longo do tempo: latência, erros, tráfego, saturação, filas, idade de dados ou taxa de sucesso. Elas são a base de muitos alertas porque permitem observar tendência, taxa e mudança de comportamento.

Um valor instantâneo raramente basta. Regras úteis consideram janela, agregação, taxa de variação e impacto para o usuário.

### **Alertas acionáveis**

**Alertas acionáveis** exigem ação humana imediata e clara. Se a notificação não muda uma decisão naquele momento, ela não deve paginar alguém; deve virar ticket, dashboard, relatório ou investigação assíncrona.

A pergunta prática é simples: "quem recebe esse alerta sabe o que fazer agora?". Se a resposta for não, o alerta ainda não está pronto.

### **Página, ticket e dashboard**

Nem todo sinal tem a mesma urgência. **Página** é interrupção imediata. **Ticket** é trabalho que precisa ser planejado. **Dashboard** é apoio para análise. Misturar esses canais destrói prioridade.

Separar canais preserva atenção humana para problemas que realmente precisam de julgamento durante a janela de impacto.

### **Qualidade dos alertas**

Qualidade de alerta envolve precisão, contexto, runbook, dono, severidade e relação com SLO. Um alerta bom descreve impacto, escopo provável, primeiro diagnóstico e caminho de mitigação.

Alertas devem ser revisados como código operacional. Se um alerta dispara muito e não gera ação útil, ele está ensinando a equipe a ignorar o sistema.

### **Plantão sustentável**

**Plantão sustentável** equilibra volume, complexidade, treinamento, remuneração ou reconhecimento, segurança psicológica e tempo de recuperação. A escala não pode depender de heroísmo contínuo.

Um rodízio saudável tem carga previsível, handoff claro, apoio de escalonamento e critérios para tirar uma pessoa da linha de frente quando a pressão acumulada fica alta.

### **Runbooks e escalonamento**

**Runbooks** reduzem incerteza inicial: o que verificar, onde olhar, como mitigar, quando escalar e quais riscos evitar. **Escalonamento** define quando envolver especialistas, liderança, suporte ou times dependentes.

Runbook bom não substitui pensamento. Ele remove passos repetitivos para que a pessoa possa usar julgamento onde ele realmente importa.

## Aplicação prática

Escolha os dez alertas que mais interromperam a equipe nas últimas semanas:

- Classifique cada um como página, ticket, dashboard ou remoção.
- Verifique se cada página tem impacto de usuário ou risco claro de SLO.
- Adicione dono, runbook, severidade e primeiro passo de mitigação.
- Meça páginas por turno e interrupções fora do horário esperado.
- Defina uma regra para revisar alertas ruidosos após incidentes ou semanas ruins de plantão.

## Diagrama de apoio

```mermaid
flowchart LR
    Signal["Sinal operacional"] --> Rule["Regra de alerta"]
    Rule --> Decision{{"Exige ação imediata?"}}
    Decision -->|Sim| Page["Página de plantão"]
    Decision -->|Não| Async["Ticket / dashboard"]
    Page --> Runbook["Runbook"]
    Runbook --> Mitigate["Mitigação"]
    Mitigate --> Review["Revisão do alerta"]
    Review --> Rule
```

## Erros comuns

- Acordar pessoas por sintomas sem impacto real ou risco iminente.
- Criar alertas sem dono, runbook ou critério de severidade.
- Usar o mesmo canal para urgência, melhoria planejada e curiosidade operacional.
- Medir plantão apenas por cobertura, sem medir carga e qualidade das interrupções.
- Aceitar fadiga de alerta como custo inevitável de operar produção.

## Perguntas para revisão

1. Quais alertas atuais realmente exigem julgamento humano imediato?
2. Qual volume de páginas por turno ainda é sustentável para a equipe?
3. Que informação mínima precisa aparecer em uma página para acelerar a mitigação?

## Exercícios

### Compreensão

Explique a diferença entre página, ticket e dashboard usando exemplos de produção.

### Aplicação

Reescreva um alerta ruidoso para incluir impacto, condição, janela, severidade, dono e runbook.

### Análise

Avalie um rodízio de plantão e identifique o maior risco: excesso de volume, falta de prática, falta de runbook, escalonamento confuso ou ausência de recuperação.

## Relação com práticas atuais

Em ambientes modernos, alertas costumam ser ligados a SLOs, burn rate, sintomas de usuário, traces, logs e eventos de deploy. Ferramentas de incident management ajudam com escalonamento e calendário, mas a saúde do plantão ainda depende de disciplina editorial nos alertas: poucas páginas, alto sinal, contexto claro e revisão contínua.

## Recursos complementares

- **Google SRE Book - Practical Alerting:** <https://sre.google/sre-book/practical-alerting/>
- **Google SRE Book - Being On-Call:** <https://sre.google/sre-book/being-on-call/>
- **Site Reliability Workbook - On-Call:** <https://sre.google/workbook/on-call/>
- **Site Reliability Workbook - Alerting on SLOs:** <https://sre.google/workbook/alerting-on-slos/>
- **OpenTelemetry Signals:** <https://opentelemetry.io/docs/concepts/signals/>

## Fechamento

Guarde a ideia principal: **a qualidade do plantão começa na qualidade do alerta que interrompe a pessoa**.

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Practical Alerting from Time-Series Data**. <https://sre.google/sre-book/practical-alerting/>
- Google SRE. **Being On-Call**. <https://sre.google/sre-book/being-on-call/>
- Google SRE. **On-Call**. <https://sre.google/workbook/on-call/>
- Google SRE. **Alerting on SLOs**. <https://sre.google/workbook/alerting-on-slos/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_incident_response_page() -> str:
    next_link = next_chapter(chapters[12])
    return f"""# Capítulo {display_number(13):02d} - Resposta a incidentes e aprendizado operacional

## Objetivos de aprendizagem

- Explicar como **prontidão**, **coordenação** e **postmortem sem culpa** formam um ciclo único.
- Definir papéis, comunicação e documentação para incidentes severos.
- Transformar falhas em melhorias rastreáveis de confiabilidade.

## Síntese

Incidentes não começam no momento em que alguém é acordado. A qualidade da resposta depende de treinamento, runbooks, histórico de falhas, simulações, papéis claros e comunicação preparada. Durante a crise, **comando de incidente**, delegação e um documento vivo reduzem ambiguidade. Depois da mitigação, **postmortems sem culpa** convertem o evento em aprendizado, ações corretivas e memória operacional.

Em uma frase: **resposta a incidentes é um ciclo de preparação, coordenação e aprendizado, não apenas reação durante a crise**.

## Por que isso importa

Sem processo explícito, incidentes viram improviso. Pessoas competentes podem trabalhar em paralelo, repetir diagnóstico, comunicar mensagens conflitantes ou aplicar correções arriscadas sem visão comum. A disciplina de SRE reduz esse caos ao tornar visíveis o estado do incidente, as decisões tomadas, os donos de cada frente e as ações que impedem recorrência.

## Conceitos essenciais

### **Prontidão antes da crise**

**Prontidão operacional** combina runbooks, treinamento, simulações, revisão de incidentes anteriores e perguntas do tipo "e se?". A equipe não precisa prever todos os modos de falha, mas precisa treinar como pensar sob pressão.

Uma boa preparação reduz tempo de triagem e evita que a primeira decisão relevante aconteça no pior momento possível.

### **Resposta a emergência**

**Resposta a emergência** prioriza mitigação, segurança do serviço e redução de impacto. A causa raiz pode esperar quando usuários estão afetados; o primeiro objetivo é estabilizar o sistema de forma controlada.

Correções emergenciais devem ser registradas. Sem registro, a mitigação vira uma mudança invisível que pode gerar novo risco depois.

### **Comando de incidente**

**Comando de incidente** separa coordenação de execução técnica. Uma pessoa mantém visão do estado geral, define prioridades, remove bloqueios e garante comunicação. Outras pessoas investigam, mitigam, comunicam com stakeholders ou acompanham métricas.

Essa separação impede que todos tentem resolver o mesmo problema enquanto ninguém cuida da coordenação.

### **Comunicação durante crise**

**Comunicação de incidente** precisa ser objetiva: impacto, escopo, ações em andamento, próximos marcos e nível de incerteza. Mensagens claras reduzem pressão externa e ajudam equipes dependentes a tomar decisões.

Comunicação boa não exige certeza absoluta. Ela exige honestidade sobre o que se sabe, o que ainda está sendo investigado e quando haverá nova atualização.

### **Documento vivo**

Um **documento vivo de incidente** registra linha do tempo, hipóteses, comandos executados, decisões, donos e próximos passos. Ele reduz perda de contexto em handoffs e serve como base para o postmortem.

O documento não deve virar burocracia paralela. Ele precisa ajudar a operação em tempo real.

### **Postmortem sem culpa**

**Postmortem sem culpa** investiga condições sistêmicas, não culpados. O foco é entender por que as decisões pareciam razoáveis no momento, quais sinais estavam ausentes e quais defesas falharam.

A saída concreta deve incluir ações corretivas com dono, prazo e critério de conclusão. Sem isso, o postmortem vira narrativa, não melhoria.

## Aplicação prática

Escolha um incidente recente ou simulado e execute uma revisão curta:

- Defina quando o incidente deveria ter sido declarado.
- Liste os papéis mínimos: comando, investigação, comunicação e registro.
- Recrie uma linha do tempo com eventos, decisões e mudanças.
- Identifique uma lacuna de prontidão que poderia ser treinada antes da próxima crise.
- Escreva duas ações corretivas com dono e evidência de conclusão.

## Diagrama de apoio

```mermaid
flowchart LR
    Prep["Prontidão"] --> Detect["Detecção"]
    Detect --> Declare["Declaração do incidente"]
    Declare --> Command["Comando e papéis"]
    Command --> Mitigate["Mitigação"]
    Mitigate --> Learn["Postmortem sem culpa"]
    Learn --> Actions["Ações corretivas"]
    Actions --> Prep
```

## Erros comuns

- Declarar incidente tarde demais por medo de "exagerar".
- Fazer todos investigarem tecnicamente sem alguém coordenando.
- Comunicar certeza quando ainda há hipótese.
- Escrever postmortem sem ações rastreáveis.
- Tratar culpa individual como substituto de correção sistêmica.

## Perguntas para revisão

1. Quais sinais indicam que um problema deve virar incidente formal?
2. Quem coordena, quem investiga e quem comunica durante uma crise severa?
3. Como a equipe prova que um postmortem reduziu risco real?

## Exercícios

### Compreensão

Explique a diferença entre mitigação, resolução definitiva e ação corretiva de postmortem.

### Aplicação

Crie um template mínimo de documento vivo para incidentes com linha do tempo, papéis, impacto, decisões e próximos passos.

### Análise

Escolha um incidente conhecido e identifique qual parte do ciclo falhou: prontidão, detecção, coordenação, mitigação ou aprendizado.

## Relação com práticas atuais

Ferramentas modernas de incident management, status pages, chatops e automação de escalonamento ajudam, mas a confiabilidade continua dependendo de papéis claros, comunicação disciplinada e aprendizado rastreável. Em organizações maduras, postmortems alimentam backlog de confiabilidade, testes de falha, ajustes de SLO e treinamento de plantão.

## Recursos complementares

- **Google SRE Book - Emergency Response:** <https://sre.google/sre-book/emergency-response/>
- **Google SRE Book - Managing Incidents:** <https://sre.google/sre-book/managing-incidents/>
- **Google SRE Book - Postmortem Culture:** <https://sre.google/sre-book/postmortem-culture/>
- **Site Reliability Workbook - Incident Response:** <https://sre.google/workbook/incident-response/>
- **Site Reliability Workbook - Postmortem Culture:** <https://sre.google/workbook/postmortem-culture/>

## Fechamento

Guarde a ideia principal: **incidentes melhoram a organização quando a resposta é coordenada e o aprendizado vira mudança verificável**.

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Emergency Response**. <https://sre.google/sre-book/emergency-response/>
- Google SRE. **Managing Incidents**. <https://sre.google/sre-book/managing-incidents/>
- Google SRE. **Postmortem Culture**. <https://sre.google/sre-book/postmortem-culture/>
- Google SRE. **Incident Response**. <https://sre.google/workbook/incident-response/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_load_balancing_page() -> str:
    next_link = next_chapter(chapters[18])
    return f"""# Capítulo {display_number(19):02d} - Distribuição de carga na borda e no datacenter

## Objetivos de aprendizagem

- Explicar como **balanceamento de carga** protege experiência do usuário e capacidade interna.
- Relacionar borda, entrada de tráfego, backends, saúde e topologia.
- Avaliar decisões de roteamento com base em latência, capacidade, falha e sobrecarga.

## Síntese

Distribuição de carga não é apenas dividir requisições igualmente. Na borda, o sistema precisa levar usuários a pontos de entrada saudáveis, próximos e capazes. Dentro do datacenter, clientes e proxies precisam escolher backends considerando saúde, custo, conexões, subconjuntos e sinais de saturação. O objetivo é usar capacidade disponível sem concentrar risco em uma região, VIP, proxy ou conjunto pequeno de instâncias.

Em uma frase: **balanceamento confiável direciona tráfego para destinos saudáveis, próximos e capazes, da borda aos backends internos**.

## Por que isso importa

Uma requisição real atravessa várias decisões de roteamento. Se a borda ignora falha regional, usuários continuam indo para um destino ruim. Se o balanceamento interno ignora saúde ou saturação, o sistema amplifica latência, erros e cascatas. A confiabilidade melhora quando cada camada conhece seus sinais e limita o impacto de destinos degradados.

## Conceitos essenciais

### **Balanceamento global**

**Balanceamento global** decide para onde enviar usuários antes de a requisição entrar no serviço. DNS, anycast, endereços virtuais e proxies globais podem considerar proximidade, disponibilidade regional, capacidade e políticas de failover.

O objetivo não é achar o caminho perfeito para cada requisição; é evitar decisões obviamente ruins em escala.

### **Entrada de tráfego**

Pontos de entrada como **VIPs**, load balancers e proxies precisam absorver volume, terminar conexões, aplicar políticas e encaminhar tráfego sem se tornarem gargalos invisíveis.

Falhas nessa camada costumam parecer falha total do serviço, mesmo quando os backends estão saudáveis.

### **Saúde e capacidade**

**Sinais de saúde** indicam se um destino pode receber tráfego. **Sinais de capacidade** indicam quanto tráfego ele deve receber. Um backend vivo pode estar lento, saturado ou incapaz de atender uma classe específica de requisição.

Balanceamento maduro usa esses sinais para reduzir exposição, não apenas para remover instâncias mortas.

### **Subconjuntos de backends**

**Subconjuntos** reduzem custo de conexão e complexidade quando há muitos backends. Em vez de cada cliente falar com todos, cada cliente escolhe um conjunto limitado e bem distribuído.

Subconjuntos mal desenhados podem concentrar carga. A escolha precisa preservar diversidade suficiente para resistir a falhas.

### **Políticas de escolha**

Round robin, pesos, least-loaded e políticas adaptativas são ferramentas. A escolha correta depende de custo por requisição, variância de latência, precisão dos sinais e risco de reação exagerada.

Políticas muito reativas podem oscilar. Políticas muito estáticas podem manter tráfego em destinos ruins.

### **Interação com sobrecarga**

Balanceamento e sobrecarga estão ligados. Quando uma camada tenta "fugir" de instâncias lentas sem limites, pode empurrar carga para destinos ainda saudáveis e derrubá-los também.

Por isso, decisões de roteamento precisam conversar com throttling, prioridades, rejeição explícita e degradação.

## Aplicação prática

Desenhe o caminho de uma requisição crítica:

- Identifique decisões de roteamento na borda, entre regiões e dentro do datacenter.
- Liste quais sinais de saúde e capacidade cada camada usa.
- Verifique se uma região degradada deixa de receber tráfego automaticamente.
- Avalie se clientes internos falam com todos os backends ou com subconjuntos.
- Defina o comportamento esperado quando metade dos backends fica lenta.

## Diagrama de apoio

```mermaid
flowchart LR
    User["Usuário"] --> Edge["Borda / DNS / Anycast"]
    Edge --> Region["Região saudável"]
    Region --> Entry["VIP / proxy de entrada"]
    Entry --> Pool["Pool de backends"]
    Pool --> Subset["Subconjunto"]
    Subset --> Backend["Backend escolhido"]
    Health["Saúde e capacidade"] -. ajusta .-> Edge
    Health -. ajusta .-> Pool
```

## Erros comuns

- Balancear apenas por quantidade de requisições, ignorando custo e latência.
- Remover instâncias somente quando estão mortas, não quando estão degradadas.
- Criar pools de conexão amplos demais sem necessidade.
- Deixar failover regional depender de intervenção manual.
- Usar política adaptativa sem entender oscilação e realimentação.

## Perguntas para revisão

1. Qual camada decide o primeiro destino de uma requisição de usuário?
2. Que sinal remove ou reduz tráfego para um backend lento, mas ainda vivo?
3. Como o balanceamento evita transformar degradação parcial em falha ampla?

## Exercícios

### Compreensão

Explique a diferença entre balanceamento na borda e balanceamento interno entre backends.

### Aplicação

Mapeie um serviço real e indique onde existem DNS, VIPs, proxies, pools e políticas de escolha.

### Análise

Descreva o que aconteceria se uma região ficasse com latência alta, mas sem falhar completamente.

## Relação com práticas atuais

Em ambientes cloud native, essas decisões aparecem em load balancers gerenciados, service mesh, ingress controllers, gateways globais, health checks, circuit breakers e políticas de roteamento por região. A tecnologia varia, mas a pergunta central permanece: cada camada sabe para onde enviar tráfego quando parte do sistema degrada?

## Recursos complementares

- **Google SRE Book - Load Balancing at the Frontend:** <https://sre.google/sre-book/load-balancing-frontend/>
- **Google SRE Book - Load Balancing in the Datacenter:** <https://sre.google/sre-book/load-balancing-datacenter/>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>
- **Google Cloud Architecture Framework:** <https://docs.cloud.google.com/architecture/framework>

## Fechamento

Guarde a ideia principal: **distribuição de carga é uma sequência de decisões de confiabilidade, não apenas um algoritmo de divisão de tráfego**.

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Load Balancing at the Frontend**. <https://sre.google/sre-book/load-balancing-frontend/>
- Google SRE. **Load Balancing in the Datacenter**. <https://sre.google/sre-book/load-balancing-datacenter/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_overload_cascading_page() -> str:
    next_link = next_chapter(chapters[20])
    return f"""# Capítulo {display_number(21):02d} - Sobrecarga, retentativas e falhas em cascata

## Objetivos de aprendizagem

- Explicar como **sobrecarga** pode evoluir para **falha em cascata**.
- Aplicar limites, throttling, prioridades, timeouts, backoff e jitter.
- Projetar degradação explícita para proteger dependências críticas.

## Síntese

Sobrecarga acontece quando a demanda real supera a capacidade útil do sistema. Falhas em cascata acontecem quando respostas locais a esse problema, como retries agressivos, filas sem limite e clientes insistentes, empurram mais carga para dependências já degradadas. SRE trata esses temas juntos porque a prevenção depende de limites claros, rejeição explícita, prioridades, timeouts coerentes, **backoff com jitter** e degradação elegante.

Em uma frase: **um sistema confiável rejeita, reduz ou degrada trabalho antes que a sobrecarga derrube dependências em cadeia**.

## Por que isso importa

Capacidade não é apenas queries por segundo. Duas requisições podem ter custos muito diferentes; um cliente pode consumir recursos desproporcionais; uma fila pode esconder saturação até ser tarde demais. Quando cada componente tenta se salvar sozinho, o efeito combinado pode derrubar o ecossistema inteiro.

## Conceitos essenciais

### **Capacidade real**

**Capacidade real** considera CPU, memória, I/O, conexões, locks, filas, dependências e custo por tipo de requisição. Um serviço pode parecer saudável em média e ainda falhar para uma jornada crítica.

Medir apenas volume costuma esconder saturação. É preciso observar utilização, latência, erros, fila e custo por cliente ou operação.

### **Limites e throttling**

**Limites** definem quanto trabalho será aceito. **Throttling** reduz ou bloqueia demanda antes que o serviço colapse. Esses mecanismos protegem o sistema e tornam o fracasso explícito.

Rejeitar carga de forma controlada é melhor do que aceitar tudo e falhar lentamente para todos.

### **Prioridades**

Nem todo tráfego tem a mesma importância. **Prioridades** permitem preservar operações críticas quando recursos ficam escassos. Requisições administrativas, recomputações, tarefas em lote e fluxos de usuário podem receber tratamentos diferentes.

Sem prioridade, o sistema pode gastar capacidade salvando trabalho secundário enquanto a experiência principal degrada.

### **Retries, backoff e jitter**

**Retries** recuperam falhas transitórias, mas também podem amplificar carga. **Backoff exponencial** aumenta o intervalo entre tentativas; **jitter** espalha as tentativas para evitar ondas sincronizadas.

Retries sem orçamento, sem deadline e sem jitter são uma causa clássica de cascata.

### **Timeouts e filas**

**Timeouts** limitam espera; filas absorvem variação. Os dois precisam ser dimensionados com cuidado. Timeout longo demais prende recursos; curto demais gera retries desnecessários. Fila sem limite transforma atraso em explosão de trabalho acumulado.

O objetivo é falhar cedo quando continuar esperando piora a saúde geral.

### **Degradação elegante**

**Degradação elegante** preserva partes essenciais do serviço quando dependências ou capacidade não estão saudáveis. Exemplos incluem reduzir qualidade de resposta, desativar recursos secundários, servir cache, limitar recomendações ou pausar processamento não crítico.

Degradação deve ser planejada antes do incidente. Improvisar o que desligar durante a crise aumenta risco.

## Aplicação prática

Revise uma dependência crítica do serviço:

- Liste clientes, tipos de requisição e custo aproximado de cada operação.
- Defina limites por cliente ou por classe de tráfego.
- Verifique se retries têm deadline, backoff e jitter.
- Identifique filas sem limite ou sem métrica de idade.
- Escolha um modo de degradação que preserve a jornada principal do usuário.

## Diagrama de apoio

```mermaid
flowchart LR
    Demand["Demanda"] --> Limit["Limites e prioridades"]
    Limit -->|Aceita| Service["Serviço"]
    Limit -->|Rejeita| FailFast["Falha explícita"]
    Service --> Dependency["Dependência"]
    Dependency -->|Erro/lentidão| Retry["Retry com backoff e jitter"]
    Retry --> Limit
    Service --> Degrade["Degradação elegante"]
```

## Erros comuns

- Medir capacidade apenas por QPS médio.
- Fazer retry sem deadline, limite ou jitter.
- Usar filas ilimitadas para esconder saturação.
- Tratar todo tráfego como igualmente crítico.
- Preferir falha lenta e global a rejeição rápida e explícita.

## Perguntas para revisão

1. Que comportamento do cliente poderia amplificar uma falha parcial?
2. Qual tráfego deve ser preservado quando o sistema está saturado?
3. Que limite impede um cliente ou job de derrubar uma dependência compartilhada?

## Exercícios

### Compreensão

Explique por que retries podem melhorar disponibilidade em um caso e causar falha em cascata em outro.

### Aplicação

Desenhe uma política de retry com timeout, deadline, backoff, jitter e limite de tentativas.

### Análise

Escolha um fluxo crítico e defina uma estratégia de degradação que mantenha o serviço parcialmente útil.

## Relação com práticas atuais

Esses controles aparecem em API gateways, service mesh, SDKs de clientes, filas, circuit breakers, políticas de rate limit e mecanismos de autoscaling. Autoscaling ajuda, mas não substitui limites: capacidade nova pode chegar tarde, depender de recursos compartilhados ou amplificar custo durante um evento de carga.

## Recursos complementares

- **Google SRE Book - Handling Overload:** <https://sre.google/sre-book/handling-overload/>
- **Google SRE Book - Addressing Cascading Failures:** <https://sre.google/sre-book/addressing-cascading-failures/>
- **Google Cloud Architecture Framework:** <https://docs.cloud.google.com/architecture/framework>
- **AWS Well-Architected Reliability Pillar:** <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html>

## Fechamento

Guarde a ideia principal: **sobrecarga controlada é uma decisão de design; cascata é o preço de deixar cada componente reagir sem limites**.

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Handling Overload**. <https://sre.google/sre-book/handling-overload/>
- Google SRE. **Addressing Cascading Failures**. <https://sre.google/sre-book/addressing-cascading-failures/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def consolidated_scheduling_pipelines_page() -> str:
    next_link = next_chapter(chapters[23])
    return f"""# Capítulo {display_number(24):02d} - Agendamento distribuído e pipelines confiáveis

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

{next_link}

## Referências

- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (eds.). **Site Reliability Engineering: How Google Runs Production Systems**. O'Reilly Media / Google, 2016. <https://sre.google/sre-book/>
- Beyer, B.; Murphy, N. R.; Rensin, D.; Kawahara, K.; Thorne, S. (eds.). **The Site Reliability Workbook**. O'Reilly Media / Google, 2018. <https://sre.google/workbook/>
- Google SRE. **Distributed Periodic Scheduling with Cron**. <https://sre.google/sre-book/distributed-periodic-scheduling/>
- Google SRE. **Data Processing Pipelines**. <https://sre.google/sre-book/data-processing-pipelines/>
- PDF local usado como fonte primária em português: `../Engenharia de Confiabilidade do Google ( etc.).pdf`.
"""


def chapter_page(chapter: dict) -> str:
    concepts = bullets(chapter["concepts"])
    practice = bullets(chapter["practice"])
    first_concept = chapter["concepts"][0]
    summary = student_facing_summary(chapter)
    visible_number = display_number(chapter["number"])
    title = display_title(chapter)
    objectives = bullets([
        "Explicar o problema de confiabilidade tratado pelo tema.",
        "Reconhecer onde o tema aparece em um serviço real.",
        "Aplicar o conceito em uma decisão operacional ou de engenharia.",
    ])
    mistakes = bullets(chapter_specific_mistakes(chapter))
    questions = "\n".join(
        f"{index}. {question}" for index, question in enumerate(review_questions(chapter), start=1)
    )
    return f"""# Capítulo {visible_number:02d} - {title}

## Objetivos de aprendizagem

{objectives}

## Síntese

{summary}

Em uma frase: **{chapter["central"]}**

## Por que isso importa

{why_it_matters(chapter)}

## Conceitos essenciais

{concept_deep_dive(chapter)}

## Aplicação prática

Para evitar burocracia, escolha um serviço concreto e execute uma ação pequena:

{practice}

Depois da ação, procure uma evidência simples de melhoria: menos alertas
irrelevantes, recuperação mais rápida, dependência mais clara, deploy menos
arriscado, métrica mais confiável ou decisão mais fácil de explicar.

{diagram_block(chapter)}## Erros comuns

{mistakes}

## Perguntas para revisão

{questions}

## Exercícios

### Compreensão

Explique a ideia central em até cinco linhas, usando um serviço real como exemplo.

### Aplicação

Escolha um serviço real e execute uma das ações práticas.

### Análise

Liste duas formas de aplicar esse conceito de maneira superficial e explique o
risco de cada uma.

## Relação com práticas atuais

{current_practice(chapter)}

{resources_block(chapter)}
## Fechamento

Guarde a ideia principal: **{chapter["central"]}**

{next_chapter(chapter)}

{references_block(chapter)}
"""


def build_index() -> str:
    by_number = {chapter["number"]: chapter for chapter in chapters}
    sections = []
    for part, nums in PART_NAV.items():
        lines = "\n".join(
            f"- [Capítulo {display_number(number):02d} - {display_title(by_number[number])}](capitulos/{display_slug(number)})"
            for number in nums
        )
        sections.append(f"## {part}\n\n{lines}")

    return f"""# Curso - Engenharia de Confiabilidade

Este repositório MkDocs organiza um material de estudo baseado no livro
**Engenharia de Confiabilidade do Google**. O conteúdo aqui é um resumo
autoral para estudo: não substitui o livro e não reproduz capítulos.

## Como estudar

1. Comece por [Conceitos centrais](conceitos-centrais.md).
2. Leia os capítulos em ordem, observando a seção **Aplicação prática**.
3. Use as perguntas práticas para relacionar o livro a serviços reais.

{chr(10).join(sections).replace(chr(10) + '## ', chr(10) + chr(10) + '## ')}

## Referências

- Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard, eds. **Engenharia de Confiabilidade do Google**. Novatec, 2016.
- Google. **Site Reliability Engineering: How Google Runs Production Systems**. <https://sre.google/sre-book/>.
"""


def build_concepts() -> str:
    return """
    # Conceitos centrais

    Esta página existe como **mapa de referência** do curso. Ela não substitui
    os capítulos; ela ajuda a enxergar como os conceitos se conectam e quais
    decisões cada um melhora em produção.

    Use esta página antes de começar o curso para criar vocabulário comum, e
    volte a ela depois de cada parte para revisar o encadeamento entre risco,
    medição, automação, operação, incidentes, arquitetura e gestão.

    ## Como usar

    Para cada conceito, responda três perguntas:

    - Que decisão operacional ele melhora?
    - Que evidência mostra que ele está funcionando?
    - Que erro comum ele ajuda a evitar?

    ## Mapa de decisões

    | Decisão de confiabilidade | Conceitos que sustentam a decisão | Capítulos |
    | --- | --- | --- |
    | Quanto risco o serviço pode aceitar? | **SLI**, **SLO**, **SLA**, **error budget**, risco administrado | 01, 02 |
    | O que deve acordar uma pessoa? | **quatro sinais de ouro**, **alertas acionáveis**, sintomas, burn rate | 04, 07 |
    | Como reduzir trabalho manual? | **toil**, **automação**, estado desejado, idempotência, release seguro | 03, 05 |
    | Como responder quando produção falha? | **plantão**, troubleshooting, comando de incidente, postmortem sem culpa | 07, 08, 09 |
    | Como evitar amplificação de falhas? | balanceamento, sobrecarga, retries, backoff, jitter, degradação elegante | 13, 14 |
    | Como proteger estado e dados? | consenso distribuído, liderança, workflows, integridade, backup e recuperação | 15, 16, 17 |
    | Como levar mudanças grandes para produção? | testes de confiabilidade, rollouts, feature flags, prontidão de lançamento | 11, 18 |
    | Como sustentar SRE como prática organizacional? | onboarding, interrupções, engajamento, comunicação, responsabilidade compartilhada | 19 a 25 |

    ## Fundamentos

    ### **SRE**

    **SRE** aplica engenharia de software ao trabalho historicamente tratado
    como operação. A equipe não existe apenas para manter sistemas funcionando;
    ela reduz intervenção manual, automatiza rotinas, melhora arquitetura,
    mede comportamento real e cria mecanismos para equilibrar velocidade e
    confiabilidade.

    ### **Confiabilidade como decisão de produto**

    **Confiabilidade** não é busca automática por 100%. O nível correto depende
    de expectativa do usuário, impacto da falha, custo de redução de risco e
    velocidade de evolução desejada. Um serviço interno eventual e uma API de
    pagamento não têm o mesmo alvo.

    ### **SLI, SLO e SLA**

    **SLI** mede uma experiência relevante do serviço. **SLO** define a meta
    para essa medição em uma janela. **SLA** é o compromisso externo, geralmente
    contratual, com consequência quando não é cumprido. A ordem saudável é medir
    bem, definir objetivo interno e só então prometer externamente.

    ### **Error budget**

    **Error budget** é a margem de falha permitida por um SLO. Ele transforma
    confiabilidade em uma regra de decisão: orçamento saudável permite mudança
    com risco controlado; orçamento queimando rápido desloca prioridade para
    estabilização.

    ### **Toil**

    **Toil** é trabalho manual, repetitivo, reativo, sem valor durável e que
    cresce com o serviço. Toil excessivo prende a equipe em operação reativa e
    reduz tempo disponível para engenharia.

    ### **Simplicidade operacional**

    **Simplicidade operacional** reduz estados, dependências, exceções e
    caminhos de falha. Remover complexidade não é estética: é reduzir o número
    de coisas que precisam ser entendidas durante mudança, incidente e
    recuperação.

    ## Operação diária

    ### **Observabilidade e monitoração**

    **Monitoração** transforma sinais de produção em decisão. **Observabilidade**
    amplia a capacidade de investigar sistemas distribuídos usando métricas,
    logs, traces e eventos. O objetivo não é coletar tudo; é criar evidência
    suficiente para detectar impacto e diagnosticar causa.

    ### **Quatro sinais de ouro**

    **Latência**, **tráfego**, **erros** e **saturação** formam uma base prática
    para observar serviços. Eles aproximam a operação da experiência do usuário
    e ajudam a separar sintoma de causa.

    ### **Alertas acionáveis**

    **Alertas acionáveis** exigem julgamento humano imediato. Se uma notificação
    não muda uma decisão agora, ela deve virar ticket, dashboard, automação ou
    análise assíncrona.

    ### **Plantão saudável**

    **Plantão saudável** depende de volume manejável, alertas bons, runbooks,
    escalonamento claro, treinamento e recuperação. Plantão não é apenas uma
    escala de pessoas; é um sistema sociotécnico que precisa ser projetado.

    ### **Troubleshooting**

    **Troubleshooting** eficaz usa triagem, hipóteses testáveis, experimentos
    pequenos e linha do tempo. Resultados negativos são úteis porque reduzem o
    espaço de busca e evitam mudanças aleatórias em produção.

    ## Incidentes e aprendizado

    ### **Resposta a incidentes**

    **Resposta a incidentes** organiza papéis, comunicação, mitigação e registro
    durante uma crise. Separar coordenação de execução técnica reduz caos e
    melhora a qualidade das decisões.

    ### **Postmortem sem culpa**

    **Postmortem sem culpa** investiga condições sistêmicas, não culpados. A
    saída útil é ação corretiva rastreável: dono, prazo e evidência de redução
    de risco.

    ### **Interrupções de serviço**

    **Interrupções** precisam ser registradas, classificadas e analisadas ao
    longo do tempo. Sem linha de base, a equipe não sabe se está melhorando
    confiabilidade ou apenas reagindo ao incidente mais recente.

    ## Arquitetura e mudança

    ### **Automação confiável**

    **Automação confiável** expressa intenção, valida pré-condições, executa de
    forma idempotente, observa resultado e permite recuperação. Script rápido
    não é suficiente quando o efeito em produção não é rastreável.

    ### **Engenharia de release**

    **Engenharia de release** torna mudanças pequenas, rastreáveis, testáveis e
    reversíveis. Builds reprodutíveis, artefatos versionados, configuração
    controlada, rollout gradual e rollback exercitado reduzem surpresa.

    ### **Balanceamento de carga**

    **Balanceamento de carga** direciona tráfego para destinos saudáveis,
    próximos e capazes. A decisão acontece em camadas: borda, região, proxy,
    pool e backend.

    ### **Sobrecarga e falhas em cascata**

    **Sobrecarga** deve ser controlada com limites, throttling, prioridades e
    rejeição explícita. **Falhas em cascata** aparecem quando retries, filas,
    timeouts ruins e dependências lentas amplificam uma falha parcial.

    ### **Consenso distribuído**

    **Consenso distribuído** coordena estado crítico quando decisões
    conflitantes seriam perigosas: eleição de líder, locks, configuração,
    filas confiáveis e máquinas de estado replicadas.

    ### **Workflows e pipelines**

    **Workflows confiáveis** têm estado visível, liderança ou coordenação,
    idempotência, tratamento de atraso, controle de duplicidade e validação de
    resultado. Jobs periódicos e pipelines falham de formas parecidas.

    ### **Integridade de dados**

    **Integridade de dados** exige prevenção, detecção, replicação, backup e
    restauração testada. Backup sem recuperação verificável é apenas esperança.

    ## Gestão de SRE

    ### **Prontidão para produção**

    **Prontidão para produção** combina arquitetura, capacidade, observabilidade,
    runbooks, rollback, modos de falha, suporte e critérios de lançamento.

    ### **Responsabilidade compartilhada**

    **Responsabilidade compartilhada** impede que SRE vire uma fila de suporte.
    Produto, desenvolvimento, plataforma e SRE precisam de objetivos,
    responsabilidades e critérios de engajamento claros.

    ### **Comunicação operacional**

    **Comunicação operacional** reduz ambiguidade entre equipes. Reuniões,
    documentos, canais e decisões registradas importam porque sistemas de
    produção atravessam fronteiras organizacionais.

    ## Mapa visual dos conceitos

    ```mermaid
    flowchart LR
        User["Experiência do usuário"] --> SLI["SLI"]
        SLI --> SLO["SLO"]
        SLO --> Budget["Error budget"]
        Budget --> Change["Mudança controlada"]
        Budget --> Reliability["Trabalho de confiabilidade"]
        Reliability --> Automation["Automação e simplicidade"]
        Automation --> Monitoring["Observabilidade"]
        Monitoring --> Alerting["Alertas e plantão"]
        Alerting --> Incident["Incidente"]
        Incident --> Postmortem["Postmortem"]
        Postmortem --> Reliability
        Change --> User
    ```

    ## Tabela de estudo rápido

    | Conceito | Pergunta que ele responde | Resultado esperado |
    | --- | --- | --- |
    | SLI | O que vamos medir? | Evidência objetiva de comportamento. |
    | SLO | Qual nível é bom o suficiente? | Meta clara para produto e engenharia. |
    | Error budget | Quanto risco ainda podemos gastar? | Decisão objetiva sobre releases e estabilização. |
    | Toil | Que trabalho repetitivo consome a equipe? | Priorização de automação e melhoria. |
    | Monitoramento | O que precisa acordar uma pessoa? | Alertas acionáveis e menos ruído. |
    | Incidente | Quem coordena e comunica durante a crise? | Resposta mais rápida e menos caos. |
    | Postmortem | O que o sistema nos ensinou? | Ações preventivas e memória operacional. |
    | Overload | Quando rejeitar ou degradar trabalho? | Proteção contra cascatas. |
    | Consenso | Que estado não pode divergir? | Coordenação forte para decisões críticas. |
    | Integridade | O dado pode ser restaurado e verificado? | Recuperação confiável. |

    ## Leitura complementar

    - Livro oficial online do Google SRE: <https://sre.google/sre-book/table-of-contents/>
    - Materiais suplementares citados no PDF: <https://g.co/SREBook>

    ## Referências

    - Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard, eds. **Engenharia de Confiabilidade do Google**. Novatec, 2016.
    - Google. **Site Reliability Engineering: How Google Runs Production Systems**. <https://sre.google/sre-book/>.
    """


def build_source() -> str:
    return """
    # Fonte e escopo

    Este material foi criado a partir do PDF local:

    - `Engenharia de Confiabilidade do Google ( etc.).pdf`
    - Título no PDF: **Engenharia de Confiabilidade do Google**
    - Autores/editores: Betsy Beyer, Chris Jones, Jennifer Petoff e Niall Richard Murphy
    - Edição em português: Novatec, 2016

    O conteúdo deste repositório é um guia de estudo com resumos e conceitos
    reescritos. Ele não reproduz capítulos do livro e deve ser usado junto com a
    obra original.

    Materiais suplementares mencionados no PDF: <https://g.co/SREBook>.

    ## Referências

    - Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard, eds. **Engenharia de Confiabilidade do Google**. Novatec, 2016.
    - Google. **Site Reliability Engineering: How Google Runs Production Systems**. <https://sre.google/sre-book/>.
    """


def build_readme() -> str:
    return """
    # Curso Engenharia de Confiabilidade

    Repositório MkDocs com conceitos centrais e resumo capítulo a capítulo do
    livro **Engenharia de Confiabilidade do Google**.

    Site público: <https://rafaelrezo.github.io/curso-engenharia-confiabilidade/>

    ## Rodando localmente

    ```bash
    make install
    make run
    ```

    Depois acesse `http://127.0.0.1:8001`.

    Para usar outra porta:

    ```bash
    make run PORT=8000
    ```

    ## Gerando o site estático

    ```bash
    make build
    ```

    ## Validando em modo estrito

    ```bash
    make strict
    ```

    ## Validando o conteúdo editorial

    ```bash
    make check-content
    ```

    ## Regenerando a documentação

    ```bash
    make generate
    ```

    ## Limpando artefatos

    ```bash
    make clean
    make clean-venv
    ```

    ## Organização

    - `docs/conceitos-centrais.md`: mapa de referência dos conceitos de SRE.
    - `docs/capitulos/`: resumos dos 25 capítulos consolidados.
    - `docs/fonte-e-escopo.md`: fonte usada e limites do material.

    ## Referências

    - Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard, eds. **Engenharia de Confiabilidade do Google**. Novatec, 2016.
    - Google. **Site Reliability Engineering: How Google Runs Production Systems**. <https://sre.google/sre-book/>.
    """


def build_mkdocs() -> str:
    by_number = {chapter["number"]: chapter for chapter in chapters}
    nav_lines = [
        "site_name: Curso Engenharia de Confiabilidade",
        "site_description: Conceitos centrais e resumos de Engenharia de Confiabilidade do Google",
        "site_url: https://rafaelrezo.github.io/curso-engenharia-confiabilidade/",
        "theme:",
        "  name: material",
        "  language: pt-BR",
        "  features:",
        "    - navigation.sections",
        "    - navigation.top",
        "    - search.highlight",
        "extra_css:",
        "  - stylesheets/extra.css",
        "markdown_extensions:",
        "  - admonition",
        "  - pymdownx.superfences:",
        "      custom_fences:",
        "        - name: mermaid",
        "          class: mermaid",
        "          format: !!python/name:pymdownx.superfences.fence_code_format",
        "  - toc:",
        "      permalink: true",
        "nav:",
        "  - Início: index.md",
        "  - Conceitos centrais: conceitos-centrais.md",
        "  - Fonte e escopo: fonte-e-escopo.md",
    ]
    for part, nums in PART_NAV.items():
        nav_lines.append(f"  - {part}:")
        for number in nums:
            chapter = by_number[number]
            nav_title = display_title(chapter)
            nav_lines.append(
                f"      - \"Capítulo {display_number(number):02d} - {nav_title}\": capitulos/{display_slug(number)}"
            )
    return "\n".join(nav_lines) + "\n"


def build_extra_css() -> str:
    return """
    /* Use the available viewport for course content and diagrams. */
    .md-grid {
      max-width: 96rem;
    }

    .md-sidebar--secondary {
      display: none;
    }

    .md-content {
      max-width: none;
    }

    .md-content__inner {
      margin: 0 1.6rem 2rem;
    }

    .md-typeset {
      font-size: 0.82rem;
    }

    .md-typeset h1 {
      margin-bottom: 1.2rem;
    }

    .md-typeset h2 {
      margin-top: 2.2rem;
    }

    .md-typeset table:not([class]) {
      display: table;
      width: 100%;
    }

    .md-typeset .mermaid {
      width: 100%;
      margin: 1.25rem 0 2rem;
      overflow-x: auto;
      text-align: center;
    }

    .md-typeset .mermaid svg {
      min-width: 760px;
      max-width: 100%;
      height: auto;
    }

    @media screen and (min-width: 76.25em) {
      .md-sidebar--primary {
        width: 14rem;
      }

      .md-main__inner {
        margin-top: 0;
      }
    }

    @media screen and (max-width: 76.1875em) {
      .md-content__inner {
        margin: 0 1rem 2rem;
      }

      .md-typeset .mermaid svg {
        min-width: 640px;
      }
    }
    """


def main() -> None:
    write(CHAPTERS_DIR / display_slug(3), consolidated_risk_slo_page())
    write(CHAPTERS_DIR / display_slug(7), consolidated_automation_release_page())
    write(CHAPTERS_DIR / display_slug(10), consolidated_alerting_oncall_page())
    write(CHAPTERS_DIR / display_slug(13), consolidated_incident_response_page())
    write(CHAPTERS_DIR / display_slug(19), consolidated_load_balancing_page())
    write(CHAPTERS_DIR / display_slug(21), consolidated_overload_cascading_page())
    write(CHAPTERS_DIR / display_slug(24), consolidated_scheduling_pipelines_page())

    for chapter in chapters:
        # Chapter 01 is maintained manually as a consolidated introduction.
        # Consolidated pages are generated from their representative chapter numbers.
        if chapter["number"] in DISPLAY_SEQUENCE and chapter["number"] not in {1, 3, 7, 10, 13, 19, 21, 24}:
            write(CHAPTERS_DIR / display_slug(chapter["number"]), chapter_page(chapter))

    write(DOCS / "index.md", build_index())
    write(DOCS / "conceitos-centrais.md", build_concepts())
    write(DOCS / "fonte-e-escopo.md", build_source())
    write(ROOT / "README.md", build_readme())
    write(ROOT / "mkdocs.yml", build_mkdocs())


if __name__ == "__main__":
    main()

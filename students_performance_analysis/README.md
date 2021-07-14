

<h1>Seleção de atributos baseado em métricas</h1>

<p>O objetivo dessa análise é a partir do dataset Students Performance avaliar quais são as variáveis que mais influenciam para dizer se um aluno foi aprovado ou não.  São 9 colunas que tem os atributos descrito abaixo </p>

<table>
    <tr>
    <th>Gender</th>
        <td>Variável categórica. Female e Male</td>
    </tr>
    <tr>
        <th>Race/ethnicity</th>
           <td>Variável categórica. Group A,B,C,D e E</td>
    </tr>
    <tr>
        <th>Parental level of education</th>
           <td>Variável categórica. Bachelor's degree, some college, master's degree, associate's degree, high school e some high school</td>
    </tr>
    <tr>
        <th>Lunch</th>
           <td>Variável categórica. Standard e free/reduced </td>
    </tr>
    <tr>
        <th>Test preparation course</th>
           <td>Variável categórica. None e complete</td>
    </tr>
    <tr>
        <th>Math score</th>
           <td>Variável númerica. Pode variar de 0 a 100</td>
    </tr>
    <tr>
        <th>Reading score</th>
           <td>Variável númerica. Pode variar de 0 a 100</td>
    </tr>
    <tr>
        <th>Writing score</th>
           <td>Variável númerica. Pode variar de 0 a 100</td>
    </tr>

</table>

<p>Uma das maneiras de verificar a força dessas variáveis para responder nosso problema é utilizar o teste de chi quadrado. Assim, um alto valor de chi quadrado indica que mais relacionadas são essas variáveis entre si.</p>

<p>Dito isso, uma outra maneira de avaliar quão relacionadas são as variáveis para prever se um aluno foi aprovado ou não é utilizar os modelos lineares e de árvore de decisão.  Para os primeiros é necessário se utilizar da técnica de regularização onde é feito uma seleção do melhor valor de C (penalização aplicada para ajuste da reta aos dados) para criar um modelo que melhor se adapta aos dados (sem que ocorra o overfitting). Já para os últimos é necessário verificar o ganho de informação que cada segmentação dos dados por variável traz. Por fim, através desses conceitos vamos analisar quais são as variáveis mais importantes para saber se um aluno será ou não aprovado.</p>


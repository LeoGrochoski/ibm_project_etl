# Criação de Dados

## Biblioteca Faker

Utilizei a biblioteca faker para geração dos dados sinteticos de clientes. Consegui gerar dados como nome, endereco, telefone, email e renda.
Utilizei a biblioteca e gerei dados em formatos diferentes, .csv, .json e .xml

## Arquivos

### CSV (Comma-Separated Values)
#### Formato:

Arquivo de texto simples onde os valores são separados por vírgulas (ou outro delimitador como ponto e vírgula).
Cada linha do arquivo representa um registro de dados.
A primeira linha geralmente contém os cabeçalhos das colunas.

#### Uso:

Amplamente utilizado para exportar e importar dados em tabelas de banco de dados e planilhas.
Fácil de ler e escrever para scripts e programas.

#### Vantagens:

Simplicidade e legibilidade.
Compatibilidade com muitos sistemas e ferramentas.

#### Desvantagens:

Não suporta estruturas de dados complexas (apenas tabelas simples).
Falta de suporte para tipos de dados (tudo é texto).

### XML (eXtensible Markup Language)
#### Formato:

Formato de texto estruturado usando tags aninhadas, semelhante ao HTML.
As tags definem a estrutura e a hierarquia dos dados.
Suporta atributos para fornecer informações adicionais sobre os elementos.

#### Uso:

Utilizado em várias aplicações para armazenar e transportar dados.
Comumente usado em web services (SOAP) e configurações de software.

#### Vantagens:

Flexível e extensível, capaz de representar estruturas de dados complexas.
Facilmente legível por humanos e máquinas.

#### Desvantagens:

Verbosidade pode levar a arquivos grandes e de processamento lento.
Mais complexo de analisar e gerar em comparação com CSV e JSON.

### JSON (JavaScript Object Notation)
#### Formato:

Formato de texto leve para intercâmbio de dados, baseado na sintaxe de objetos do JavaScript.
Representa dados como pares de chave-valor e arrays.

#### Uso:

Popular em APIs web (especialmente RESTful APIs) para enviar e receber dados.
Comumente usado em aplicações web para transmissão de dados entre servidor e cliente.

#### Vantagens:

Estrutura simples e compacta.
Nativamente suportado em muitas linguagens de programação, especialmente JavaScript.
Suporta dados aninhados e complexos.

#### Desvantagens:

Pode não ser tão eficiente em termos de espaço como CSV para dados tabulares simples.
A falta de comentários pode dificultar a legibilidade em arquivos grandes.
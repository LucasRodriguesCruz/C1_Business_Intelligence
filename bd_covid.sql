
-- Criação da tabela Localização
CREATE TABLE Localizacao (
 Localizacao_ID INT NOT NULL AUTO_INCREMENT,
 Municipio VARCHAR(50) NOT NULL,
 Bairro VARCHAR(50) NOT NULL,
 PRIMARY KEY (Localizacao_ID)
 );


-- Criação da tabela Data
CREATE TABLE Data (
 Data_ID INT NOT NULL AUTO_INCREMENT,
 DataNotificacao DATE NOT NULL,
 DataCadastro DATE NOT NULL,
 DataDiagnostico DATE NOT NULL,
 DataColeta_RT_PCR DATE NOT NULL,
 DataColetaTesteRapido DATE NOT NULL,
 DataColetaSorologiaIGG DATE NOT NULL,
 DataEncerramento DATE NOT NULL,
 DataObito DATE NOT NULL,
 PRIMARY KEY (Data_ID)
 );


-- Criação da tabela de dimensão Sexo
CREATE TABLE Sexo (
 Sexo_ID INT NOT NULL AUTO_INCREMENT,
 Sexo VARCHAR(50) NOT NULL,
 PRIMARY KEY (Sexo_ID)
 );


-- Criação da tabela de dimensão Comorbidade
CREATE TABLE Comorbidade (
 Comorbidade_ID INT NOT NULL AUTO_INCREMENT,
 ComorbidadePulmao VARCHAR(50) NOT NULL,
 ComorbidadeCardio VARCHAR(50) NOT NULL,
 ComorbidadeRenal VARCHAR(50) NOT NULL,
 ComorbidadeDiabetes VARCHAR(50) NOT NULL,
 ComorbidadeTabagismo VARCHAR(50) NOT NULL,
 ComorbidadeObesidade VARCHAR(50) NOT NULL,
 PRIMARY KEY (Comorbidade_ID)
 );


-- Criação da tabela fato 
CREATE TABLE tabela_fato (
 Localizacao_ID INT NOT NULL,
 Data_ID INT NOT NULL,
 Sexo_ID INT NOT NULL,
 Comorbidade_ID INT NOT NULL,
 Casos_confirmados INT NOT NULL,
 Obitos INT NOT NULL,
 Valor INT NOT NULL,
 PRIMARY KEY (Localizacao_ID,  Data_ID, Sexo_ID, Comorbidade_ID),
 FOREIGN KEY (Localizacao_ID) REFERENCES Localizacao(Localizacao_ID),
 FOREIGN KEY (Data_ID) REFERENCES Data(Data_ID),
 FOREIGN KEY (Sexo_ID) REFERENCES Sexo(Sexo_ID),
 FOREIGN KEY (Comorbidade_ID) REFERENCES Comorbidade(Comorbidade_ID)
 );

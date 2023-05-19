# Criação de Bando de Dados e suas tabelas


## Nessa aula, vamos usar os comandos CREATE DATABASE para a criação do banco de dados e CREATE TABLE para criar tabelas e os INSERT para inserir conteúdos nele.
```sh
*/

CREATE DATABASE teste;

USE teste;

CREATE TABLE membros (ser VARCHAR(20), pernas INT, braços INT);

INSERT INTO membros (ser,pernas,braços) VALUES('humano',2,2);
INSERT INTO membros (ser,pernas,braços) VALUES('inseto',6,0);
INSERT INTO membros (ser,pernas,braços) VALUES('lula',0,10);
INSERT INTO membros (ser,pernas,braços) VALUES('peixe',0,0);
INSERT INTO membros (ser,pernas,braços) VALUES('centopéia',100,0);
INSERT INTO membros (ser,pernas,braços) VALUES('tabela',4,0);
INSERT INTO membros (ser,pernas,braços) VALUES('poltrona',4,2);
INSERT INTO membros (ser,pernas,braços) VALUES('fonografo',0,1);
INSERT INTO membros (ser,pernas,braços) VALUES('tripe',3,0);
INSERT INTO membros (ser,pernas,braços) VALUES('teste123',1,2);
INSERT INTO membros (ser,pernas,braços) VALUES('alien',NULL,NULL);
```


##-- Agora para ver os conteúdos vistos:
```sh

SELECT * FROM membros;
```

##
```sh
-- Agora, se quisermos criar um arquivo em SQL e depois jogar esse arquivo em nosso MySQL, devemos fazer:

# vim membros.sql

# membros.sql

#@ _CREATE_TABLE_
DROP TABLE IF EXISTS membros;
CREATE TABLE membros
(
  ser VARCHAR(20),      # qual é a coisa
  pernas  INT,          # numero of pernas que possui
  braços  INT           # numero of braços que possui
);
#@ _CREATE_TABLE_

#@ _INSERT_
INSERT INTO membros (ser,pernas,braços) VALUES('humano',2,2);
INSERT INTO membros (ser,pernas,braços) VALUES('inseto',6,0);
INSERT INTO membros (ser,pernas,braços) VALUES('lula',0,10);
INSERT INTO membros (ser,pernas,braços) VALUES('peixe',0,0);
INSERT INTO membros (ser,pernas,braços) VALUES('centopéia',100,0);
INSERT INTO membros (ser,pernas,braços) VALUES('tabela',4,0);
INSERT INTO membros (ser,pernas,braços) VALUES('poltrona',4,2);
INSERT INTO membros (ser,pernas,braços) VALUES('fonografo',0,1);
INSERT INTO membros (ser,pernas,braços) VALUES('tripe',3,0);
INSERT INTO membros (ser,pernas,braços) VALUES('teste123',1,2);
INSERT INTO membros (ser,pernas,braços) VALUES('alien',NULL,NULL);
#@ _INSERT_
```


## mysql teste -u root -p < membros.sql
```sh
 mysql -h localhost -u root -p

SELECT * FROM membros;
```

## -- Agora, para fazer o backup do nosso banco de dados:
```sh
mysqldump teste -u root -p  > dump.sql
```

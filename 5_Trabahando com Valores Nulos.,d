# Trabahando com Valores Nulos

##
```sh
wget https://raw.githubusercontent.com/Mazuco/MySQL/master/expt.sql

mysql teste -u root -p < expt.sql

mysql -u root -p
```

##
```sh
USE teste;

SELECT * FROM expt;

SELECT * FROM expt WHERE score = NULL;

SELECT * FROM expt WHERE score <> NULL;

SELECT * FROM expt WHERE score IS NULL;

SELECT * FROM expt WHERE score IS NOT NULL;

SELECT NULL = NULL, NULL <=> NULL;

SELECT subject, test, IF(score IS NULL,'Valor Desconhecido', score) AS 'score' FROM expt;
```


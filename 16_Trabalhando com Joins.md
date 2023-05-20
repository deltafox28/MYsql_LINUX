# Trabalhando com Joins

##
```sh
/*

O comando JOIN é utilizada para juntar dados provenientes de duas ou mais tabelas do banco de dados, formando assim um relacionamento entre as colunas das tabelas selecionadas. Temos duas categorias principais de joins:

        INNER JOIN: Retorna linhas (registros) quando houver pelo menos uma correspondência em ambas as tabelas.
        OUTER JOIN: Retorna linhas (registros) mesmo quando não houver ao menos uma correspondência em uma das tabelas (ou ambas). O OUTER JOIN divide-se em  LEFT JOIN, RIGHT JOIN e FULL JOIN.

É importante saber como cada tipo se comporta porque, se as linhas desejadas não forem capturadas pela associação, elas não poderão aparecer no resultado final.


*/
```


##
```sh
CREATE TABLE tabela1 (
	tabela1_id INTEGER,
	tabela1_valor CHAR(3)
);
```

##
```sh
CREATE TABLE tabela2 (
	tabela2_id INTEGER,
	tabela2_valor CHAR(3),
	tabela1_id INTEGER
);
```

##
```sh
INSERT INTO tabela1 (tabela1_id, tabela1_valor) VALUES (1, 'boo');
INSERT INTO tabela1 (tabela1_id, tabela1_valor) VALUES (2, 'lol');
INSERT INTO tabela2 (tabela2_id, tabela2_valor, tabela1_id) VALUES (1, 'baz', 2);
INSERT INTO tabela2 (tabela2_id, tabela2_valor, tabela1_id) VALUES (2, 'qux', 3);
```

##
```sh
-- INNER JOIN

SELECT * FROM tabela1 f INNER JOIN tabela2 b ON b.tabela1_id = f.tabela1_id;

-- O MySQL compara cada linha na primeira tabela em relação a cada na segunda tabela e identifica os pares correspondentes com base na condição ON. 

-- As linhas que correspondem são unidas e incluídas no resultado. 

-- Nossa condição ON especifica que o valor na coluna tabela1_id de ambas as tabelas deve ser igual e que apenas um par de linhas atenda ao requisito.
```


##
```sh
-- LEFT OUTER JOIN

SELECT * FROM tabela1 f LEFT OUTER JOIN tabela2 b ON f.tabela1_id = b.tabela1_id;

```

##
```sh
-- Os dois OUTER JOINs retornam as mesmas linhas que INNER JOIN, mas também incluem as linhas sem correspondência de uma tabela ou de outra (as partes externas dos círculos de interseção). 

-- O LEFT OUTER JOIN inclui as linhas não correspondidas da tabela que aparece à esquerda da palavra-chave JOIN. No resultado, as colunas definidas pela outra tabela contêm NULL.

-- RIGHT OUTER JOIN

SELECT * FROM tabela1 f RIGHT OUTER JOIN tabela2 b ON f.tabela1_id = b.tabela1_id;
```

##
```sh
-- RIGHT OUTER JOIN é o oposto de LEFT OUTER JOIN, retornando as linhas sem correspondência da tabela que aparece à direita da palavra-chave JOIN.
```

##
```sh
-- JOIN

-- O mais básico, que soma ambas as tabelas:

SELECT * FROM tabela1 JOIN tabela2;


-- Link de ref:
-- https://dev.mysql.com/doc/refman/8.0/en/join.html
-- https://www.w3schools.com/sql/sql_join.asp
```

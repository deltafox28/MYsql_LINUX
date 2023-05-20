# Clones e tabelas temporarias

##
```sh
use teste;

show tables;

CREATE TABLE mail2 LIKE mail;
```

##
```sh
INSERT INTO mail2 SELECT * FROM mail WHERE srcuser = 'gene';

INSERT INTO mail2 SELECT * FROM mail WHERE srcuser = 'teste1';

SELECT * FROM mail2;
```

##
```sh
CREATE TEMPORARY TABLE mail SELECT * FROM mail;

SELECT COUNT(*) FROM mail;

DELETE FROM mail;

SELECT COUNT(*) FROM mail;

DROP TEMPORARY TABLE mail;

SELECT COUNT(*) FROM mail;

DROP TEMPORARY TABLE IF EXISTS mail;
```

##
```sh
-- Links de Referência:
https://dev.mysql.com/doc/refman/8.0/en/create-table.html
```




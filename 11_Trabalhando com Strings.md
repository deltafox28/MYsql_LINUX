# Trabalhando com Strings

##
```sh
CREATE TABLE temp_char (
    data CHAR(3)
);

INSERT INTO temp_char(data) VALUES('abc'), (' a ');

SELECT data, LENGTH(data) 
    FROM temp_char;
```

##
```sh
CREATE TABLE temp_varchar (
    data VARCHAR(255)
);

INSERT INTO temp_varchar(data) VALUES('abc'), (' a ');

SELECT data, LENGTH(data) 
    FROM temp_varchar;
```

##
```sh
CREATE TABLE assuntos (
 nome VARCHAR(40),
 corrente ENUM('arte', 'comercio', 'ciencia')
);

INSERT INTO assuntos (nome, corrente) VALUES ('biologia','ciencia'), ('estatisticas','comercio'), ('historia','arte');

SELECT nome, corrente FROM assuntos WHERE corrente = 'comercio';
```

##
```sh
UPDATE assuntos SET corrente = 'ciencia' WHERE corrente = 'comercio';

SELECT * FROM assuntos;

```

##
```sh
CREATE TABLE usuarios(
    id_usuario INT UNSIGNED NOT NULL,
    preferencias JSON NOT NULL);

INSERT INTO usuarios(id_usuario, preferencias)
    VALUES(1, '{"pag_tamanho": 10, "gostos": {"esportes": 1}}');


SELECT preferencias FROM usuarios;


INSERT INTO usuarios(id_usuario, preferencias)
    VALUES(2, JSON_OBJECT("pag_tam", 1, "network", JSON_ARRAY("GSM", "CDMA", "WIFI")));


SELECT preferencias FROM usuarios;
```


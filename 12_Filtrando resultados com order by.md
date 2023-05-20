# Filtrando resultados com order by

##
```sh
DROP TABLE IF EXISTS log_moto;
CREATE TABLE log_moto
(
  cart_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome      VARCHAR(20) NOT NULL,
  data_viagem DATE NOT NULL,
  milhas     INT NOT NULL,
  PRIMARY KEY (cart_id)
);

INSERT INTO log_moto (nome,data_viagem,milhas)
  VALUES
    ('João','2014-07-30',152),
    ('Suzi','2014-07-29',391),
    ('Lucas','2014-07-29',300),
    ('Lucas','2014-07-27',96),
    ('João','2014-07-29',131),
    ('Lucas','2014-07-26',115),
    ('Suzi','2014-08-02',502),
    ('Lucas','2014-08-01',197),
    ('João','2014-08-02',79),
    ('Lucas','2014-07-30',203)
;
```

##
```sh
SELECT * FROM log_moto;

SELECT nome, data_viagem, DAYNAME(data_viagem) FROM log_moto ORDER BY nome, data_viagem;

SELECT * FROM log_moto;


SELECT * FROM log_moto ORDER BY nome;


SELECT * FROM log_moto ORDER BY nome DESC;


SELECT * FROM log_moto ORDER BY nome, data_viagem;


SELECT * FROM log_moto ORDER BY nome DESC, data_viagem;


SELECT nome, data_viagem, milhas AS distancia FROM log_moto ORDER BY distancia;


SELECT t, srcuser, FLOOR((size+1023)/1024) FROM mail WHERE size > 50000 ORDER BY FLOOR((size+1023)/1024);

SELECT t, srcuser, FLOOR((size+1023)/1024) AS KB FROM mail WHERE size > 50000 ORDER BY KB;


SELECT * FROM mail ORDER BY TIME(t);


SELECT * FROM mail ORDER BY DATE(t);


SELECT * FROM mail ORDER BY MONTH(t), DAYOFMONTH(t);


SELECT * FROM mail ORDER BY DAYOFWEEK(t);


SELECT * FROM log_moto ORDER BY FIELD(nome,'João','Suzi','Lucas');
```

# Trabalhando com AUTO_INCREMENT

##
```sh
CREATE TABLE inseto
(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id),
nome VARCHAR(30) NOT NULL, 
date DATE NOT NULL, 
origem VARCHAR(30) NOT NULL
);

INSERT INTO inseto (id,nome,date,origem) VALUES
(NULL,'housefly','2001-09-10','kitchen'),
(NULL,'millipede','2001-09-10','driveway'),
(NULL,'grasshopper','2001-09-10','front yard');
```

##
```sh
SELECT * FROM inseto ORDER BY id;

ALTER TABLE inseto DROP id;

ALTER TABLE inseto
ADD id INT UNSIGNED NOT NULL AUTO_INCREMENT FIRST,
ADD PRIMARY KEY (id);
```

##
```sh
SELECT * FROM inseto ORDER BY id;

ALTER TABLE inseto AUTO_INCREMENT = 1000;

INSERT INTO inseto (id,nome,date,origem) VALUES
(NULL,'housefly','2001-09-10','kitchen'),
(NULL,'millipede','2001-09-10','driveway'),
(NULL,'grasshopper','2001-09-10','front yard');

SELECT * FROM inseto ORDER BY id;

-- Links de ref:
-- https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html
```

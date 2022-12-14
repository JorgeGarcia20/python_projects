CREATE DATABASE login_app;
USE login_app;

CREATE TABLE tipo_usuario( 
    id TINYINT(1) UNSIGNED NOT NULL AUTO_INCREMENT ,
    usuario VARCHAR(15) NOT NULL , 
    PRIMARY KEY (id)
    );

CREATE TABLE usuario( 
    id SMALLINT(3) UNSIGNED NOT NULL AUTO_INCREMENT , 
    usuario VARCHAR(20) NOT NULL ,
    password CHAR(120) NOT NULL , 
    tipo_usuario TINYINT(1) UNSIGNED NOT NULL , 
    PRIMARY KEY (id));

ALTER TABLE usuario ADD CONSTRAINT FK_usuario_tipousuario
    FOREIGN KEY (tipo_usuario) REFERENCES tipo_usuario(id);

INSERT tipousuario(usuario) VALUES ('Administrador'), ('Cliente');

insert usuario(usuario, password, tipo_usuario) values
('Garcia', 'pbkdf2:sha256:260000$pgG4qLX5XMtkUAYz$a791554138ce4063c1adafa7f169e443644e4dd84522fc3324ec54b4b5fd2e06', 2);


-- SELECT id, usuario, password FROM usuario WHERE usuario = 'Alberto';

-- SELECT USUARIO.id, USUARIO.usuario, TIPO.id, TIPO.usuario
--                     FROM usuario USUARIO 
--                     JOIN tipousuario TIPO
--                     ON USUARIO.tipo_usuario = TIPO.id
--                     WHERE USUARIO.id = 2;
                    
-- SELECT USUARIO.id, USUARIO.usuario, TIPO.id, TIPO.usuario
--                     FROM usuario USUARIO 
--                     JOIN tipousuario TIPO
--                     ON USUARIO.tipo_usuario = TIPO.id
--                     WHERE USUARIO.id = '3';
                    
-- SELECT USU.id, USU.usuario, TIP.id, TIP.usuario
--                     FROM usuario USU JOIN tipousuario TIP ON USU.tipo_usuario = TIP.id
--                     WHERE USU.id = 1;
-- select *  from usuario;
CREATE DATABASE IF NOT EXISTS optimizador_insertos;
USE optimizador_insertos;

CREATE TABLE tornos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(100)
);

CREATE TABLE tipos_insertos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    vida_util_estimada FLOAT
);

CREATE TABLE materiales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    factor_desgaste FLOAT
);

CREATE TABLE insertos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_tipo INT,
    id_torno INT,
    fecha_instalacion DATE,
    estado ENUM('activo', 'cambiado') DEFAULT 'activo',
    FOREIGN KEY (id_tipo) REFERENCES tipos_insertos(id),
    FOREIGN KEY (id_torno) REFERENCES tornos(id)
);

CREATE TABLE uso_insertos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_inserto INT,
    fecha DATE,
    horas_usadas FLOAT,
    id_material INT,
    FOREIGN KEY (id_inserto) REFERENCES insertos(id),
    FOREIGN KEY (id_material) REFERENCES materiales(id)
);

INSERT INTO materiales (nombre, factor_desgaste) VALUES 
('Teflon', 0.7),
('Grillon', 1.0),
('Acero Inoxidable', 1.5),
('Aluminio', 0.9),
('Bronce', 1.2);

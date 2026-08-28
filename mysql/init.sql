CREATE DATABASE IF NOT EXISTS company;

USE company;

CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
role VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS assets(
id INT AUTO_INCREMENT PRIMARY KEY,
hostname VARCHAR(50),
ip VARCHAR(50),
status VARCHAR(20)
);

INSERT INTO users(name,role)
VALUES
('admin','operator');
INSERT INTO assets(hostname,ip,status)
VALUES
('prod-web01','192.168.1.10','running'),
('prod-db01','192.168.1.20','running')

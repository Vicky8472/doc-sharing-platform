CREATE DATABASE admin;
use admin;


CREATE TABLE admin (
    admin_id VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

INSERT INTO admin (admin_id, password) VALUES ('admin1', '123');

select *from admin;


use admin;
CREATE TABLE docs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    content LONGBLOB
);

select* from docs;
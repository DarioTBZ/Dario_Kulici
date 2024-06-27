DROP DATABASE IF EXISTS dariosql;
CREATE DATABASE dariosql;
USE dariosql;

CREATE TABLE categorie (
    id INT unsigned auto_increment primary key,
    type VARCHAR(255) not null,
    description TEXT not null
);

CREATE TABLE location (
    id INT unsigned auto_increment primary key,
    location VARCHAR(255) not null,
    postal_code INT not null
    );

CREATE TABLE address (
    id INT unsigned auto_increment primary key,
    person_address VARCHAR(255) not null, 
    fk_location_id INT unsigned not null,
    
    foreign key(fk_location_id) references location(id)
);

CREATE TABLE person (
    id INT unsigned auto_increment primary key,
    firstname VARCHAR(255) not null,
    lastname VARCHAR(255) not null,
    email VARCHAR(255) not null unique,
    fk_address_id INT unsigned not null,
    
    FOREIGN KEY (fk_address_id) REFERENCES address(id)
    );

CREATE TABLE product (
    id INT unsigned auto_increment primary key,
	fk_categorie_id INT UNSIGNED NOT NULL,
    `name` VARCHAR(255) not null,
    price INT unsigned unsigned not null,

    FOREIGN KEY(fk_categorie_id) REFERENCES categorie(id)
);

CREATE TABLE `order` (
    id INT unsigned auto_increment PRIMARY KEY,
    order_date DATETIME DEFAULT NOW(),
    fk_product_id INT UNSIGNED NOT NULL,
    
    foreign key(fk_product_id) references product(id)
);
CREATE DATABASE banking_system;

USE banking_system;

-- Table for customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00
);

-- Table for transactions
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (first_name, last_name, email, balance) VALUES ('Tony', 'Stark', 'starkiswithTony@marvel.com', 1000.00);
INSERT INTO customers (first_name, last_name, email, balance) VALUES ('Bruce', 'Banner', 'bruceLovesNatasha@marvel.com', 1000.00);
INSERT INTO customers (first_name, last_name, email, balance) VALUES ('Black', 'Window', 'natashaIsGreen@marvel.com', 1000.00);
INSERT INTO customers (first_name, last_name, email, balance) VALUES ('Thor', 'Odinson', 'thorisGodofThunder@marvel.com', 1000.00);
INSERT INTO customers (first_name, last_name, email, balance) VALUES ('Loki', 'Odinson', 'godOfMischief@marvel.com', 1000.00);

Select * from customers;
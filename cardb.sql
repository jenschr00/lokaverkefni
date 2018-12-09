CREATE DATABASE 0908012440_carsales;
USE 0908012440_carsales;

DROP TABLE IF EXISTS USERS;
DROP TABLE IF EXISTS CARS;
DROP TABLE IF EXISTS ORDERS;

CREATE TABLE USERS(
	User_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(20),
    UserPassword VARCHAR(20),
    Users_Name VARCHAR(50),
    Email VARCHAR(15),
    USER_TYPE VARCHAR(10)
);


CREATE TABLE CARS(
	PlateNumber VARCHAR(8) NOT NULL PRIMARY KEY,
    Color VARCHAR(10),
	Manufacturer VARCHAR(20),
    Model VARCHAR(20),
    Sjalfskiptur BOOLEAN,
    Beinskiptur BOOLEAN,
    Car_Name VARCHAR(45),
    Man_Year VARCHAR(4),
    Price DECIMAL(10,2)
);



CREATE TABLE ORDERS(
	User_id INT,
    Car_Number VARCHAR(8),
    Car_Price DECIMAL(10,2),
    Order_Date DATE,
    CONSTRAINT Buyer FOREIGN KEY(User_id) REFERENCES USERS(User_id)
);

INSERT INTO USERS(UserName,UserPassword,USER_TYPE) 
VALUES
('Jens','jens12345','Admin'),
('Alf','Alf12345','Muggles'),
('Sigg','Sigg12345','Muggles');

INSERT INTO CARS 
VALUES 
('yyf70','Hvítur','Subaru','Impreza','1','0','Jens','2008',1000000.00),
('aa031','Blár','PEUGEOT','306','0','1','Alfred','1998',200000.00),
('bb045','Svartur','KIA','PICANTO','0','1','Sigmundur','2005',350000.00);


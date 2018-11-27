DROP DATABASE IF EXISTS 0908012440_CarSales;
CREATE DATABASE 0908012440_CarSales;
USE 0908012440_CarSales;

CREATE TABLE USERS(
	User_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(20),
    UserPassword VARCHAR(20),
    Users_Name VARCHAR(50),
    Email VARCHAR(15)
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
    Price DECIMAL(10,2),
    Seller_id INT,
    CONSTRAINT Car_Salesman FOREIGN KEY(Seller_id) REFERENCES 0908012440_CarSales.USERS(User_id)
);



CREATE TABLE ORDERS(
	User_id INT,
    Car_Number VARCHAR(8),
    Car_Price DECIMAL(10,2),
    Order_Date DATE,
    CONSTRAINT Buyer FOREIGN KEY(User_id) REFERENCES USERS(User_id) ON DELETE CASCADE,
    CONSTRAINT Bought_Car FOREIGN KEY(Car_Number) REFERENCES CARS(PlateNumber) ON DELETE CASCADE
);

CREATE TABLE title_types(
	type_id INT NOT NULL PRIMARY KEY,
    type_name VARCHAR(20)
);

CREATE TABLE titles(
	title_type INT,
    title_name VARCHAR(60),
    CONSTRAINT TYPE_FK FOREIGN KEY(title_type) REFERENCES title_types(type_id)
);


INSERT INTO USERS(UserName,UserPassword) 
VALUES
('Jens','jens12345'),
('Alf','Alf12345'),
('Sigg','Sigg12345');

INSERT INTO CARS 
VALUES 
('yyf70','Hvítur','Subaru','Impreza','1','0','Jens','2008',1000000.00,1),
('aa031','Blár','PEUGEOT','306','0','1','Alfred','1998',200000.00,2),
('bb045','Svartur','KIA','PICANTO','0','1','Sigmundur','2005',350000.00,3);


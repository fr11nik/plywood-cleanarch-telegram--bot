-- Table for Status
CREATE TABLE statuses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table for Product
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    color VARCHAR(255),
    shape VARCHAR(255),
    application VARCHAR(255),
    treatment VARCHAR(255),
    price NUMERIC(10, 2),
    min_ready_date TIMESTAMP
);

-- Table for Organization
CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table for Position
CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table for User
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    phone_number VARCHAR(50),
    birth_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    position_id INTEGER REFERENCES positions(id),
    organization_id INTEGER REFERENCES organizations(id),
    email VARCHAR(255),
    UNIQUE(email)
);

-- Table for Order
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    status_id INTEGER REFERENCES statuses(id),
    datetime TIMESTAMP NOT NULL,
    user_id INTEGER REFERENCES users(id)
);

-- Table for SupportChat
CREATE TABLE support_chats (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    problem_description TEXT,
    response TEXT DEFAULT ''
);

-- Create junction table for User_Orders to normalize product associations
CREATE TABLE user_orders (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    user_id INTEGER REFERENCES users(id)
);

-- Create table to store the relationship between Orders and Products
CREATE TABLE order_products (
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    PRIMARY KEY (order_id, product_id)
);


CREATE TABLE order_products (
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    PRIMARY KEY (order_id, product_id)
);


CREATE TABLE  user_identification (
    code VARCHAR(255),
    position_id INTEGER REFERENCES positions(id),
    PRIMARY KEY (position_id)
);
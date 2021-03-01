CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    restaurant_id INTEGER REFERENCES restaurants
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    restaurant TEXT
);

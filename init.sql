--Crear tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id     SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock  INTEGER NOT NULL
);
 
--Insertar registros
INSERT INTO productos (nombre, precio, stock) VALUES
    ('Laptop Lenovo IdeaPad',  799.99, 15),
    ('Mouse Inalambrico Logitech', 29.99, 80),
    ('Teclado Mecanico Redragon', 59.99, 40),
    ('Monitor LG 24 pulgadas',  249.99, 20),
    ('Auriculares Sony WH-1000', 179.99, 30);

import mysql.connector

class StockManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
    
    def get_category_id_by_name(self, category_name):
        query = "SELECT id FROM category WHERE name = %s"
        self.cursor.execute(query, (category_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def get_categories(self):
        self.cursor.execute("SELECT * FROM category")
        return self.cursor.fetchall()

    def get_category_name_by_id(self, category_id):
        query = "SELECT name FROM category WHERE id = %s"
        self.cursor.execute(query, (category_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def get_products(self):
        self.cursor.execute("SELECT * FROM product")
        return self.cursor.fetchall()

    def add_product(self, name, description, price, quantity, category_id):
        query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        values = (name, description, price, quantity, category_id)
        self.cursor.execute(query, values)
        self.connection.commit()
    
    def add_category(self, name):
        query = "INSERT INTO category (name) VALUES (%s)"
        self.cursor.execute(query, (name,))
        self.connection.commit()

    def delete_product(self, product_id):
        query = "DELETE FROM product WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()

    def update_product(self, product_id, quantity, price):
        query = "UPDATE product SET quantity = %s, price = %s WHERE id = %s"
        values = (quantity, price, product_id)
        self.cursor.execute(query, values)
        self.connection.commit()

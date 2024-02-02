from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLineEdit

class StockApp(QMainWindow):
    def __init__(self, stock_manager):
        super().__init__()

        self.stock_manager = stock_manager

        self.setWindowTitle("Gestion de Stock")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.populate_table()

        self.layout.addWidget(self.table_widget)

        self.central_widget.setLayout(self.layout)

    def populate_table(self):
        products = self.stock_manager.get_products()
        self.table_widget.setRowCount(len(products))
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"])

        for row, product in enumerate(products):
            for col, data in enumerate(product):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row, col, item)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    stock_manager = StockManager(host="your_mysql_host", user="your_mysql_user", password="your_mysql_password", database="store")

    window = StockApp(stock_manager)
    window.show()

    sys.exit(app.exec_())

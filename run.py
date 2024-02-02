from backend import StockManager
from frontend import StockApp
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stock_manager = StockManager(host="your_mysql_host", user="your_mysql_user", password="your_mysql_password", database="store")

    window = StockApp(stock_manager)
    window.show()

    sys.exit(app.exec_())

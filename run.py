# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
#email : raphael.attias@laplateforme.io

from backend import StockManager
from frontend import StockApp
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stock_manager = StockManager(host="127.0.0.1", user="root", password="R@ph@e?13*?", database="store")

    window = StockApp(stock_manager)
    window.show()

    sys.exit(app.exec_())

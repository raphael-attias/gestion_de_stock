# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
#email : raphael.attias@laplateforme.io

from backend import StockManager
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QHBoxLayout, QComboBox, QDialog, QMessageBox, QFileDialog
import csv

class StockApp(QMainWindow):
    def __init__(self, stock_manager):
        super().__init__()

        self.stock_manager = stock_manager
        self.selected_product_id = None 

        self.setWindowTitle("Gestion de Stock")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.populate_table()

        self.layout.addWidget(self.table_widget)

        self.form_layout = QHBoxLayout()

        self.name_label = QLabel("Nom:")
        self.name_input = QLineEdit()

        self.description_label = QLabel("Description:")
        self.description_input = QLineEdit()

        self.price_label = QLabel("Prix:")
        self.price_input = QLineEdit()

        self.quantity_label = QLabel("Quantité:")
        self.quantity_input = QLineEdit()

        self.category_label = QLabel("Catégorie:")
        self.category_combo = QComboBox()
        self.populate_categories()

        self.add_modify_button = QPushButton("Ajouter")
        self.add_modify_button.clicked.connect(self.add_modify_product)

        self.create_category_button = QPushButton("Nouvelle Catégorie")
        self.create_category_button.clicked.connect(self.create_category_dialog)

        self.export_csv_button = QPushButton("Exporter en CSV")
        self.export_csv_button.clicked.connect(self.export_to_csv)

        self.category_filter_label = QLabel("Filtrer par catégorie:")
        self.category_filter_combo = QComboBox()
        self.populate_category_filter()
        self.category_filter_combo.currentIndexChanged.connect(self.filter_by_category)
        self.delete_button = QPushButton("Supprimer")
        self.delete_button.clicked.connect(self.delete_product)

        self.form_layout.addWidget(self.name_label)
        self.form_layout.addWidget(self.name_input)
        self.form_layout.addWidget(self.description_label)
        self.form_layout.addWidget(self.description_input)
        self.form_layout.addWidget(self.price_label)
        self.form_layout.addWidget(self.price_input)
        self.form_layout.addWidget(self.quantity_label)
        self.form_layout.addWidget(self.quantity_input)
        self.form_layout.addWidget(self.category_label)
        self.form_layout.addWidget(self.category_combo)
        self.form_layout.addWidget(self.add_modify_button)
        self.form_layout.addWidget(self.create_category_button)
        self.form_layout.addWidget(self.export_csv_button)
        self.form_layout.addWidget(self.category_filter_label)
        self.form_layout.addWidget(self.category_filter_combo)
        self.form_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.form_layout)

        self.central_widget.setLayout(self.layout)

    def populate_table(self):
        products = self.stock_manager.get_products()
        self.table_widget.setRowCount(len(products))
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"])

        for row, product in enumerate(products):
            for col, data in enumerate(product):
                if col == 5:
                    category_name = self.stock_manager.get_category_name_by_id(data)
                    item = QTableWidgetItem(category_name)
                else:
                    item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row, col, item)

        self.table_widget.itemSelectionChanged.connect(self.update_form_on_selection)

    def populate_categories(self):
        categories = self.stock_manager.get_categories()
        self.category_combo.clear()
        self.category_combo.addItems([category[1] for category in categories])

    def update_form_on_selection(self):
        selected_items = self.table_widget.selectedItems()

        if selected_items:
            row = selected_items[0].row()
            self.selected_product_id = int(self.table_widget.item(row, 0).text())
            self.name_input.setText(self.table_widget.item(row, 1).text())
            self.description_input.setText(self.table_widget.item(row, 2).text())
            self.price_input.setText(self.table_widget.item(row, 3).text())
            self.quantity_input.setText(self.table_widget.item(row, 4).text())
            self.category_combo.setCurrentText(self.table_widget.item(row, 5).text())
            self.add_modify_button.setText("Modifier")
        else:
            self.selected_product_id = None
            self.name_input.clear()
            self.description_input.clear()
            self.price_input.clear()
            self.quantity_input.clear()
            self.category_combo.setCurrentIndex(0)
            self.add_modify_button.setText("Ajouter")

    def add_modify_product(self):
        name = self.name_input.text()
        description = self.description_input.text()
        price = int(self.price_input.text())
        quantity = int(self.quantity_input.text())
        category_name = self.category_combo.currentText()
        category_id = self.stock_manager.get_category_id_by_name(category_name)

        if self.selected_product_id:
            self.stock_manager.update_product(self.selected_product_id, quantity, price)
        else:
            self.stock_manager.add_product(name, description, price, quantity, category_id)

        self.populate_table()


    def create_category_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Nouvelle Catégorie")

        layout = QVBoxLayout()

        name_label = QLabel("Nom de la Catégorie:")
        name_input = QLineEdit()

        create_button = QPushButton("Créer")
        create_button.clicked.connect(lambda: self.create_category(name_input.text(), dialog))

        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(create_button)

        dialog.setLayout(layout)

        dialog.exec_()

    def create_category(self, category_name, dialog):
        if category_name:
            self.stock_manager.add_category(category_name)
            self.populate_categories()
            dialog.accept()
        else:
            QMessageBox.warning(self, "Attention", "Veuillez entrer un nom de catégorie.")

    def export_to_csv(self):
        products = self.stock_manager.get_products()
        file_path, _ = QFileDialog.getSaveFileName(self, "Exporter en CSV", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"])
                for product in products:
                    csv_writer.writerow(product)

    def populate_category_filter(self):
        categories = self.stock_manager.get_categories()
        self.category_filter_combo.addItem("Toutes les catégories")
        self.category_filter_combo.addItems([category[1] for category in categories])

    def filter_by_category(self):
        selected_category = self.category_filter_combo.currentText()
        if selected_category == "Toutes les catégories":
            self.populate_table()
        else:
            category_id = self.stock_manager.get_category_id_by_name(selected_category)
            products = self.stock_manager.get_products_by_category(category_id)
            self.populate_table_with_products(products)

    def populate_table_with_products(self, products):
        self.table_widget.setRowCount(len(products))
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"])

        for row, product in enumerate(products):
            for col, data in enumerate(product):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row, col, item)
    
    def delete_product(self):
        if self.selected_product_id:
            confirm_dialog = QMessageBox.question(
                self, "Confirmation", "Êtes-vous sûr de vouloir supprimer ce produit ?",
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm_dialog == QMessageBox.Yes:
                self.stock_manager.delete_product(self.selected_product_id)
                self.populate_table()
                self.selected_product_id = None
                self.name_input.clear()
                self.description_input.clear()
                self.price_input.clear()
                self.quantity_input.clear()
                self.category_combo.setCurrentIndex(0)
                self.add_modify_button.setText("Ajouter")
        else:
            QMessageBox.warning(self, "Attention", "Aucun produit sélectionné pour la suppression.")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    stock_manager = StockManager(host="127.0.0.1", user="root", password="R@ph@e?13*?", database="store")

    window = StockApp(stock_manager)
    window.show()

    sys.exit(app.exec_())

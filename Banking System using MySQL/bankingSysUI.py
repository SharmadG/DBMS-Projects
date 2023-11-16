from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys
import mysql.connector

class BankingSystemApp(QWidget):
    def __init__(self):
        super().__init__()

        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="banking_system"
        )
        self.cursor = self.db.cursor()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Banking System')
        self.setGeometry(100, 100, 400, 200)

        self.label_customer_id = QLabel('Customer ID:')
        self.entry_customer_id = QLineEdit(self)

        self.label_amount = QLabel('Amount:')
        self.entry_amount = QLineEdit(self)

        self.btn_deposit = QPushButton('Deposit', self)
        self.btn_deposit.clicked.connect(self.deposit)

        self.btn_withdraw = QPushButton('Withdraw', self)
        self.btn_withdraw.clicked.connect(self.withdraw)

        layout = QVBoxLayout()
        layout.addWidget(self.label_customer_id)
        layout.addWidget(self.entry_customer_id)
        layout.addWidget(self.label_amount)
        layout.addWidget(self.entry_amount)
        layout.addWidget(self.btn_deposit)
        layout.addWidget(self.btn_withdraw)

        self.setLayout(layout)

    def deposit(self):
        customer_id = self.entry_customer_id.text()
        amount = self.entry_amount.text()

        if not customer_id or not amount:
            self.show_error("Please enter both customer ID and amount.")
            return

        try:
            amount = float(amount)
            self.cursor.execute("UPDATE customers SET balance = balance + %s WHERE customer_id = %s", (amount, customer_id))
            self.cursor.execute("INSERT INTO transactions (customer_id, amount, transaction_type) VALUES (%s, %s, 'deposit')", (customer_id, amount))
            self.db.commit()
            self.show_info("Deposit successful.")
        except Exception as e:
            self.db.rollback()
            self.show_error(f"Error during deposit: {str(e)}")

    def withdraw(self):
        customer_id = self.entry_customer_id.text()
        amount = self.entry_amount.text()

        if not customer_id or not amount:
            self.show_error("Please enter both customer ID and amount.")
            return

        try:
            amount = float(amount)
            self.cursor.execute("SELECT balance FROM customers WHERE customer_id = %s", (customer_id,))
            balance = self.cursor.fetchone()[0]

            if balance < amount:
                self.show_error("Insufficient funds.")
                return

            self.cursor.execute("UPDATE customers SET balance = balance - %s WHERE customer_id = %s", (amount, customer_id))
            self.cursor.execute("INSERT INTO transactions (customer_id, amount, transaction_type) VALUES (%s, %s, 'withdrawal')", (customer_id, amount))
            self.db.commit()
            self.show_info("Withdrawal successful.")
        except Exception as e:
            self.db.rollback()
            self.show_error(f"Error during withdrawal: {str(e)}")

    def show_info(self, message):
        QMessageBox.information(self, 'Information', message)

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BankingSystemApp()
    window.show()
    sys.exit(app.exec())

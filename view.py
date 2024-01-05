from datetime import datetime

class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message("2. Показати таблицю")
        self.show_message("3. Редагувати рядок")
        self.show_message("4. Видалити рядок")
        self.show_message("5. Вихід")
        choice = input("Виберіть пункт: ")
        return choice

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. Recipients (отримувачі)")
        self.show_message("2. Senders (відправники)")
        self.show_message("3. Parcels (посилки)")
        self.show_message("4. Couriers (кур'єри)")
        self.show_message("5. Warehouses (склади)")
        self.show_message("6. Couriers Warehouses (кур'єри-склади)")
        self.show_message("7. Повернутися до меню")
        table = input("Оберіть потрібну таблицю: ")
        return table

    def show_recipients(self, recipients):
        print("\nRecipients:")
        for recipient in recipients:
            print(f"ID: {recipient[0]}, Name: {recipient[1]}, Address: {recipient[2]}")

    def show_senders(self, senders):
        print("\nSenders:")
        for sender in senders:
            print(f"ID: {sender[0]}, Name: {sender[1]}, Address: {sender[2]}")

    def show_parcels(self, parcels):
        print("\nParcels:")
        for parcel in parcels:
            print(f"ID: {parcel[0]}, Status: {parcel[1]}, Creation Date: {parcel[2]}, Price: {parcel[3]}, Courier ID: {parcel[4]}, Recipient ID: {parcel[5]}, Warehouse ID: {parcel[6]}")

    def show_couriers(self, couriers):
        print("\nCouriers:")
        for courier in couriers:
            print(f"ID: {courier[0]}, Name: {courier[1]}, Phone: {courier[2]}")

    def show_warehouses(self, warehouses):
        print("\nWarehouses:")
        for warehouse in warehouses:
            print(f"ID: {warehouse[0]}, Address: {warehouse[1]}, Phone: {warehouse[2]}")

    def show_couriers_warehouses(self, couriers_warehouses):
        print("\nCouriers Warehouses:")
        for courier_warehouse in couriers_warehouses:
            print(f"ID: {courier_warehouse[0]}, Courier ID: {courier_warehouse[1]}, Warehouse ID: {courier_warehouse[2]}")

    def get_recipient_input(self):
        while True:
            try:
                name = input("Enter recipient name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                address = input("Enter recipient address: ")
                if address.strip():
                    break
                else:
                    print("Address cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name, address

    def get_sender_input(self):
        while True:
            try:
                name = input("Enter sender name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                address = input("Enter sender address: ")
                if address.strip():
                    break
                else:
                    print("Address cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name, address

    def get_parcel_input(self):
        while True:
            try:
                status = input("Enter parcel status: ")
                if status.strip():
                    break
                else:
                    print("Status cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                date = input("Enter creation date (YYYY-MM-DD): ")
                creation_date = datetime.strptime(date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        while True:
            try:
                parcel_cost_input = input("Enter parcel price: ")
                if parcel_cost_input.strip():
                    parcel_cost = float(parcel_cost_input)
                    break
                else:
                    print("Price cannot be empty.")
            except ValueError:
                print("Price must be a valid number.")
        while True:
            try:
                courier_id = int(input("Enter parcel courier ID: "))
                break
            except ValueError:
                print("Courier ID must be a number.")
        while True:
            try:
                recipient_id = int(input("Enter parcel recipient ID: "))
                break
            except ValueError:
                print("Recipient ID must be a number.")
        while True:
            try:
                warehouse_id = int(input("Enter parcel warehouse ID: "))
                break
            except ValueError:
                print("Warehouse ID must be a number.")
        return status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id

    def get_courier_input(self):
        while True:
            try:
                name = input("Enter courier name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                phone = input("Enter courier phone: ")
                if phone.strip():
                    break
                else:
                    print("Phone cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name, phone

    def get_warehouse_input(self):
        while True:
            try:
                address = input("Enter warehouse address: ")
                if address.strip():
                    break
                else:
                    print("Address cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                phone = input("Enter warehouse phone: ")
                if phone.strip():
                    break
                else:
                    print("Phone cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return address, phone

    def get_courier_warehouse_input(self):
        while True:
            try:
                courier_id = int(input("Enter courier ID: "))
                break
            except ValueError:
                print("Courier ID must be a number.")
        while True:
            try:
                warehouse_id = int(input("Enter warehouse ID: "))
                break
            except ValueError:
                print("Warehouse ID must be a number.")
        return courier_id, warehouse_id

    def get_id(self):
        while True:
            try:
                id = int(input("Enter ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number
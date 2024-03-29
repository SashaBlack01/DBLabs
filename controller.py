import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '5':
                break
            elif choice in ['1', '2', '3', '4']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_view_option(table)
            elif choice == '3':
                self.process_update_option(table)
            elif choice == '4':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding recipient:")
            self.add_recipient()
        elif table == '2':
            self.view.show_message("\nAdding sender:")
            self.add_sender()
        elif table == '3':
            self.view.show_message("\nAdding parcel:")
            self.add_parcel()
        elif table == '4':
            self.view.show_message("\nAdding courier:")
            self.add_courier()
        elif table == '5':
            self.view.show_message("\nAdding warehouse:")
            self.add_warehouse()
        elif table == '6':
            self.view.show_message("\nAdding courier-warehouse:")
            self.add_courier_warehouse()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.view_recipients()
        elif table == '2':
            self.view_senders()
        elif table == '3':
            self.view_parcels()
        elif table == '4':
            self.view_couriers()
        elif table == '5':
            self.view_warehouses()
        elif table == '6':
            self.view_couriers_warehouses()
        elif table == '7':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating recipient:")
            self.update_recipient()
        elif table == '2':
            self.view.show_message("\nUpdating sender:")
            self.update_sender()
        elif table == '3':
            self.view.show_message("\nUpdating parcel:")
            self.update_parcel()
        elif table == '4':
            self.view.show_message("\nUpdating courier:")
            self.update_courier()
        elif table == '5':
            self.view.show_message("\nUpdating warehouse:")
            self.update_warehouse()
        elif table == '6':
            self.view.show_message("\nUpdating courier-warehouse:")
            self.update_courier_warehouse()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting recipient:")
            self.delete_recipient()
        elif table == '2':
            self.view.show_message("\nDeleting sender:")
            self.delete_sender()
        elif table == '3':
            self.view.show_message("\nDeleting parcel:")
            self.delete_parcel()
        elif table == '4':
            self.view.show_message("\nDeleting courier:")
            self.delete_courier()
        elif table == '5':
            self.view.show_message("\nDeleting warehouse:")
            self.delete_warehouse()
        elif table == '6':
            self.view.show_message("\nDeleting courier-warehouse:")
            self.delete_courier_warehouse()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def add_recipient(self):
        try:
            name, address = self.view.get_recipient_input()
            self.model.insert_recipient(name, address)
            self.view.show_message("Recipient added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_sender(self):
        try:
            name, address = self.view.get_sender_input()
            self.model.insert_sender(name, address)
            self.view.show_message("Sender added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_parcel(self):
        try:
            status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id = self.view.get_parcel_input()
            self.model.insert_parcel(status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id)
            self.view.show_message("Parcel added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_courier(self):
        try:
            name, phone = self.view.get_courier_input()
            self.model.insert_courier(name, phone)
            self.view.show_message("Courier added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_warehouse(self):
        try:
            address, phone = self.view.get_warehouse_input()
            self.model.insert_warehouse(address, phone)
            self.view.show_message("Warehouse added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_courier_warehouse(self):
        try:
            courier_id, warehouse_id = self.view.get_courier_warehouse_input()
            self.model.insert_courier_warehouse(courier_id, warehouse_id)
            self.view.show_message("Courier Warehouse added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_recipients(self):
        try:
            recipients = self.model.show_recipients()
            self.view.show_recipients(recipients)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_senders(self):
        try:
            senders = self.model.show_senders()
            self.view.show_senders(senders)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_parcels(self):
        try:
            parcels = self.model.show_parcels()
            self.view.show_parcels(parcels)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_couriers(self):
        try:
            couriers = self.model.show_couriers()
            self.view.show_couriers(couriers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_warehouses(self):
        try:
            warehouses = self.model.show_warehouses()
            self.view.show_warehouses(warehouses)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_couriers_warehouses(self):
        print(1)
        try:
            couriers_warehouses = self.model.show_couriers_warehouses()
            self.view.show_couriers_warehouses(couriers_warehouses)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_recipient(self):
        try:
            recipient_id = self.view.get_id()
            name, address = self.view.get_recipient_input()
            self.model.update_recipient(name, address, recipient_id)
            self.view.show_message("Recipient updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_sender(self):
        try:
            sender_id = self.view.get_id()
            name, address = self.view.get_sender_input()
            self.model.update_sender(name, address, sender_id)
            self.view.show_message("Sender updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_parcel(self):
        try:
            parcel_id = self.view.get_id()
            status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id = self.view.get_parcel_input()
            self.model.update_parcel(status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id, parcel_id)
            self.view.show_message("Parcel updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_courier(self):
        try:
            courier_id = self.view.get_id()
            name, phone = self.view.get_courier_input()
            self.model.update_courier(name, phone, courier_id)
            self.view.show_message("Courier updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_warehouse(self):
        try:
            warehouse_id = self.view.get_id()
            address, phone = self.view.get_warehouse_input()
            self.model.update_warehouse(address, phone, warehouse_id)
            self.view.show_message("Warehouse updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_courier_warehouse(self):
        try:
            courier_warehouse_id = self.view.get_id()
            courier_id, warehouse_id = self.view.get_courier_warehouse_input()
            self.model.update_courier_warehouse(courier_id, warehouse_id, courier_warehouse_id)
            self.view.show_message("Courier Warehouse updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_recipient(self):
        try:
            recipient_id = self.view.get_id()
            self.model.delete_recipient(recipient_id)
            self.view.show_message("Recipient deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_sender(self):
        try:
            sender_id = self.view.get_id()
            self.model.delete_sender(sender_id)
            self.view.show_message("Sender deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_parcel(self):
        try:
            parcel_id = self.view.get_id()
            self.model.delete_parcel(parcel_id)
            self.view.show_message("Parcel deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_courier(self):
        try:
            courier_id = self.view.get_id()
            self.model.delete_courier(courier_id)
            self.view.show_message("Courier deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_warehouse(self):
        try:
            warehouse_id = self.view.get_id()
            self.model.delete_warehouse(warehouse_id)
            self.view.show_message("Warehouse deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_courier_warehouse(self):
        try:
            courier_warehouse_id = self.view.get_id()
            self.model.delete_courier_warehouse(courier_warehouse_id)
            self.view.show_message("Courier Warehouse deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


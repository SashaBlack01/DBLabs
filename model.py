import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='courier_service',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_recipient(self, name, address):
        c = self.conn.cursor()
        c.execute('INSERT INTO recipients (name, address) VALUES (%s, %s)', (name, address))
        self.conn.commit()

    def add_sender(self, name, address):
        c = self.conn.cursor()
        c.execute('INSERT INTO senders (name, address) VALUES (%s, %s)', (name, address))
        self.conn.commit()
    
    def add_parcel(self, status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO parcels (status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id) VALUES (%s, %s, %s, %s, %s, %s)', (status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id))
        self.conn.commit()

    def add_courier(self, name, phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO couriers (name, phone) VALUES (%s, %s)', (name, phone))
        self.conn.commit()

    def add_warehouse(self, address, phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO warehouses (address, phone) VALUES (%s, %s)', (address, phone))
        self.conn.commit()

    def add_courier_warehouse(self, courier_id, warehouse_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO couriers_warehouses (courier_id, warehouse_id) VALUES (%s, %s)', (courier_id, warehouse_id))
        self.conn.commit()

    def get_all_recipients(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM recipients')
        return c.fetchall()

    def get_all_senders(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM senders')
        return c.fetchall()

    def get_all_parcels(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM parcels')
        return c.fetchall()

    def get_all_couriers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM couriers')
        return c.fetchall()

    def get_all_warehouses(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM warehouses')
        return c.fetchall()

    def get_all_couriers_warehouses(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM couriers_warehouses')
        return c.fetchall()

    def get_all_couriers_with_warehouses(self):
         c = self.conn.cursor()
         c.execute('SELECT couriers.name AS courier_name, warehouses.address AS warehouse_address FROM couriers JOIN couriers_warehouses ON couriers.courier_id = couriers_warehouses.courier_id JOIN warehouses ON couriers_warehouses.warehouse_id = warehouses.warehouse_id;')
         return c.fetchall()

    def get_delivered_parcels(self):
         c = self.conn.cursor()
         c.execute('''
        SELECT couriers.name AS courier_name, COUNT(parcels.parcel_id) AS delivered_count
        FROM couriers
        LEFT JOIN parcels ON couriers.courier_id = parcels.courier_id
        WHERE parcels.status = 'Delivered'
        GROUP BY couriers.courier_id, couriers.name;
    ''')
         return c.fetchall()

    def get_parcels_in_warehouses(self):
         c = self.conn.cursor()
         c.execute('''
        SELECT warehouses.address AS warehouse_address, COUNT(parcels.parcel_id) AS parcel_count
        FROM parcels
        JOIN warehouses ON parcels.warehouse_id = warehouses.warehouse_id
        GROUP BY warehouses.warehouse_id, warehouses.address;
    ''')
         return c.fetchall()

    def update_recipient(self, name, address, id):
        c = self.conn.cursor()
        c.execute('UPDATE recipients SET name=%s, address=%s WHERE recipient_id=%s', (name, address, id))
        self.conn.commit()

    def update_sender(self, name, address, id):
        c = self.conn.cursor()
        c.execute('UPDATE senders SET name=%s, address=%s WHERE sender_id=%s', (name, address, id))
        self.conn.commit()

    def update_parcel(self, status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE parcels SET status=%s, creation_date=%s, parcel_cost=%s, courier_id=%s, recipient_id=%s, warehouse_id=%s WHERE parcel_id=%s', (status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id, id))
        self.conn.commit()

    def update_courier(self, name, phone, id):
        c = self.conn.cursor()
        c.execute('UPDATE couriers SET name=%s, phone=%s WHERE courier_id=%s', (name, phone, id))
        self.conn.commit()

    def update_warehouse(self, address, phone, id):
        c = self.conn.cursor()
        c.execute('UPDATE warehouses SET address=%s, phone=%s WHERE warehouse_id=%s', (address, phone, id))
        self.conn.commit()

    def update_courier_warehouse(self, courier_id, warehouse_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE warehouses SET courier_id=%s, warehouse_id=%s WHERE courier_warehouse_id=%s', (courier_id, warehouse_id, id))
        self.conn.commit()

    def delete_recipient(self, recipient_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM recipients WHERE recipient_id=%s', (recipient_id,))
        self.conn.commit()

    def delete_sender(self, sender_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM senders WHERE sender_id=%s', (sender_id,))
        self.conn.commit()

    def delete_parcel(self, parcel_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM parcels WHERE parcel_id=%s', (parcel_id,))
        self.conn.commit()

    def delete_courier(self, courier_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM couriers WHERE courier_id=%s', (courier_id,))
        self.conn.commit()

    def delete_warehouse(self, warehouse_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM warehouses WHERE warehouse_id=%s', (warehouse_id,))
        self.conn.commit()

    def delete_courier_warehouse(self, courier_warehouse_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM couriers_warehouses WHERE courier_warehouse_id=%s', (courier_warehouse_id,))
        self.conn.commit()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute('''
        INSERT INTO warehouses (address, phone)
        SELECT chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), '+380' || lpad(trunc(random() * 10000000)::text, 7, '0')
        FROM generate_series(1, %s);
    ''',(number,))
        self.conn.commit()



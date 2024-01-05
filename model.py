from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date

s = Session()

class Recipient(Base):
    __tablename__ = 'recipients'
    recipient_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    parcel = relationship("Parcel")

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"<Recipients(recipient_id={self.recipient_id}, name={self.name}, address={self.address})>"


class Sender(Base):
    __tablename__ = 'senders'
    sender_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"<Senders(sender_id={self.sender_id}, name={self.name}, address={self.address})>"


class Parcel(Base):
    __tablename__ = 'parcels'
    parcel_id = Column(Integer, primary_key=True)
    status = Column(String)
    creation_date = Column(Date)
    parcel_cost = Column(Numeric)

    courier_id = Column(Integer, ForeignKey('couriers.courier_id'))
    recipient_id = Column(Integer, ForeignKey('recipients.recipient_id'))
    warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'))

    def __init__(self, status, creation_date, parcel_cost, courier_id, recipient_id, warehouse_id):
        self.status = status
        self.creation_date = creation_date
        self.parcel_cost = parcel_cost
        self.courier_id = courier_id
        self.recipient_id = recipient_id
        self.warehouse_id = warehouse_id

    def __repr__(self):
        return f"<Parcels(parcel_id={self.parcel_id}, status={self.status}, creation_date={self.creation_date}, parcel_cost={self.parcel_cost}, courier_id={self.courier_id}, recipient_id={self.recipient_id}, warehouse_id={self.warehouse_id})>"


class Courier(Base):
    __tablename__ = 'couriers'
    courier_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)

    parcel = relationship("Parcel")
    courier_warehouse = relationship("CourierWarehouse")

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"<Couriers(courier_id={self.courier_id}, name={self.name}, phone={self.phone})>"


class Warehouse(Base):
    __tablename__ = 'warehouses'
    warehouse_id = Column(Integer, primary_key=True)
    address = Column(String)
    phone = Column(String)

    parcel = relationship("Parcel")
    courier_warehouse = relationship("CourierWarehouse")

    def __init__(self, address, phone):
        self.address = address
        self.phone = phone

    def __repr__(self):
        return f"<Warehouses(warehouse_id={self.warehouse_id}, address={self.address}, phone={self.phone})>"


class CourierWarehouse(Base):
    __tablename__ = 'couriers_warehouses'
    courier_warehouse_id = Column(Integer, primary_key=True)

    courier_id = Column(Integer, ForeignKey('couriers.courier_id'))
    warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'))

    def __init__(self, courier_id, warehouse_id):
        self.courier_id = courier_id
        self.warehouse_id = warehouse_id

    def __repr__(self):
        return f"<CouriersWarehouses(courier_warehouse_id={self.courier_warehouse_id}, courier_id={self.courier_id}, warehouse_id={self.warehouse_id})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def insert_recipient(self, name: str, address: float) -> None:
        recipient = Recipient(name=name, address=address)
        s.add(recipient)
        s.commit()

    def insert_sender(self, name: str, address: float) -> None:
        sender = Sender(name=name, address=address)
        s.add(sender)
        s.commit()

    def insert_parcel(self, status: str, creation_date: Date, parcel_cost: Numeric, courier_id: int, recipient_id: int, warehouse_id: int) -> None:
        parcel = Parcel(status=status, creation_date=creation_date, parcel_cost=parcel_cost, courier_id=courier_id, recipient_id=recipient_id, warehouse_id=warehouse_id)
        s.add(parcel)
        s.commit()

    def insert_courier(self, name: str, phone: str) -> None:
        courier = Courier(name=name, phone=phone)
        s.add(courier)
        s.commit()

    def insert_warehouse(self, address: str, phone: str) -> None:
        warehouse = Warehouse(address=address, phone=phone)
        s.add(warehouse)
        s.commit()

    def insert_courier_warehouse(self, courier_id: int, warehouse_id: int) -> None:
        courier_warehouse = CourierWarehouse(courier_id=courier_id, warehouse_id=warehouse_id)
        s.add(courier_warehouse)
        s.commit()

    def show_recipients(self):
        return s.query(Recipient.recipient_id, Recipient.name, Recipient.address).all()

    def show_senders(self):
        return s.query(Sender.sender_id, Sender.name, Sender.address).all()

    def show_parcels(self):
        return s.query(Parcel.parcel_id, Parcel.status, Parcel.creation_date, Parcel.parcel_cost, Parcel.courier_id, Parcel.recipient_id, Parcel.warehouse_id).all()

    def show_couriers(self):
        return s.query(Courier.courier_id, Courier.name, Courier.phone).all()

    def show_warehouses(self):
        return s.query(Warehouse.warehouse_id, Warehouse.address, Warehouse.phone).all()

    def show_couriers_warehouses(self):
        return s.query(CourierWarehouse.courier_warehouse_id, CourierWarehouse.courier_id, CourierWarehouse.warehouse_id).all()

    def update_recipient(self, name: str, address: str, recipient_id: int) -> None:
        s.query(Recipient).filter_by(recipient_id=recipient_id).update({Recipient.name: name, Recipient.address: address})
        s.commit()

    def update_sender(self, name: str, address: str, sender_id: int) -> None:
        s.query(Sender).filter_by(sender_id=sender_id).update({Sender.name: name, Sender.address: address})
        s.commit()

    def update_parcel(self, status: str, creation_date: Date, parcel_cost: Numeric, courier_id: int, recipient_id: int, warehouse_id: int, parcel_id: int, ) -> None:
        s.query(Parcel).filter_by(parcel_id=parcel_id).update({Parcel.status: status, Parcel.creation_date: creation_date, Parcel.parcel_cost: parcel_cost, Parcel.courier_id: courier_id, Parcel.recipient_id: recipient_id, Parcel.warehouse_id: warehouse_id})
        s.commit()

    def update_courier(self, name: str, phone: str, courier_id: int) -> None:
        s.query(Courier).filter_by(courier_id=courier_id).update({Courier.name: name, Courier.phone: phone})
        s.commit()

    def update_warehouse(self, address: str, phone: str, warehouse_id: int) -> None:
        s.query(Warehouse).filter_by(warehouse_id=warehouse_id).update({Warehouse.address: address, Warehouse.phone: phone})
        s.commit()

    def update_courier_warehouse(self, courier_id: int, warehouse_id: int, courier_warehouse_id: int) -> None:
        s.query(CourierWarehouse).filter_by(courier_warehouse_id=courier_warehouse_id).update({CourierWarehouse.courier_id: courier_id, CourierWarehouse.warehouse_id: warehouse_id})
        s.commit()

    def delete_recipient(self, recipient_id) -> None:
        recipient = s.query(Recipient).filter_by(recipient_id=recipient_id).one()
        s.delete(recipient)
        s.commit()

    def delete_sender(self, sender_id) -> None:
        sender = s.query(Sender).filter_by(sender_id=sender_id).one()
        s.delete(sender)
        s.commit()

    def delete_parcel(self, parcel_id) -> None:
        parcel = s.query(Parcel).filter_by(parcel_id=parcel_id).one()
        s.delete(parcel)
        s.commit()

    def delete_courier(self, courier_id) -> None:
        courier = s.query(Courier).filter_by(courier_id=courier_id).one()
        s.delete(courier)
        s.commit()

    def delete_warehouse(self, warehouse_id) -> None:
        warehouse = s.query(Warehouse).filter_by(warehouse_id=warehouse_id).one()
        s.delete(warehouse)
        s.commit()

    def delete_courier_warehouse(self, courier_warehouse_id) -> None:
        couriers_warehouses = s.query(CourierWarehouse).filter_by(courier_warehouse_id=courier_warehouse_id).all()
        for courier_warehouse in couriers_warehouses:
            s.delete(courier_warehouse)
        s.commit()
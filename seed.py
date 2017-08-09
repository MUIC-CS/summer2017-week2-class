from phonerecord import PhoneRecord, PhoneRecordRepo
from friendship import FriendShip, FriendShipRepo

if __name__ == '__main__':
    PhoneRecordRepo.create_table()

    kfc = PhoneRecord(None, 'KFC', '1150')
    mcdonald = PhoneRecord(None, 'McDonald', '1711')
    pizza = PhoneRecord(None, 'Pizza Company', '1112')
    chester = PhoneRecord(None, 'Chester Grill', '1145')

    PhoneRecordRepo.add(kfc)
    PhoneRecordRepo.add(mcdonald)
    PhoneRecordRepo.add(pizza)
    PhoneRecordRepo.add(chester)

    FriendShipRepo.create_table()

    FriendShipRepo.add_friendship(kfc.id, pizza.id, True)
    FriendShipRepo.add_friendship(kfc.id, chester.id, False)
    FriendShipRepo.add_friendship(chester.id, mcdonald.id, False)
    FriendShipRepo.add_friendship(kfc.id, mcdonald.id, False)

    all = PhoneRecordRepo.find_all()
    print all

#!/usr/bin/python3
"""Task 7 of state"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    result = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()

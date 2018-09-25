from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.automap import automap_base
import datetime

#from helpers import get_con_string, load_tables, update_buckets, update_LJFT




if __name__=="__main__":
    url = 'postgresql://{}:{}@{}:{}/{}'
    user='fmqntwrubliffb'
    password='a076a655c5e74aff036ca94c0daa4e4da3d81e7974f6455ad6cb80874a22f3cf'
    host='ec2-54-235-94-36.compute-1.amazonaws.com'
    port='5432'
    db='d4u0djq9omtvn'
    url = url.format(user, password, host, port, db)

    #cs = get_con_string()
    # automap base
    Base = automap_base()

    # pre-declare User for the 'user' table
    class Leaver(Base):
        __tablename__ = 'leaver'

    # reflect
    engine = create_engine(url)
    Base.prepare(engine, reflect=True)

    # we still have Address generated from the tablename "address",
    # but User is the same as Base.classes.User now

    Suspect = Base.classes.suspect
    Buckets = Base.classes.buckets
    LJFT = Base.classes.LJFT
    Session = sessionmaker(bind=engine)
    session = Session()

    result_list = ['Tracking', 'Lost', 'Inactive', 'Lead', 'TrackAlert', 'Recapture', 'Left Industry']
    for r in result_list:
        results = session.query(Leaver).filter_by(result=r).all()
        count = len(results)
        b = Buckets(status=r, count=count, date=datetime.datetime.now(datetime.timezone.utc))
        session.add(b)

    result_list1 = ['Yes', 'No']
    for i in result_list1:
        results1 = session.query(Leaver).filter_by(inprosshell=i).all()
        count1 = len(results1)
        l = LJFT(status=i, count=count1, date=datetime.datetime.now(datetime.timezone.utc))
        session.add(l)

    try:
        session.commit()
        print('Success')
    except:
        session.rollback()
        print('Failure')

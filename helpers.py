# from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.engine.url import URL
# from sqlalchemy.orm import mapper, sessionmaker
# from sqlalchemy.ext.automap import automap_base
# import datetime
#
#
# def get_con_string():
#     url = 'postgresql://{}:{}@{}:{}/{}'
#     user='fmqntwrubliffb'
#     password='a076a655c5e74aff036ca94c0daa4e4da3d81e7974f6455ad6cb80874a22f3cf'
#     host='ec2-54-235-94-36.compute-1.amazonaws.com'
#     port='5432'
#     db='d4u0djq9omtvn'
#     url = url.format(user, password, host, port, db)
#     return url
#
# def load_tables():
#     """"""
#     cs = get_con_string()
#     # automap base
#     Base = automap_base()
#
#     # pre-declare User for the 'user' table
#     class Leaver(Base):
#         __tablename__ = 'leaver'
#
#     # reflect
#     engine = create_engine(cs)
#     Base.prepare(engine, reflect=True)
#
#     # we still have Address generated from the tablename "address",
#     # but User is the same as Base.classes.User now
#
#     Suspect = Base.classes.suspect
#     Buckets = Base.classes.buckets
#     LJFT = Base.classes.LJFT
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session, Suspect, Leaver, Buckets, LJFT
#
# def get_count(col, status, session):
#     if col == 'result':
#         results = session.query(Leaver).filter_by(result=status).all()
#         count = len(results)
#         return count
#     elif col == 'inpros':
#         results = session.query(Leaver).filter_by(inprosshell=status).all()
#         count = len(results)
#         return count
#
#
#
# def update_buckets(session):
#     result_list = ['Tracking', 'Lost', 'Inactive', 'Lead', 'TrackAlert','User Placed', 'Rep Placed']
#     for r in result_list:
#         ct = get_count('result', r, session)
#         b = Buckets(status=r, count=ct, date=datetime.datetime.now(datetime.timezone.utc))
#         session.add(b)
#     try:
#         session.commit()
#         return 'Success'
#     except:
#         session.rollback()
#         return 'Failure'
#
# def update_LJFT(session):
#     result_list = ['Yes', 'No']
#     for r in result_list:
#         ct = get_count('inpros', r, session)
#         l = LJFT(status=r, count=ct, date=datetime.datetime.now(datetime.timezone.utc))
#         session.add(l)
#     try:
#         session.commit()
#         return 'Success'
#     except:
#         session.rollback()
#         return 'Failure'

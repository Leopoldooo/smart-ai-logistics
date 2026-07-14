from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///logistics.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class DriverLog(Base):
    __tablename__ = "driver_logs"

    id = Column(Integer, primary_key=True, index=True)
    speed = Column(Float)
    harsh_braking = Column(Integer)
    fatigue_level = Column(Integer)
    prediction = Column(String)
    risk_score = Column(Float)


Base.metadata.create_all(bind=engine)
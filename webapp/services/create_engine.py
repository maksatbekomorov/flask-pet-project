from sqlalchemy import create_engine
import os


def write_table(df):
    engine = create_engine(f"sqlite:///{os.path.abspath('test1.db')}")
    df.to_sql(df.name, con=engine)

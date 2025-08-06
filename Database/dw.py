from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()


dw_url = (    f"postgresql+psycopg2://{os.getenv('DW_USER')}:{os.getenv('DW_PASS')}@"
            f"{os.getenv('DW_HOST')}:{os.getenv('DW_PORT')}/{os.getenv('DW_NAME')}")


engine = create_engine(dw_url, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()





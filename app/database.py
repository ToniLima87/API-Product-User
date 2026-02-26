from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time

DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

engine = None

# aguarda banco subir
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("✅ Banco conectado!")
        break
    except Exception:
        print("⏳ Aguardando banco iniciar...")
        time.sleep(3)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ ISSO FALTAVA
Base = declarative_base()

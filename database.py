from sqlmodel import SQLModel, Session, create_engine, select

from models import Task


DATABASE_URL = "sqlite:///tasks.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        existing_task = session.exec(select(Task)).first()

        if existing_task is None:
            sample_tasks = [
                Task(title="Learn FastAPI", completed=False),
                Task(title="Build CRUD API", completed=False),
                Task(title="Submit FlyRank Assignment", completed=False)
            ]

            session.add_all(sample_tasks)
            session.commit()
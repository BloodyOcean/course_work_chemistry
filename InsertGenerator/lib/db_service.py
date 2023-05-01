import random
from typing import Any, List, Type

from sqlalchemy import select, Result
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func, select
from models.models import Customer


class DbService:
    session = None

    def __init__(self, session: Session):
        self.session = session

    def get_instances(self, n: int, obj_type: Type) -> List[Type]:
        """
        Selects n random records from table passed via ORM class and returns the result
        @param n: num of records
        @return: list of appropriate objects
        """
        # TODO: add thresholds checking
        total_count = self.session.query(obj_type).count()
        random_ids = random.sample(range(1, total_count + 1), n)
        random_instances = self.session.query(obj_type).filter(obj_type.id.in_(random_ids)).all()
        return random_instances

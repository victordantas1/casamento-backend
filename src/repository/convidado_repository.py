from sqlalchemy.orm import Session


class ConvidadoRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int):
        pass
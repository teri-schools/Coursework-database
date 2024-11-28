from .base import BaseRepository
from ..models import Label

class LabelRepository(BaseRepository):
    def add_label(self, name: str, country_id: int) -> Label:
        new_label = Label(name=name, country_id=country_id)
        self.session.add(new_label)
        self.session.commit()
        return new_label

    def get_all_labels(self):
        return self.session.query(Label).all()

    def get_label(self, label_id: int) -> Label:
        return self.session.query(Label).filter(Label.id == label_id).first()

    def update_label(self, label_id: int, name: str, country_id: int):
        label = self.get_label(label_id)
        if label:
            label.name = name
            label.country_id = country_id
            self.session.commit()
        return label

    def delete_label(self, label_id: int):
        label = self.get_label(label_id)
        if label:
            self.session.delete(label)
            self.session.commit()

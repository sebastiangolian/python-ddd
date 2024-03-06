from typing import Any, List, Optional

from domain.entity.school_class import SchoolClass
from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from infrastructure.db.db_interface import DbInterface


class SchoolClassRepository(SchoolClassRepositoryInterface):
    TYPE = "school_class"

    def __init__(self, db: DbInterface) -> None:
        self.__db = db

    @property
    def count(self) -> int:
        return self.__db.set_resource(self.TYPE).count()

    def get(self, limit: Optional[int] = None, page: Optional[int] = None) -> List[SchoolClass]:
        school_classes_dicts = self.__db.set_resource(self.TYPE).get(limit, page)
        return [SchoolClass(**school_class_dict) for school_class_dict in school_classes_dicts]

    def get_by_id(self, id: int) -> Optional[SchoolClass]:
        school_class_dict = self.__db.set_resource(self.TYPE).get_by_id(id)
        if school_class_dict:
            return SchoolClass(**school_class_dict)
        else:
            return None

    def get_by_ids(self, ids: List[int]) -> List[SchoolClass]:
        school_classes_dicts = self.__db.set_resource(self.TYPE).get_by_ids(ids)
        return [SchoolClass(**school_class_dict) for school_class_dict in school_classes_dicts]

    def find_by_attribute(self, attribute: str, value: Any) -> List[SchoolClass]:
        school_classes_dicts = self.__db.set_resource(self.TYPE).get_by_attribute(attribute, value)
        return [SchoolClass(**school_class_dict) for school_class_dict in school_classes_dicts]

    def save(self, school_class: SchoolClass) -> None:
        school_class_finded = self.__db.set_resource(self.TYPE).get_by_id(school_class.id)
        if school_class_finded:
            self.__db.set_resource(self.TYPE).update(school_class.id, school_class.to_dict())
        else:
            self.__db.set_resource(self.TYPE).add(school_class.to_dict())

    def remove(self, id: int) -> None:
        self.__db.set_resource(self.TYPE).remove(id)

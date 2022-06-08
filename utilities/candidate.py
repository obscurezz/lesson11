from utilities.utils import *


class Candidates(object):
    def __init__(self, value):
        self._value = load_candidates_from_json(value)

    @property
    def print_value(self):
        return self._value

    def get_candidate_by_id(self, uid: int) -> dict | None:
        return next((item for item in self._value if item['id'] == uid), None)

    def get_candidates_by_name(self, name=None) -> list | dict:
        if name is not None:
            return [(item['id'], item['name']) for item in self._value if name.lower() in item['name'].lower()]
        return [(item['id'], item['name']) for item in self._value]

    def get_candidates_by_skill(self, skill: str) -> list[dict] | None:
        return [item for item in self._value if skill.lower() in item['skills']]

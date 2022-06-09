import json


def load_candidates_from_json(jsonfile) -> list[dict] | None:
    if jsonfile is not None:
        with open(jsonfile, 'r', encoding='utf-8') as file:
            result = json.load(file)
            return result
    raise FileExistsError('No such file')

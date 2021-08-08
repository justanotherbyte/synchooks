from typing import List, Dict, Union, Optional

class Embed:
    def __init__(
        self,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        colour: Optional[int] = None,
        color: Optional[int] = None
    ):
        self.title = title
        self.description = description
        self.colour = colour or color
        self.fields: List[Dict[str, Union[str, bool]]] = []

    def add_field(self, *, name: str, value: str, inline: bool = False):
        field = {
            "name": name,
            "value": value,
            "inline": inline
        }
        self.fields.append(field)
        return self

    def to_dict(self) -> dict:
        data = {
            "title": self.title,
            "description": self.description,
            "color": self.colour,
            "fields": self.fields
        }
        return data
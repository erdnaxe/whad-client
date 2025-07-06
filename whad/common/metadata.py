from dataclasses import dataclass, fields
from typing import Optional

@dataclass(repr=False)
class Metadata:
    raw : Optional[bool] = None
    timestamp : Optional[int] = None
    channel : Optional[int] = None
    rssi : Optional[int] = None

    def convert_to_header(self):
        pass

    def __repr__(self):
        metadatas = []
        for field in fields(self.__class__):
            if hasattr(self, field.name) and getattr(self,field.name) is not None:
                metadatas.append("{}={}".format(field.name, getattr(self,field.name)))

        if len(metadatas) == 0:
            return ""
        else:
            return "[ " + ", ".join(metadatas) + " ]"

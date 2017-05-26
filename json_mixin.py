"""
    This is Example of Python Mixin,
"""
import json


class Jsonizable(object):

    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.__dict__)
            

class DeserializeObj(Jsonizable):

    def __init__(self, **kwargs):
        self.created_at = kwargs.pop("created_at", None)
        self.tags = kwargs.pop("tags", None)


if __name__ == "__main__":
    meta = DeserializeObj()
    meta.created_at = 1234567
    meta.tags = ["Node",]

    meta_str = meta.to_json()
    print(meta_str)

    meta2 = DeserializeObj.from_json(meta_str)
    print(meta2.created_at)
    print(meta2.tags)
    print(meta2.to_json())


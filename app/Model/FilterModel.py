class FilterModel(object):
    def __init__(self):
        self.type = None
        self.subsvc = None
        self.submsg = None

    def set_filter_options(self, type: str, subsvc: int, submsg: int):
        self.type = type
        self.subsvc = subsvc
        self.submsg = submsg

    def get_filter_options(self):
        if self.type == "" and self.subsvc == 0 and self.submsg == 0:
            return None
        return {"type": self.type, "svc": self.subsvc, "msg": self.submsg}

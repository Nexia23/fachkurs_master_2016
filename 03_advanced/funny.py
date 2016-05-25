import funny_codes

class DeFunnyCodes(FunnyCodes):
    LETTER_GROUPS = [
        u"AÄEIOÖUÜY",
        u"BCDFGHJKLMNPQRSTVXZ",
        u"123456789",
    ]
    

class MyFunnyCodes(FunnyCodes):
    def generate_unique_set(self, n):
        res = []
        while len(res) < n:
            code = self.next()
            if not code in res:
                res.append(code)
        return res

    def next(self):
        """ Returns next random string """
        return u"".join(self._get()).lower()

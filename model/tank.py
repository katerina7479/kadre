# I'm an engineer, so I'm going to do a simple tank.
# It has a tag, and a max volume
# It's min volume is calculated when the max volume is set.
# They are all properties, so you can refer to them as
# MyTank.tag in the program.


class Tank(object):
    """Simple Tank"""
    def __init__(self, mytag, maxvolume):
        self.tag = mytag
        self.maxvolume = maxvolume

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = "TNK-" + str(value)

    @property
    def maxvolume(self):
        return self._maxvolume

    @property
    def minvolume(self):
        return self._minvolume

    @maxvolume.setter
    def maxvolume(self, value):
        self._maxvolume = value
        self._minvolume = int(value * 0.1)

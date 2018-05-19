class DiaCD(object):
    def __init__(self, ten, casy, sobaihat, gia):
        self.name = ten
        self.artist = casy
        self.track = sobaihat
        self.price = gia

    def in_danhsach(self):
        danhsach = '# ' + self.name + ' ' + self.artist + \
            ' ' + str(self.track) + ' ' + str(self.price)
        return(danhsach)

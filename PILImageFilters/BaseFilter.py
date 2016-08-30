class BaseFilter(object):

    def __init__(self, image):
        self.image = image.copy()
        self.width, self.height = self.image.size

    def apply(self):
        return self.image

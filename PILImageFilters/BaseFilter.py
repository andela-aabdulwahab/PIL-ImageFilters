class BaseFilter(object):

    def __init__(self, image):
        self.image = image.copy()

    def apply(self):
        return self.image

class Element:
    def __init__(self, type, value=None, children=[], siblings=None, parent=None):
        self.type = type
        self.value = value
        self.siblings = siblings or []
        self.parent = parent or []
        self.children = []
        self.addchildren(children)

    def addchild(self, element):
        if element is not None:
            self.children.append(element)
            element.parent = self

    def addchildren(self, elements):
        if elements is not None:
            for element in elements:
                if isinstance(element, list):
                    self.addchildren(element)
                else:
                    self.addchild(element)

            for element in self.children:
                element.siblings = [el for el in self.children if el is not element]

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.type)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

import abc

try:
    from abc import update_abstractmethods
except ImportError:
    def update_abstractmethods(cls):
        """Recalculate the set of abstract methods of an abstract class.

        If a class has had one of its abstract methods implemented after the
        class was created, the method will not be considered implemented until
        this function is called. Alternatively, if a new abstract method has been
        added to the class, it will only be considered an abstract method of the
        class after this function is called.

        This function should be called before any use is made of the class,
        usually in class decorators that add methods to the subject class.

        Returns cls, to allow usage as a class decorator.

        If cls is not an instance of ABCMeta, does nothing.
        """
        if not hasattr(cls, '__abstractmethods__'):
            # We check for __abstractmethods__ here because cls might by a C
            # implementation or a python implementation (especially during
            # testing), and we want to handle both cases.
            return cls
        abstracts = set()
        # Check the existing abstract methods of the parents, keep only the ones
        # that are not implemented.
        for scls in cls.__bases__:
            for name in getattr(scls, '__abstractmethods__', ()):
                value = getattr(cls, name, None)
                if getattr(value, "__isabstractmethod__", False):
                    abstracts.add(name)
        # Also add any other newly added abstract methods.
        for name, value in cls.__dict__.items():
            if getattr(value, "__isabstractmethod__", False):
                abstracts.add(name)
        cls.__abstractmethods__ = frozenset(abstracts)
        return cls

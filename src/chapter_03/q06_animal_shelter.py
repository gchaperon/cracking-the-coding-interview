import collections
import dataclasses
import typing as tp


@dataclasses.dataclass(eq=False)
class _Animal:
    name: str


class Cat(_Animal):
    pass


class Dog(_Animal):
    pass


T = tp.TypeVar("T")


class AnimalShelter:
    class ShelterItem(tp.NamedTuple, tp.Generic[T]):
        item: T
        position: int

    _cats: collections.deque[ShelterItem[Cat]]
    _dogs: collections.deque[ShelterItem[Dog]]

    def __init__(self) -> None:
        self._cats = collections.deque()
        self._dogs = collections.deque()

    def enqueue(self, animal: Cat | Dog) -> None:
        if isinstance(animal, Cat):
            self._cats.append(self.ShelterItem(animal, self._last_position + 1))
        elif isinstance(animal, Dog):
            self._dogs.append(self.ShelterItem(animal, self._last_position + 1))
        else:
            raise TypeError

    def dequeue_any(self) -> Cat | Dog:
        if not (self._cats or self._dogs):
            raise IndexError
        elif not self._cats:
            return self._dogs.popleft().item
        elif not self._dogs:
            return self._cats.popleft().item
        else:
            catitem, dogitem = self._cats[0], self._dogs[0]
            if catitem.position < dogitem.position:
                return self._cats.popleft().item
            else:
                return self._dogs.popleft().item

    def dequeue_dog(self) -> Dog:
        if not self._dogs:
            raise IndexError
        return self._dogs.popleft().item

    def dequeue_cat(self) -> Cat:
        if not self._cats:
            raise IndexError
        return self._cats.popleft().item

    @property
    def _last_position(self) -> int:
        max_cat = self._cats[0].position if self._cats else 0
        max_dog = self._dogs[0].position if self._dogs else 0
        return max(max_cat, max_dog)


# ******************** Tests ********************
def test_shelter() -> None:
    shelter = AnimalShelter()

    shelter.enqueue(Cat("misifu"))
    assert shelter.dequeue_any().name == "misifu"
    shelter.enqueue(Cat("michi"))
    assert shelter.dequeue_cat().name == "michi"
    shelter.enqueue(Dog("rex"))
    assert shelter.dequeue_dog().name == "rex"

    shelter.enqueue(Dog("dog2"))
    shelter.enqueue(Cat("cat2"))
    shelter.enqueue(Dog("dog1"))
    shelter.enqueue(Cat("cat1"))

    assert shelter.dequeue_dog().name == "dog2"
    assert shelter.dequeue_any().name == "cat2"
    assert shelter.dequeue_cat().name == "cat1"
    shelter.enqueue(Cat("cat_last"))
    assert shelter.dequeue_dog().name == "dog1"

#include <queue>
#include <tuple>
#include <vector>
#include <string>
#include <catch2/catch_test_macros.hpp>

enum class Type {
	Dog,
	Cat
};

struct Animal {
	Type type;
	std::string name = "";
};


struct ShelterQueue {
	size_t absolute_position = 0;
	std::queue<std::pair<Animal, size_t>> cats;
	std::queue<std::pair<Animal, size_t>> dogs;


	void enqueue(Animal animal) {
		switch (animal.type) {
		case Type::Cat:
			cats.push(std::make_pair(animal, absolute_position++));
			break;
		case Type::Dog:
			dogs.push(std::make_pair(animal, absolute_position++));
			break;
		}
	}

	Animal dequeueAny() {
		auto &queue = (std::get<1>(dogs.front()) < std::get<1>(cats.front())) ? dogs : cats;
		Animal animal = std::get<0>(queue.front());
		queue.pop();
		return animal;
	};

	Animal dequeueDog() {
		Animal dog = std::get<0>(dogs.front());
		dogs.pop();
		return dog;
	};

	Animal dequeueCat() {
		Animal cat = std::get<0>(cats.front());
		cats.pop();
		return cat;
	};

	bool isEmpty() {
		return false;
	}
};


TEST_CASE( "Test Shelter Queue" ) {
	ShelterQueue queue;

	queue.enqueue(Animal{Type::Dog, "rex"});
	REQUIRE( queue.dequeueAny().name == "rex" );
	queue.enqueue(Animal{Type::Dog, "rex"});
	REQUIRE( queue.dequeueDog().name == "rex" );

	queue.enqueue(Animal{Type::Cat, "misifu"});
	REQUIRE( queue.dequeueAny().name == "misifu" );
	queue.enqueue(Animal{Type::Cat, "misifu"});
	REQUIRE( queue.dequeueCat().name == "misifu" );

	queue.enqueue(Animal{Type::Dog, "rex"});
	queue.enqueue(Animal{Type::Dog, "max"});
	queue.enqueue(Animal{Type::Cat, "misifu"});
	REQUIRE( queue.dequeueAny().name == "rex" );
	REQUIRE( queue.dequeueAny().name == "max" );
	REQUIRE( queue.dequeueAny().name == "misifu" );

	std::vector<std::pair<Type, std::string>> animals {
		{Type::Dog, "dog 1"},
		{Type::Cat, "cat 1"},
		{Type::Dog, "dog 2"},
		{Type::Cat, "cat 2"},
		{Type::Dog, "dog 3"},
		{Type::Cat, "cat 3"}
	};
	for (auto&[type, name] : animals)
		queue.enqueue(Animal{type, name});

	REQUIRE( queue.dequeueCat().name == "cat 1" );
	REQUIRE( queue.dequeueAny().name == "dog 1" );
	REQUIRE( queue.dequeueAny().name == "dog 2" );
	REQUIRE( queue.dequeueDog().name == "dog 3" );
	REQUIRE( queue.dequeueAny().name == "cat 2" );
	REQUIRE( queue.dequeueCat().name == "cat 3" );
}

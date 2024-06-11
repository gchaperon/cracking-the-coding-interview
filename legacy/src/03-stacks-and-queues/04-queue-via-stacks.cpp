#include <stack>
#include <catch2/catch_test_macros.hpp>

enum class Direction {
	Forward,
	Backward
};

template<typename T>
struct Queue {
	std::stack<T> forward;
	std::stack<T> backward;

	void add(T item) {
		transferTo(Direction::Backward);
		backward.push(item);
	}

	void remove() {
		transferTo(Direction::Forward);
		forward.pop();
	}

	T peek() {
		transferTo(Direction::Forward);
		return forward.top();
	}

	bool isEmpty() {
		return backward.size() + forward.size() == 0;
	}

	void transferTo(Direction direction) {
		std::stack<T> &from = (direction == Direction::Forward) ? backward : forward;
		std::stack<T> &to = (direction == Direction::Forward) ? forward : backward;

		while (!from.empty()) {
			to.push(from.top());
			from.pop();
		}
	}
};

TEST_CASE( "Queue works" ) {
	Queue<int> queue;
	REQUIRE( queue.isEmpty() );

	queue.add(1);
	REQUIRE( queue.peek() == 1 );
	REQUIRE( !queue.isEmpty() );
	queue.add(2);
	queue.add(4);
	queue.add(123);
	REQUIRE( queue.peek() == 1 );
	queue.remove();
	queue.add(34);
	queue.add(12);
	REQUIRE( queue.peek() == 2 );
	queue.remove();
	REQUIRE( queue.peek() == 4 );
	queue.remove();
	queue.add(432);
	REQUIRE( queue.peek() == 123 );
	queue.remove();
	REQUIRE( queue.peek() == 34 );
	queue.remove();
	REQUIRE( queue.peek() == 12 );
	queue.remove();
	REQUIRE( queue.peek() == 432 );
	queue.remove();
	REQUIRE( queue.isEmpty() );

	int nelements = 100;
	for (int i = 0; i < nelements; i++)
		queue.add(i);
	for (int i = 0; i < nelements; i++) {
		REQUIRE( queue.peek() == i );
		queue.remove();
	}
	REQUIRE( queue.isEmpty() );




}

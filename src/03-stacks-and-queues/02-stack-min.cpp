#include <iostream>
#include <stack>
#include <catch2/catch_test_macros.hpp>

template<typename T>
struct MinStack {
	std::stack<T> data;
	std::stack<T> mins;
	void pop() {
		int value = data.top();
		data.pop();
		if (value == mins.top())
			mins.pop();
	}
	
	void push(T value) {
		data.push(value);
		if (mins.empty() || value <= mins.top())
			mins.push(value);
	}

	T peek() {
		return data.top();
	}

	bool isEmpty() {
		return data.empty();
	}

	T min() {
		return mins.top();
	}
};

TEST_CASE( "Keeps track of min" ) {
	MinStack<int> stack;

	REQUIRE( stack.isEmpty() );

	stack.push(3);
	REQUIRE_FALSE( stack.isEmpty() );
	REQUIRE( stack.peek() == 3 );
	REQUIRE( stack.min() == 3 );


	stack.push(5);
	stack.push(1);
	stack.push(2);
	stack.push(10);
	REQUIRE( stack.peek() == 10 );
	REQUIRE( stack.min() == 1 );

	stack.pop();
	REQUIRE( stack.peek() == 2 );
	REQUIRE( stack.min() == 1 );

	stack.pop();
	REQUIRE( stack.peek() == 1 );
	REQUIRE( stack.min() == 1 );

	stack.pop();
	REQUIRE( stack.peek() == 5 );
	REQUIRE( stack.min() == 3 );

	stack.pop();
	stack.pop();
	REQUIRE( stack.isEmpty() );

	stack.push(2);
	REQUIRE( stack.min() == 2 );
	stack.push(1);
	REQUIRE( stack.min() == 1 );
	stack.push(1);
	stack.pop();
	REQUIRE( stack.min() == 1 );
	stack.pop();
	REQUIRE( stack.min() == 2 );
	stack.pop();
	REQUIRE( stack.isEmpty() );
}

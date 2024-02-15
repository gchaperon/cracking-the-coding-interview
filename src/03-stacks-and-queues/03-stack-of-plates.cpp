#include <vector>
#include <iostream>
#include <stack>
#include <catch2/catch_test_macros.hpp>

template<typename T>
struct SetOfStacks {
	int maxheight;
	std::stack<std::stack<T>> stacks{};
	

	void pop() {
		stacks.top().pop();
		if (stacks.top().empty())
			stacks.pop();
	}

	void push(T value) {
		if (stacks.empty() || static_cast<int>(stacks.top().size()) == maxheight) {
			std::stack<T> newtop;
			newtop.push(value);
			stacks.push(newtop);
		} else {
			stacks.top().push(value);
		}
	}

	T peek() {
		return stacks.top().top();
	}

	bool isEmpty() {
		return stacks.empty();
	}

};

int ceildiv(int m, int n) {
	return (m + n - 1) / n;
}

TEST_CASE( "Set of stacks has same interface as single stack" ) {
	int maxheight = 3;
	SetOfStacks<int> stack{maxheight};

	// Same tests as base stack impl
	REQUIRE( stack.isEmpty() );
	stack.push(1);
	REQUIRE( stack.peek() == 1 );
	REQUIRE( !stack.isEmpty() );
	stack.push(2);
	stack.push(4);
	stack.push(123);
	REQUIRE( stack.peek() == 123 );
	stack.pop();
	REQUIRE( stack.peek() == 4 );
	stack.pop();
	REQUIRE( stack.peek() == 2 );
	stack.pop();
	REQUIRE( stack.peek() == 1 );
	stack.pop();
	REQUIRE( stack.isEmpty() );

	// tests specifically for SetOfStacks
	int nelements = 100;
	for (int i = 0; i < nelements; i++)
		stack.push(i);
	REQUIRE( stack.peek() == nelements - 1 );
	REQUIRE( static_cast<int>(stack.stacks.size()) == ceildiv(nelements, maxheight) );

	for (int i = 0; i < nelements; i++)
		stack.pop();
	REQUIRE( stack.isEmpty() );
}

template<typename T>
struct SetOfStacksPopIndex {
	int maxheight;
	std::vector<std::stack<T>> stacks{};
	
	void pop() {
		stacks.back().pop();
		if (stacks.back().empty())
			stacks.pop_back();
	}

	void push(T value) {
		if (stacks.empty() || static_cast<int>(stacks.back().size()) == maxheight) {
			std::stack<T> newtop;
			newtop.push(value);
			stacks.push_back(newtop);
		} else {
			stacks.back().push(value);
		}
	}

	T peek() {
		return stacks.back().top();
	}

	bool isEmpty() {
		return stacks.empty();
	}

	void popAt(int index) {
		stacks[index].pop();
	}
};


TEST_CASE( "Test popAt(index)" ) {
	int maxheight = 3;
	SetOfStacksPopIndex<int> stack{maxheight};

	// Same tests as base stack impl
	REQUIRE( stack.isEmpty() );
	stack.push(1);
	REQUIRE( stack.peek() == 1 );
	REQUIRE( !stack.isEmpty() );
	stack.push(2);
	stack.push(4);
	stack.push(123);
	REQUIRE( stack.peek() == 123 );
	stack.pop();
	REQUIRE( stack.peek() == 4 );
	stack.pop();
	REQUIRE( stack.peek() == 2 );
	stack.pop();
	REQUIRE( stack.peek() == 1 );
	stack.pop();
	REQUIRE( stack.isEmpty() );

	// tests same interface as SetOfStacks
	int nelements = 100;
	for (int i = 0; i < nelements; i++)
		stack.push(i);
	REQUIRE( stack.peek() == nelements - 1 );
	REQUIRE( static_cast<int>(stack.stacks.size()) == ceildiv(nelements, maxheight) );

	for (int i = 0; i < nelements; i++)
		stack.pop();
	REQUIRE( stack.isEmpty() );


	// specific tests for SetOfStacksPopIndex
	nelements = 10;
	for (int i = 0; i < nelements; i++)
		stack.push(i);
	REQUIRE( stack.peek() == nelements - 1 );
	REQUIRE( static_cast<int>(stack.stacks.size()) == ceildiv(nelements, maxheight) );

	stack.popAt(0);
	REQUIRE( stack.stacks[0].top() == 1 );
	REQUIRE( stack.stacks[1].top() == 5 );
	for (int i = 0; i < nelements - 1; i++)
		stack.pop();
	REQUIRE( stack.isEmpty() );
}

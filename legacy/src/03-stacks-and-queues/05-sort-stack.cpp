#include <limits>
#include <cstdlib>
#include <stack>
#include <catch2/catch_test_macros.hpp>

void sort(std::stack<int> &stack) {
	std::stack<int> temp;

	while ( !stack.empty() ) {
		int value = stack.top();
		stack.pop();
		int nmoved;
		for (nmoved=0; !temp.empty() && temp.top() > value; nmoved++,temp.pop())
			stack.push(temp.top());
		temp.push(value);
		for ( ; nmoved; nmoved--,stack.pop())
			temp.push(stack.top());
	}
	for ( ; !temp.empty(); temp.pop())
		stack.push(temp.top());
}

bool sorted(std::stack<int>  stack) {
	int last = std::numeric_limits<int>::min();
	for ( ; !stack.empty(); stack.pop()) {
		int current = stack.top();
		if (current < last) return false;
		last = current;
	}
	return true;
}

TEST_CASE( "Check sorted function works" ) {
	std::stack<int> stack;
	REQUIRE( sorted(stack) );

	stack.push(10);
	REQUIRE( sorted(stack) );
	stack.push(4);
	stack.push(2);
	stack.push(1);
	stack.push(-3);
	REQUIRE( sorted(stack) );

	stack = {};
	REQUIRE( stack.empty() );
	stack.push(1);
	stack.push(2);
	REQUIRE_FALSE( sorted(stack) );
	stack.push(-2);
	REQUIRE_FALSE( sorted(stack) );
}

TEST_CASE( "Sorts stack" ) {
	int nrepeat = 10, nelements = 100;

	for (int repeat = 0; repeat < nrepeat; repeat++) {
		std::stack<int> stack;
		for (int el = 0; el < nelements; el++) {
			int value = std::rand();
			stack.push(value);
		}
		sort(stack);
		REQUIRE( sorted(stack) );
	}
}

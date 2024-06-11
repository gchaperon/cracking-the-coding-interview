#include <sstream>
#include <iostream>
#include <vector>
#include <catch2/catch_test_macros.hpp>


template<typename T>
struct MultiStackFixed {
	int nstacks;
	int stacksize;
	std::vector<T> data;
	std::vector<int> heads;

	MultiStackFixed(int nstacks, int stacksize)
		: nstacks(nstacks)
		, stacksize(stacksize)
		, data(nstacks * stacksize)
		, heads(nstacks, -1)
	{}

	void pop(int i) {
		if ( isEmpty(i) ) {
			std::stringstream ss;
			ss << "Stack " << i << " is empty.";
			throw std::runtime_error(ss.str());
		}
		int &head = heads.at(i);
		if ( head == i * stacksize )
			head = -1;
		else
			heads.at(i)--;
	}

	void push(int i, T value) {
		if ( isFull(i) ) {
			std::stringstream ss;
			ss << "Stack " << i << " is full.";
			throw std::runtime_error(ss.str());
		}
		int &head = heads.at(i);
		if ( isEmpty(i) )
			head = i * stacksize;
		else
			head++;
		data[head] = value;
	}


	T peek(int i) {
		if ( isEmpty(i) ) {
			std::stringstream ss;
			ss << "Stack " << i << " is empty.";
			throw std::runtime_error(ss.str());
		}
		return data.at(heads.at(i));
	}

	bool isFull(int i) {
		return heads.at(i) == stacksize * (i + 1) - 1;
	}
	bool isEmpty(int i) {
		return heads.at(i) == -1;
	}
};

TEST_CASE( "Fixed size" ) {
	int stacksize = 10;
	MultiStackFixed<char> stacks(3, stacksize);

	// all stacks are initialized empty
	for (int i = 0; i < stacks.nstacks; i++)
		REQUIRE( stacks.isEmpty(i) );

	// push works
	// push to one keeps others empty
	stacks.push(0, 'a');
	REQUIRE( stacks.peek(0) == 'a' );
	REQUIRE_FALSE( stacks.isEmpty(0) );
	REQUIRE( stacks.isEmpty(1) );
	REQUIRE( stacks.isEmpty(2) );

	// filling one raises
	// filling one keeps others empty
	for (int i = 1; i < stacksize; i++)
		stacks.push(0, 'a' + i);
	REQUIRE_THROWS( stacks.push(0, 'z') );
	REQUIRE( stacks.isEmpty(1) );
	REQUIRE( stacks.isEmpty(2) );
	
	// check peek + pop
	REQUIRE( stacks.peek(0) == 'j' );
	stacks.pop(0);
	stacks.pop(0);
	REQUIRE( stacks.peek(0) == 'h' );
	

	// push random elements to stacks independently, check peek
	stacks.push(1, 'b');
	stacks.push(2, 'c');
	stacks.push(2, 'd');
	stacks.push(2, 'e');
	REQUIRE_FALSE( stacks.isEmpty(1) );
	REQUIRE_FALSE( stacks.isEmpty(2) );
	REQUIRE( stacks.peek(2) == 'e' );
	REQUIRE( stacks.peek(1) == 'b' );
	REQUIRE( stacks.peek(0) == 'h' );
	stacks.pop(1);
	REQUIRE( stacks.isEmpty(1) );
	for (int i = 0; i < 3; i++)
		stacks.pop(2);
	REQUIRE( stacks.isEmpty(2) );

	// check peek and pop on empty throws
	for (int i = 0; i < 8; i++)
		stacks.pop(0);
	REQUIRE( stacks.isEmpty(0) );
	REQUIRE_THROWS( stacks.peek(0) );
	REQUIRE_THROWS( stacks.pop(0) );
}

/*
 * The implementation of the multi stack with variable size is too long.
 * I won't do it.
 *
 */
TEST_CASE( "Variable size" ) {
}

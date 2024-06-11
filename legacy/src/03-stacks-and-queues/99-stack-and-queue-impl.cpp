#include <catch2/catch_test_macros.hpp>

template<typename T>
struct Node {
	T data;
	Node *next = nullptr;
};

template<typename T>
struct Stack {
	Node<T> *head = nullptr;

	~Stack() {
		while (head) {
			Node<T> *tmp = head;
			head = head->next;
			delete tmp;
		}
	}

	void pop() {
		if (isEmpty()) throw std::runtime_error("Stack is empty");
		Node<T> *tmp = head;
		head = head->next;
		delete tmp;
	}

	void push(T value) {
		Node<T> *node = new Node<T>{value, head};
		head = node;
	}

	T peek() {
		if (isEmpty()) throw std::runtime_error("Stack is empty");
		return head->data;
	}

	bool isEmpty() {
		return head == nullptr;
	}
};


TEST_CASE( "Stack works" ) {
	Stack<int> stack;
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
}

template<typename T>
struct Queue {
	Node<T> *head = nullptr;
	Node<T> *tail = nullptr;

	~Queue() {
		while ( head ) {
			Node<T> *tmp = head;
			head = head->next;
			delete tmp;
		}
	}

	void add(T item) {
		Node<T> *last = new Node<T>{item};
		if ( isEmpty() ) head = tail = last;
		else {
			tail->next = last;
			tail = last;
		}
	}

	void remove() {
		if (isEmpty()) throw std::runtime_error("Queue is empty");
		if (head == tail) tail = nullptr;
		Node<T> *tmp = head;
		head = head->next;
		delete tmp;
	}

	T peek() {
		if (isEmpty()) throw std::runtime_error("Queue is empty");
		return head->data;
	}

	bool isEmpty() {
		return head == nullptr and tail == nullptr;
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
	REQUIRE( queue.peek() == 2 );
	queue.remove();
	REQUIRE( queue.peek() == 4 );
	queue.remove();
	REQUIRE( queue.peek() == 123 );
	queue.remove();
	REQUIRE( queue.isEmpty() );

}

#include <stack>
#include <iostream>
#include <concepts>
#include <catch2/catch_test_macros.hpp>


// begin linked list node definition
template<typename T>
concept Streamable = 
	requires(std::ostream &os, T value) {
		{ os << value } -> std::convertible_to<std::ostream &>;
	};

template<typename T>
concept NodeData = std::equality_comparable<T> && std::default_initializable<T> && Streamable<T>;

template<NodeData T>
struct Node {
	T data;
	Node *next;

	Node() : data(), next(nullptr) {}
	Node(const T& new_data) : data(new_data), next(nullptr) {}

};

template<NodeData T>
std::ostream& operator<<(std::ostream& os, const Node<T>* node) {
	if (node == nullptr) return os;
	const Node<T> *p = node;
	os << p -> data;
	while ((p = p -> next) != nullptr) {
		os << " -> " << p -> data;
	}
	return os;
}

template<NodeData T>
bool listequal(const Node<T>* head1, const Node<T>* head2) {
	while (head1 != nullptr && head2 != nullptr) {
		if (head1->data != head2->data)
			return false;

		head1 = head1->next;
		head2 = head2->next;
	}
	if (head1 || head2) return false;
	return true;
}

template<NodeData T>
Node<T>* make_list() {
    return nullptr;
}

template<NodeData T, typename... Args>
Node<T>* make_list(const T& value, const Args&... args) {
    Node<T>* head = new Node<T>(value);
    head->next = make_list<T>(args...);
    return head;
}

template<NodeData T>
void delete_list(Node<T>* head) {
	Node<T> *current = head;
	while (current != nullptr) {
		Node<T> *next = current -> next;
		delete current;
		current = next;
	}
}
// end linked list node definition



bool is_palindrome(Node<char> *head) {
	int length = 0, i;
	Node<char> *index;
	for (index = head; index; index=index->next) length++;

	std::stack<char> stack;
	// store first half
	for (i=0, index=head; i < length / 2; i++, index=index->next)
		stack.push(index->data);
	// skip mid element if length is odd
	if (length%2 == 1)
		index = index->next;
	// check last half, popping from stack
	for (i=0; i<length/2; i++, index=index->next, stack.pop())
		if (index->data != stack.top())
			return false;
	return true;
}

TEST_CASE( "Is palindrome" ) {
	Node<char> *l;
	l = make_list<char>();
	REQUIRE( is_palindrome(l) );
	delete_list(l);

	l = make_list('a');
	REQUIRE( is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'a');
	REQUIRE( is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'b');
	REQUIRE( !is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'b', 'a');
	REQUIRE( is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'b', 'b', 'a');
	REQUIRE( is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'a', 'c', 'c', 'b', 'c', 'c', 'a', 'a');
	REQUIRE( is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'b', 'c');
	REQUIRE( !is_palindrome(l) );
	delete_list(l);

	l = make_list('a', 'a', 'c', 'b', 'c', 'c', 'a', 'a');
	REQUIRE( !is_palindrome(l) );
	delete_list(l);
}

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

int kth_to_last(unsigned int k, Node<int>* head) {
	// I will use python convention of last element being arr[-1],
	// so kth_to_last(1, {1, 2, 3}) == 3 and kth_to_last(3, {1, 2, 3}) == 1

	// clamp k to 1, else the algorithm fails
	k = k ? k : 1;

	// two pointer, move one k steps forward
	Node<int> *front = head, *back = head;
	for (; front != nullptr && k; k--)
		front = front->next;

	if (k) {} // throw error

	while (front != nullptr) {
		front = front->next;
		back = back->next;
	}
	return back->data;
}


TEST_CASE( "Returns kth to last" ) {
	Node<int>* list = make_list(1, 2, 3, 4, 5);
	REQUIRE( kth_to_last(0, list) == 5 ); // clamps to ends, should throw error, but I won't handle this case for this exercise.
	REQUIRE( kth_to_last(1, list) == 5 );
	REQUIRE( kth_to_last(2, list) == 4 );
	REQUIRE( kth_to_last(3, list) == 3 );
	REQUIRE( kth_to_last(5, list) == 1 );
	REQUIRE( kth_to_last(6, list) == 1 ); // clamps to ends, should throw error.
	REQUIRE( kth_to_last(10, list) == 1 );
	delete_list(list);

	list = make_list(42);
	REQUIRE( kth_to_last(1, list) == 42 );
	delete_list(list);
}

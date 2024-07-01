#include <iostream>
#include <concepts>
#include <catch2/catch_test_macros.hpp>

// begin linked list node definition
#define MAX_PRINT 20

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
	unsigned int counter = 1;
	while ((p = p -> next) != nullptr) {
		if (counter++ >= MAX_PRINT) break;
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
Node<char>* at(unsigned int i, Node<char>* head) {
	while (head != nullptr && i-- > 0) head = head->next;
	return head;
}

Node<char> *find_loop(Node<char> *head) {
	Node<char> *slow, *fast;
	slow = fast = head;
	// make slow and fast meet
	bool start = true;
	for ( ; start || (slow != fast); slow=slow->next, fast=fast->next->next, start=false) ;
	// advance head and slow until they meet
	for ( ; slow != head; slow=slow->next, head=head->next) ;
	// where they meet is the beginning of the loop
	return head;
}

TEST_CASE( "Finds loop" ) {
	Node<char> *list, *result;

	// book example
	list = make_list('A', 'B', 'C', 'D', 'E');
	at(4, list)->next = at(2, list);
	result = find_loop(list);
	REQUIRE( result == at(2, list) );
	at(4, list)->next = nullptr;
	delete_list(list);

	// list is full loop
	list = make_list('a', 'b', 'c', 'd');
	at(3, list)->next = at(0, list);
	result = find_loop(list);
	REQUIRE( result == at(0, list) );
	at(3, list)->next = nullptr;
	delete_list(list);

	// smallest full loop
	list = make_list('a');
	at(0, list)->next = at(0, list);
	result = find_loop(list);
	REQUIRE( result == at(0, list) );
	at(0, list)->next = nullptr;
	delete_list(list);

	// list with tiny loop at the end
	list = make_list('A', 'B', 'C', 'D', 'E');
	at(4, list)->next = at(3, list);
	result = find_loop(list);
	REQUIRE( result == at(3, list) );
	at(4, list)->next = nullptr;
	delete_list(list);

	// long list with tiny loop at end
	list = make_list('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j');
	at(9, list)->next = at(7, list);
	result = find_loop(list);
	REQUIRE( result == at(7, list) );
	at(9, list)->next = nullptr;
	delete_list(list);

	// long list with somewhat long loop
	list = make_list('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j');
	at(9, list)->next = at(3, list);
	result = find_loop(list);
	REQUIRE( result == at(3, list) );
	at(9, list)->next = nullptr;
	delete_list(list);
}

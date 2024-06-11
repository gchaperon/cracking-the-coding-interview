#include <unordered_set>
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

void partition(Node<int> **headptr, int k) {
	Node<int> *head = *headptr;
	if (head == nullptr) return ;

	Node<int> *last, *index, *first, *prev;
	// first is dummy node
	first = new Node(0);
	first->next = head;
	prev = first;
	last = index = head;
	while (last->next != nullptr) last = last->next;

	// at this point I have a pointer to a "dummy" node before head, a
	// pointer to the last element of the list, a pointer to head which
	// will be used to traverse the list and a pointer to the node before
	// index
	while (index != last) {
		if (index->data >= k) {
			Node<int> *next = index->next;
			prev->next = next;
			index->next = last->next;
			last->next = index;
			index = next;
		} else {
			prev = index;
			index = index->next;
		}
	}
	*headptr = first->next;
	delete first;
}

bool is_partitioned(Node<int> *head, int k) {
	bool first_half = true;
	while (head != nullptr) {
		if (head->data >= k && first_half)
			first_half = false;
		if (first_half == (head->data >= k))
			return false;
		head = head->next;
	}
	return true;
}

std::unordered_multiset<int> to_multiset(Node<int> *head) {
	std::unordered_multiset<int> s;
	if (head != nullptr)
		do s.insert(head->data);
	       	while ((head=head->next) != nullptr);
	return s;
}


TEST_CASE( "is_partitioned works" ) {
	Node<int> *l = make_list(1, 2, 3, 4, 5);
	REQUIRE( is_partitioned(l, 3) );
	delete_list(l);

	l = make_list(4, 1, 2, 3);
	REQUIRE( !is_partitioned(l, 2) );
	delete_list(l);

	l = make_list(3, 5, 8, 5, 10, 2, 1);
	REQUIRE( !is_partitioned(l, 5) );
	delete_list(l);

	l = make_list(3, 1, 2, 10, 5, 5, 8);
	REQUIRE( is_partitioned(l, 5) );
	delete_list(l);

	l = make_list(1, 2, 3, 4, 5);
	REQUIRE( is_partitioned(l, 0) );
	delete_list(l);

	l = make_list(1, 2, 3, 4, 5);
	REQUIRE( is_partitioned(l, 10) );
	delete_list(l);
}

TEST_CASE( "Converts to multiset" ) {
	Node<int> *l = make_list(1, 2, 3, 4, 5);
	REQUIRE(to_multiset(l) == std::unordered_multiset{1, 2, 3, 4, 5} );
	delete_list(l);

	l = make_list(3, 5, 8, 5, 10, 2, 1);
	REQUIRE( to_multiset(l) == std::unordered_multiset{3, 5, 8, 5, 10, 2, 1} );
	delete_list(l);

	l = make_list<int>();
	REQUIRE( to_multiset(l) == std::unordered_multiset<int>() );
	delete_list(l);
}


TEST_CASE( "Partitions" ) {
	Node<int> *l = make_list(3, 5, 8, 5, 10, 2, 1);
	int x = 5;
	std::unordered_multiset items = to_multiset(l);
	partition(&l, x);
	REQUIRE( is_partitioned(l, x) );
	REQUIRE( items == to_multiset(l) );
	delete_list(l);

	// test empty list
	l = make_list<int>();
	x = 5;
	partition(&l, x);
	REQUIRE( is_partitioned(l, x) );
	REQUIRE( std::unordered_multiset<int>() == to_multiset(l) );
	delete_list(l);

	// test only left partition
	l = make_list(3, 5, 8, 5, 10, 2, 1);
	x = 20;
	items = to_multiset(l);
	partition(&l, x);
	REQUIRE( is_partitioned(l, x) );
	REQUIRE( items == to_multiset(l) );
	delete_list(l);	

	// test only right partition
	l = make_list(3, 5, 8, 5, 10, 2, 1);
	x = 0;
	items = to_multiset(l);
	partition(&l, x);
	REQUIRE( is_partitioned(l, x) );
	REQUIRE( items == to_multiset(l) );
	delete_list(l);
}

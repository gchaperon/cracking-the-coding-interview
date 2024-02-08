#include <cmath>
#include <tuple>
#include <utility>
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

std::pair<int, int> divmod(int n, int m) {
	int div = n / m;
	int mod = n % m;
	return std::make_pair(div, mod);
}

Node<int> *sum_lists(Node<int> *h1, Node<int> *h2) {
	Node<int> *anchor, *last, *head, *tail; 
	anchor = last = new Node<int>();
	int ndata, carry = 0;

	for ( ;
		h1 || h2 || carry;
		h1 = h1 ? h1->next : h1, h2 = h2 ? h2->next : h2
	) {
		std::tie(carry, ndata) = divmod((h1 ? h1->data : 0) + (h2 ? h2->data : 0) + carry, 10);
		tail = new Node<int>(ndata);
		last->next = tail;
		last = last->next;
	}
	head = anchor->next;
	delete anchor;
	return head;
}

std::pair<Node<int>*, int> sum_lists_forward_helper(Node<int> *h1, Node<int> *h2) {
	if (h1 == nullptr && h2 == nullptr)
		return std::make_pair(nullptr, 0);
	int carry, value;
	Node<int> *digits;
	std::tie(digits, carry) = sum_lists_forward_helper(h1 ? h1->next : nullptr, h2 ? h2->next : nullptr);
	std::tie(carry, value) = divmod((h1 ? h1->data : 0) + (h2 ? h2->data : 0) + carry, 10);
	Node<int> *head = new Node(value);
	head->next = digits;
	return std::make_pair(head, carry);
}

Node<int> *sum_lists_forward(Node<int> *h1, Node<int> *h2) {
	int l1 = 0, l2 = 0;
	Node<int> *i1 = h1, *i2 = h2;
	for (; i1; i1=i1->next, l1++) ;
	for (; i2; i2=i2->next, l2++) ;

	Node<int> *padded = (l1 < l2) ? h1 : h2;
	Node<int> *longest = (l1 < l2) ? h2 : h1;

	for (int i = 0; i < std::abs(l1 - l2); i++) {
		Node<int> *node = new Node(0);
		node->next = padded;
		padded = node;
	}
	// at this point both lists are the same length and the shortest is
	// padded with 0
	auto [head, carry] = sum_lists_forward_helper(padded, longest);
	if (carry) {
		Node<int> *new_head = new Node(carry);
		new_head->next = head;
		head = new_head;
	}
	if (l1 != l2) {
		// delete padding nodes
		i1 = padded;
		for ( ; i1->next->data != 0; i1=i1->next) ;
		i1->next = nullptr;
		delete_list(padded);
	}
	return head;
}


TEST_CASE( "Sums (reversed digits)" ) {
	Node<int> *l1, *l2, *result, *target;
	// Book example
	l1 = make_list(7, 1, 6);
	l2 = make_list(5, 9, 2);
	result = sum_lists(l1, l2);
	target = make_list(2, 1, 9);
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);

	// Empty lists
	l1 = make_list<int>();
	l2 = make_list<int>();
	result = sum_lists(l1, l2);
	target = make_list<int>();
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);

	// Lists of different lengths
	l1 = make_list(7);
	l2 = make_list(5, 9, 2, 3);
	result = sum_lists(l1, l2);
	target = make_list(2, 0, 3, 3);
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);

	// Ultimate carry over / resulting list longer than both
	l1 = make_list(1);
	l2 = make_list(9, 9, 9, 9);
	result = sum_lists(l1, l2);
	target = make_list(0, 0, 0, 0, 1);
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);
	
	// Example of hint 95
	l1 = make_list(9, 7, 8);
	l2 = make_list(6, 8, 5);
	result = sum_lists(l1, l2);
	target = make_list(5, 6, 4, 1);
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);
}

TEST_CASE( "Sums (forward digits)" ) {
	Node<int> *l1, *l2, *result, *target;
	// Book example
	l1 = make_list(6, 1, 7);
	l2 = make_list(2, 9, 5);
	result = sum_lists_forward(l1, l2);
	target = make_list(9, 1, 2);

	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);

	// Empty lists
	l1 = make_list<int>();
	l2 = make_list<int>();
	result = sum_lists_forward(l1, l2);
	target = make_list<int>();
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);

	// Lists of different lengths
	l1 = make_list(7);
	l2 = make_list(3, 2, 9, 5);
	result = sum_lists_forward(l1, l2);
	target = make_list(3, 3, 0, 2);
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);

	// Ultimate carry over / resulting list longer than both
	l1 = make_list(1);
	l2 = make_list(9, 9, 9, 9);
	result = sum_lists_forward(l1, l2);
	target = make_list(1, 0, 0, 0, 0);
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(result);
	delete_list(target);
}

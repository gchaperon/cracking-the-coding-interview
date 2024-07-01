#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>
#include <catch2/catch_test_macros.hpp>


bool is_ascii_letter(unsigned char c) {
	return (c >= 65 && c <= 90) || (c >= 97 && c <= 122);
}


bool is_palindrome_permutation(std::string str) {
	std::transform(begin(str), end(str), begin(str), [](unsigned char c){ return std::tolower(c); });
	std::unordered_map<unsigned char, int> map;

	int nchars = 0;
	for (unsigned char c: str) {
		if (is_ascii_letter(c)) {
			map[c]++;
			nchars++;
		}
	}

	if (nchars % 2 == 1) {
		auto is_value_odd = [](const std::pair<unsigned char, int>& pair) {
			return pair.second % 2 == 1;
		};
		std::unordered_map<unsigned char, int>::iterator it =
			std::find_if(begin(map), end(map), is_value_odd);
		if (it == end(map)) {
			return false;
		}
		map.erase(it);
	}

	auto is_value_pair = [](const std::pair<unsigned char, int>& pair) {
		return pair.second % 2 == 0;
	};
	return all_of(begin(map), end(map), is_value_pair);
}


TEST_CASE( "Finds Palindrome Permutations" ) {
	REQUIRE( is_palindrome_permutation("Tact Coa") ); // taco cat; example from the book
	REQUIRE( is_palindrome_permutation("aancaa aa am  aalpmannnpl") ); // A man, a plan, a canal: Panama!
	REQUIRE( is_palindrome_permutation("nna aalapp caalma mnaaa  n") ); // A man, a plan, a canal: Panama!
	REQUIRE( is_palindrome_permutation(" appanaaa a lmam cnaanlna") ); // A man, a plan, a canal: Panama!
	REQUIRE( is_palindrome_permutation("aa aa  n gnsslmhgag l imao agahoi") ); // Go hang a salami, I'm a lasagna hog
	REQUIRE( is_palindrome_permutation("iggo mgomngaasahaaian hlsala") ); // Go hang a salami, I'm a lasagna hog

	REQUIRE( !is_palindrome_permutation("Tactr Coa") );
	REQUIRE( !is_palindrome_permutation("zijfadm") );
	REQUIRE( !is_palindrome_permutation("opsmgpiukxhdwdcvc") );
	REQUIRE( !is_palindrome_permutation("eb qgyhm nbyd") );
}

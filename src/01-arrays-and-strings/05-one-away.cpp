#include <string>
#include <catch2/catch_test_macros.hpp>


enum class Distance : int {
	ZERO = 0,
	ONE = 1,
	MORE = 2
};


Distance from_integer(unsigned int value) {
	switch (value) {
		case 0:
			return Distance::ZERO;
		case 1:
			return Distance::ONE;
		default:
			return Distance::MORE;
	}
}


Distance operator+(Distance lhs, Distance rhs) {
	int result = static_cast<int>(lhs) + static_cast<int>(rhs);
	return from_integer(result);
}


Distance tiny_levenshtein(std::string s1, std::string s2, Distance accumulated) {
	if (accumulated == Distance::MORE)
		return accumulated;
	else if (s1.size() == 0)
		return from_integer(s2.size());
	else if (s2.size() == 0)
		return from_integer(s1.size());
	else if (s1[0] == s2[0])
		return tiny_levenshtein(s1.substr(1), s2.substr(1), accumulated);
	else {
		return std::min({
			tiny_levenshtein(s1.substr(1), s2, accumulated + Distance::ONE),
			tiny_levenshtein(s1, s2.substr(1), accumulated + Distance::ONE),
			tiny_levenshtein(s1.substr(1), s2.substr(1), accumulated + Distance::ONE)
		});
	}
}


bool one_away(std::string s1, std::string s2) {
	switch (tiny_levenshtein(s1, s2, Distance::ZERO)) {
		case Distance::ZERO:
		case Distance::ONE:
			return true;
		case Distance::MORE:
		default:
			return false;
	}
}


TEST_CASE( "Checks one away" ) {
	REQUIRE( one_away("", "") );
	REQUIRE( one_away("pale", "ple") );
	REQUIRE( one_away("pales", "pale") );
	REQUIRE( one_away("pale", "bale") );
	REQUIRE( !one_away("pale", "bake") );
	REQUIRE( !one_away("asdf", "asdfqwer") );
}

#include <unordered_set>
#include <string_view>
#include <catch2/catch_test_macros.hpp>


bool is_permutation( std::string_view s1, std::string_view s2 ) {
	using set = std::unordered_multiset<char>;
	return set(begin(s1), end(s1)) == set(begin(s2), end(s2));
}


TEST_CASE( "Is permutation" ) {
	REQUIRE( is_permutation("", "") );
	REQUIRE( is_permutation("aaa", "aaa") );
	REQUIRE( is_permutation("abb", "bab") );
	REQUIRE( is_permutation("tom marvolo riddle ", "i am lord voldemort") );
	REQUIRE( !is_permutation("a", "aa") );
	REQUIRE( !is_permutation("abb", "aba") );
	REQUIRE( !is_permutation("harry potter", "voldemort") );
	REQUIRE( !is_permutation("Hola", "hola") );
}

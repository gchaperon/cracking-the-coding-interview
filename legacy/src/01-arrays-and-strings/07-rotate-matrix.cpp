#include <utility>
#include <vector>
#include <catch2/catch_test_macros.hpp>


using Matrix = std::vector<std::vector<int>>;


std::pair<int, int> rotate_index(int i, int j, int n) {
	int new_i = j;
	int new_j = n - 1 - i;
	return std::make_pair(new_i, new_j);
}


int ceildiv(int a, int b) {
	return (a + b - 1) / b;
}


Matrix rotate(Matrix matrix) {
	int n = matrix.size();

	for (int i = 0; i < n / 2; i++) {
		for (int j = 0; j < ceildiv(n, 2); j++) {
			int u = i;
			int v = j;
			int value = matrix[u][v];
			for (int k = 0; k < 4; k++) {
				const auto [newu, newv] = rotate_index(u, v, n);
				int tmp = matrix[newu][newv];
				matrix[newu][newv] = value;
				u = newu;
				v = newv;
				value = tmp;
			}
		}
	}
	return matrix;
}


TEST_CASE( "Rotates" ) {
	REQUIRE( rotate(Matrix{}) == Matrix{} );
	REQUIRE( rotate(Matrix{{3}}) == Matrix{{3}} );
	REQUIRE( rotate(Matrix{{1, 2},
												 {3, 4}})
							 == Matrix{{3, 1},
											   {4, 2}} );

	REQUIRE( rotate(Matrix{{1, 2, 3},
												 {4, 5, 6},
												 {7, 8, 9}})
							 == Matrix{{7, 4, 1},
							 					 {8, 5, 2},
												 {9, 6, 3}} );

	REQUIRE( rotate(Matrix{{ 1,  2,  3,  4},
												 { 5,  6,  7,  8},
												 { 9, 10, 11, 12},
												 {13, 14, 15, 16}})
							 == Matrix{{13,  9,  5,  1},
							 					 {14, 10,  6,  2},
												 {15, 11,  7,  3},
												 {16, 12,  8,  4}} );

	REQUIRE( rotate(Matrix{{ 1,  2,  3,  4,  5},
												 { 6,  7,  8,  9, 10},
												 {11, 12, 13, 14, 15},
												 {16, 17, 18, 19, 20},
												 {21, 22, 23, 24, 25}})
							 == Matrix{{21, 16, 11,  6,  1},
												 {22, 17, 12,  7,  2},
												 {23, 18, 13,  8,  3},
												 {24, 19, 14,  9,  4},
												 {25, 20, 15, 10,  5}} );
}

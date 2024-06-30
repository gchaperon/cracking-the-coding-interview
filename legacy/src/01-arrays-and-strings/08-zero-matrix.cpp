#include <unordered_set>
#include <vector>
#include <catch2/catch_test_macros.hpp>


using Matrix = std::vector<std::vector<int>>;


Matrix zero_matrix(Matrix matrix) {
	size_t n = matrix.size();
	size_t m = (n > 0) ? matrix[0].size() : 0;

	std::unordered_set<size_t> marked_rows;
	std::unordered_set<size_t> marked_columns;

	bool stop = false;
	for (size_t i = 0; i < n && !stop; i++) {
		for (size_t j = 0; j < m && !stop; j++) {
			if (matrix[i][j] == 0) {
				marked_rows.insert(i);
				marked_columns.insert(j);
				if (marked_rows.size() == n && marked_columns.size() == m) {
					stop = true;
				}
			}
		}
	}

	Matrix out(matrix);
	for (size_t i : marked_rows)
		for (size_t j = 0; j < m; j++)
			out[i][j] = 0;

	for (size_t j: marked_columns)
		for (size_t i = 0; i < n; i++)
			out[i][j] = 0;

	return out;
}


TEST_CASE( "Zeroes" ) {
	REQUIRE( zero_matrix(Matrix{}) == Matrix{} );
	REQUIRE( zero_matrix(Matrix{{1}}) == Matrix{{1}} );
	REQUIRE( zero_matrix(Matrix{{0, 1}}) == Matrix{{0, 0}} );
	REQUIRE( zero_matrix(Matrix{{1, 2, 3}}) == Matrix{{1, 2, 3}} );

	REQUIRE( zero_matrix(Matrix{{1, 2, 3, 4},
															{1, 0, 3, 4},
															{1, 2, 3, 4},
															{1, 2, 3, 4},
															{1, 2, 3, 4}})
										== Matrix{{1, 0, 3, 4},
	                       			{0, 0, 0, 0},
                        			{1, 0, 3, 4},
                        			{1, 0, 3, 4},
                        			{1, 0, 3, 4}} );

	REQUIRE( zero_matrix(Matrix{{0, 2, 3, 4},
															{1, 2, 3, 4},
															{1, 2, 3, 4},
															{1, 2, 3, 4},
															{1, 2, 3, 0}})
										== Matrix{{0, 0, 0, 0},
	                       			{0, 2, 3, 0},
                        			{0, 2, 3, 0},
                        			{0, 2, 3, 0},
                        			{0, 0, 0, 0}} );

	REQUIRE( zero_matrix(Matrix{{1, 2, 3, 4},
															{1, 0, 3, 4},
															{1, 2, 3, 4},
															{1, 2, 3, 0},
															{1, 2, 3, 4}})
										== Matrix{{1, 0, 3, 0},
	                      			{0, 0, 0, 0},
                        			{1, 0, 3, 0},
                        			{0, 0, 0, 0},
                        			{1, 0, 3, 0}} );

	REQUIRE( zero_matrix(Matrix{{0, 2, 3, 4},
															{0, 2, 3, 4},
															{0, 2, 3, 4},
															{0, 2, 3, 4},
															{0, 2, 3, 4}})
										== Matrix{{0, 0, 0, 0},
	                      			{0, 0, 0, 0},
                        			{0, 0, 0, 0},
                        			{0, 0, 0, 0},
                        			{0, 0, 0, 0}} );
}

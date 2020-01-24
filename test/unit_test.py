from board import solution

class Unit_Test():
    # run nose tests in parallel (multiprocessing module)
    _multiprocess_can_split_ = True

    def test_simple(self):
        board = [ [1,2,3],
                  [4,1,1],
                  [7,8,9] ]

        ans = solution(board)
        assert ans == 9874

    def test_path_of_9s(self):
        board = [ [1,1,1],
                  [9,1,1],
                  [9,9,9]]

        ans = solution(board)
        assert ans == 9999
    
    def test_board_of_9s(self):
        board = [ [9,9,9],
                  [9,9,9],
                  [9,9,9]]

        ans = solution(board)
        assert ans == 9999
    
    def test_board_of_1s(self):
        board = [ [1,1,1],
                  [1,1,1],
                  [1,1,1]]

        ans = solution(board)
        assert ans == 1111

    def test_single_row_board(self):
        board = [ [9,8,7,6,1,2,5,9,8] ]

        ans = solution(board)
        assert ans == 9876

    def test_multiple_paths_with_same_number(self):
        board = [[5,5,5,4],
                 [7,1,1,7],
                 [2,5,5,5]]

        ans = solution(board)
        assert ans == 7555

    def test_last_digit_differ(self):
        board = [[5,5,1,1],
                 [7,1,1,7],
                 [1,3,5,5]]

        ans = solution(board)
        assert ans == 7553
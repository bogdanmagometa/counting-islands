"""
main.py

Overall my algorithm has time complexity O(m*n) and space complexity O(m*n).
"""

from typing import List
from collections import deque


def main():
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]

    visited = [[False] * n for _ in range(m)]

    num_islands = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] and not visited[i][j]:
                visit_reachable(board, m, n, visited, i, j)
                num_islands += 1

    print(num_islands)


def visit_reachable(
        board: List[List[int]], m: int, n: int, visited: List[List[bool]], start_row: int,
        start_col: int):
    """Use BFS to visit all nodes in connected component
    Time complexity: O(number_of_nodes_in_connected_component)
    """
    frontier = deque()
    frontier.append((start_row, start_col))
    visited[start_row][start_col] = True
    while frontier:
        cur_row, cur_col = frontier.pop()
        for n_row, n_col in [(cur_row+1, cur_col), (cur_row-1, cur_col), (cur_row, cur_col+1), (cur_row, cur_col-1)]:
            if check_valid_position(n_row, n_col, m, n) and board[n_row][n_col] and not visited[n_row][n_col]:
                frontier.appendleft((n_row, n_col))
                visited[n_row][n_col] = True


def check_valid_position(row: int, col: int, m: int, n: int) -> bool:
    return 0 <= row < m and 0 <= col < n


if __name__ == "__main__":
    main()

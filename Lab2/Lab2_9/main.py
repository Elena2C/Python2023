def find_unsighted_spectators(matrix):
    unsighted_spectators = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            spectator_height = matrix[row][col]
            can_see_game = True

            r = row - 1
            while r >= 0:
                if matrix[r][col] >= spectator_height:
                    can_see_game = False
                    break
                r -= 1

            if not can_see_game:
                unsighted_spectators.append((row, col))

    return unsighted_spectators


# Example usage:
stadium_matrix = [[1, 2, 3, 2, 1, 1],
                  [2, 4, 4, 3, 7, 2],
                  [5, 5, 2, 5, 6, 4],
                  [6, 6, 7, 6, 7, 5],
                  [8, 3, 7, 7, 8, 5]]

unsighted_spectators = find_unsighted_spectators(stadium_matrix)
print("Unsighted Spectators:", unsighted_spectators)

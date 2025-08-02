#!/usr/bin/env python3
"""
Tic-Tac-Toe AI Game
An implementation of Tic-Tac-Toe with an unbeatable AI using Minimax algorithm with Alpha-Beta pruning.
"""

import math
from typing import List, Tuple, Optional, Union


class TicTacToe:
    """
    Tic-Tac-Toe game implementation with AI opponent using Minimax algorithm.
    """
    
    def __init__(self):
        # Initialize empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.human_player = 'X'
        self.ai_player = 'O'
        self.current_player = self.human_player  # Human goes first
    
    def display_board(self) -> None:
        """Display the current game board in a formatted way."""
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print("  -----------")
        print()
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if a move is valid (within bounds and cell is empty)."""
        return (0 <= row < 3 and 0 <= col < 3 and 
                self.board[row][col] == ' ')
    
    def make_move(self, row: int, col: int, player: str) -> bool:
        """Make a move on the board if valid."""
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def undo_move(self, row: int, col: int) -> None:
        """Undo a move (used in minimax algorithm)."""
        self.board[row][col] = ' '
    
    def get_available_moves(self) -> List[Tuple[int, int]]:
        """Get all available moves on the board."""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def check_winner(self) -> Optional[str]:
        """
        Check if there's a winner on the board.
        Returns 'X', 'O', or None if no winner.
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == 
                self.board[2][col] != ' '):
                return self.board[0][col]
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == 
            self.board[2][2] != ' '):
            return self.board[0][0]
        
        if (self.board[0][2] == self.board[1][1] == 
            self.board[2][0] != ' '):
            return self.board[0][2]
        
        return None
    
    def is_board_full(self) -> bool:
        """Check if the board is full (tie game)."""
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def is_game_over(self) -> bool:
        """Check if the game is over (winner or tie)."""
        return self.check_winner() is not None or self.is_board_full()
    
    def get_game_state(self) -> str:
        """Get the current game state as a string."""
        winner = self.check_winner()
        if winner:
            if winner == self.human_player:
                return "Human wins!"
            else:
                return "AI wins!"
        elif self.is_board_full():
            return "It's a tie!"
        else:
            return "Game in progress"
    
    def evaluate_board(self) -> int:
        """
        Evaluate the current board state for the AI player.
        Returns: +10 if AI wins, -10 if human wins, 0 for tie/ongoing.
        """
        winner = self.check_winner()
        if winner == self.ai_player:
            return 10
        elif winner == self.human_player:
            return -10
        else:
            return 0
    
    def minimax(self, depth: int, is_maximizing: bool, alpha: int = -math.inf, beta: int = math.inf) -> int:
        """
        Minimax algorithm with Alpha-Beta pruning.
        
        Args:
            depth: Current depth in the game tree
            is_maximizing: True if it's AI's turn (maximizing), False if human's turn (minimizing)
            alpha: Alpha value for pruning
            beta: Beta value for pruning
        
        Returns:
            The best score for the current position
        """
        # Base case: if game is over, return the evaluation
        if self.is_game_over():
            score = self.evaluate_board()
            # Adjust score by depth to prefer quicker wins and slower losses
            if score > 0:
                return score - depth
            elif score < 0:
                return score + depth
            else:
                return 0
        
        if is_maximizing:
            # AI's turn - maximize the score
            max_eval = -math.inf
            for row, col in self.get_available_moves():
                # Make the move
                self.make_move(row, col, self.ai_player)
                # Recursively evaluate
                eval_score = self.minimax(depth + 1, False, alpha, beta)
                # Undo the move
                self.undo_move(row, col)
                # Update max evaluation
                max_eval = max(max_eval, eval_score)
                # Alpha-Beta pruning
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            # Human's turn - minimize the score
            min_eval = math.inf
            for row, col in self.get_available_moves():
                # Make the move
                self.make_move(row, col, self.human_player)
                # Recursively evaluate
                eval_score = self.minimax(depth + 1, True, alpha, beta)
                # Undo the move
                self.undo_move(row, col)
                # Update min evaluation
                min_eval = min(min_eval, eval_score)
                # Alpha-Beta pruning
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval
    
    def get_best_move(self) -> Tuple[int, int]:
        """
        Get the best move for the AI using the Minimax algorithm.
        
        Returns:
            Tuple of (row, col) representing the best move
        """
        best_score = -math.inf
        best_move = None
        
        # Try all available moves
        for row, col in self.get_available_moves():
            # Make the move
            self.make_move(row, col, self.ai_player)
            # Evaluate using minimax
            score = self.minimax(0, False)
            # Undo the move
            self.undo_move(row, col)
            
            # Update best move if this is better
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move if best_move else (0, 0)  # Fallback (shouldn't happen)
    
    def get_human_move(self) -> Tuple[int, int]:
        """
        Get a valid move from the human player.
        
        Returns:
            Tuple of (row, col) representing the human's move
        """
        while True:
            try:
                print("Enter your move (row col), e.g., '1 2' for row 1, column 2:")
                move_input = input("Your move: ").strip()
                
                if move_input.lower() in ['quit', 'exit', 'q']:
                    print("Thanks for playing!")
                    exit(0)
                
                parts = move_input.split()
                if len(parts) != 2:
                    print("Please enter exactly two numbers separated by a space.")
                    continue
                
                row, col = int(parts[0]), int(parts[1])
                
                if not self.is_valid_move(row, col):
                    if not (0 <= row < 3 and 0 <= col < 3):
                        print("Invalid coordinates! Please enter numbers between 0 and 2.")
                    else:
                        print("That position is already taken! Choose an empty cell.")
                    continue
                
                return row, col
                
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space.")
            except KeyboardInterrupt:
                print("\nThanks for playing!")
                exit(0)
    
    def play_game(self) -> None:
        """Main game loop for human vs AI."""
        print("=" * 50)
        print("Welcome to Tic-Tac-Toe vs Unbeatable AI!")
        print("=" * 50)
        print("You are X, AI is O")
        print("Enter coordinates as 'row col' (0-2 for each)")
        print("Type 'quit' to exit the game")
        print("=" * 50)
        
        self.display_board()
        
        while not self.is_game_over():
            if self.current_player == self.human_player:
                # Human's turn
                print(f"\n{self.current_player}'s turn (Human)")
                row, col = self.get_human_move()
                self.make_move(row, col, self.current_player)
                print(f"You played at position ({row}, {col})")
                
            else:
                # AI's turn
                print(f"\n{self.current_player}'s turn (AI)")
                print("AI is thinking...")
                row, col = self.get_best_move()
                self.make_move(row, col, self.current_player)
                print(f"AI played at position ({row}, {col})")
            
            self.display_board()
            
            # Switch players
            self.current_player = (self.ai_player if self.current_player == self.human_player 
                                 else self.human_player)
        
        # Game over - display result
        print("=" * 30)
        print("GAME OVER!")
        print(f"Result: {self.get_game_state()}")
        print("=" * 30)


def main():
    """Main function to run the game."""
    while True:
        game = TicTacToe()
        game.play_game()
        
        # Ask if player wants to play again
        while True:
            try:
                play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes']:
                    print("\nStarting a new game...\n")
                    break
                elif play_again in ['n', 'no']:
                    print("Thanks for playing! Goodbye!")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                print("\nThanks for playing! Goodbye!")
                return


if __name__ == "__main__":
    main()
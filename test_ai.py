#!/usr/bin/env python3
"""
Test script to validate the Tic-Tac-Toe AI's unbeatable behavior.
This script runs automated tests to ensure the AI never loses.
"""

from tic_tac_toe import TicTacToe
import random
from typing import List, Tuple


class AITester:
    """Class to test the AI's performance and validate it's unbeatable."""
    
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def random_player_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Make a random move for testing purposes."""
        available_moves = game.get_available_moves()
        return random.choice(available_moves) if available_moves else (0, 0)
    
    def play_test_game(self, ai_goes_first: bool = False) -> str:
        """
        Play a single test game between AI and random player.
        
        Args:
            ai_goes_first: If True, AI goes first; otherwise human (random) goes first
            
        Returns:
            Result of the game: 'AI wins', 'Human wins', or 'Tie'
        """
        game = TicTacToe()
        
        # Set who goes first
        if ai_goes_first:
            game.current_player = game.ai_player
        else:
            game.current_player = game.human_player
        
        while not game.is_game_over():
            if game.current_player == game.ai_player:
                # AI's turn
                row, col = game.get_best_move()
                game.make_move(row, col, game.ai_player)
            else:
                # Random player's turn
                row, col = self.random_player_move(game)
                game.make_move(row, col, game.human_player)
            
            # Switch players
            game.current_player = (game.ai_player if game.current_player == game.human_player 
                                 else game.human_player)
        
        # Determine result
        winner = game.check_winner()
        if winner == game.ai_player:
            return "AI wins"
        elif winner == game.human_player:
            return "Human wins"
        else:
            return "Tie"
    
    def run_tests(self, num_games: int = 1000) -> None:
        """
        Run multiple test games to validate AI performance.
        
        Args:
            num_games: Number of games to test
        """
        print(f"Testing AI with {num_games} games...")
        print("=" * 50)
        
        # Reset counters
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
        # Test games where AI goes first
        print(f"Testing {num_games // 2} games where AI goes first...")
        for i in range(num_games // 2):
            result = self.play_test_game(ai_goes_first=True)
            if result == "AI wins":
                self.wins += 1
            elif result == "Human wins":
                self.losses += 1
            else:
                self.ties += 1
            
            if (i + 1) % 100 == 0:
                print(f"  Completed {i + 1} games...")
        
        # Test games where human goes first
        print(f"Testing {num_games // 2} games where human goes first...")
        for i in range(num_games // 2):
            result = self.play_test_game(ai_goes_first=False)
            if result == "AI wins":
                self.wins += 1
            elif result == "Human wins":
                self.losses += 1
            else:
                self.ties += 1
            
            if (i + 1) % 100 == 0:
                print(f"  Completed {i + 1} games...")
        
        # Display results
        print("\n" + "=" * 50)
        print("TEST RESULTS:")
        print("=" * 50)
        print(f"Total games played: {num_games}")
        print(f"AI wins: {self.wins} ({self.wins/num_games*100:.1f}%)")
        print(f"AI losses: {self.losses} ({self.losses/num_games*100:.1f}%)")
        print(f"Ties: {self.ties} ({self.ties/num_games*100:.1f}%)")
        print("=" * 50)
        
        # Validation
        if self.losses == 0:
            print("✅ SUCCESS: AI is unbeatable! (Never lost a game)")
        else:
            print(f"❌ FAILURE: AI lost {self.losses} games! AI should be unbeatable.")
        
        if self.wins + self.ties == num_games:
            print("✅ SUCCESS: AI either won or tied every game")
        else:
            print("❌ FAILURE: Unexpected game outcomes detected")
    
    def test_specific_scenarios(self) -> None:
        """Test specific game scenarios to ensure AI behaves correctly."""
        print("\nTesting specific scenarios...")
        print("=" * 30)
        
        # Test 1: AI should win when it can
        print("Test 1: AI should take winning move when available")
        game = TicTacToe()
        # Set up a winning scenario for AI
        game.board = [['O', 'O', ' '],
                     ['X', 'X', ' '],
                     [' ', ' ', ' ']]
        
        best_move = game.get_best_move()
        if best_move == (0, 2):  # AI should complete its winning row
            print("✅ PASSED: AI correctly identified winning move")
        else:
            print(f"❌ FAILED: AI chose {best_move} instead of (0, 2)")
        
        # Test 2: AI should block human from winning
        print("\nTest 2: AI should block human winning move")
        game = TicTacToe()
        game.board = [['X', 'X', ' '],
                     ['O', ' ', ' '],
                     [' ', ' ', ' ']]
        
        best_move = game.get_best_move()
        if best_move == (0, 2):  # AI should block human's winning move
            print("✅ PASSED: AI correctly blocked human winning move")
        else:
            print(f"❌ FAILED: AI chose {best_move} instead of blocking at (0, 2)")
        
        # Test 3: AI should prefer center when available
        print("\nTest 3: AI should prefer strategic positions")
        game = TicTacToe()
        game.board = [['X', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]
        
        best_move = game.get_best_move()
        # AI should prefer center (1,1) or corner positions
        strategic_moves = [(1, 1), (0, 2), (2, 0), (2, 2)]
        if best_move in strategic_moves:
            print(f"✅ PASSED: AI chose strategic position {best_move}")
        else:
            print(f"❌ WARNING: AI chose {best_move}, might not be optimal")


def main():
    """Main function to run AI tests."""
    print("Tic-Tac-Toe AI Testing Suite")
    print("=" * 50)
    
    tester = AITester()
    
    # Run specific scenario tests
    tester.test_specific_scenarios()
    
    # Run performance tests
    print("\n" + "=" * 50)
    tester.run_tests(num_games=1000)
    
    print("\nTesting complete!")


if __name__ == "__main__":
    main()
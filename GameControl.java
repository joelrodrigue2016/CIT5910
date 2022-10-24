package simple21;

import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

/**
 * This is a simplified version of a common card game, "21". 
 */
public class GameControl {
    
	/**
	 * Human player.
	 */
    HumanPlayer human;
    
    /**
     * Computer player. David
     */
    ComputerPlayer player1;
    
    /**
     * Computer player. Moises
     */
    ComputerPlayer player2;
    
    /**
     * Computer player. Jeniffer
     */
    ComputerPlayer player3;
    
    /** 
     * A random number generator to be used for returning random "cards" in a card deck.
     * */
    Random random = new Random();
      
    /**
     * The main method just creates a GameControl object and calls its run method.
     * @param args Not used.
     */
    public static void main(String args[]) {    

		new GameControl().run();
    }
    
    /**
     * Prints a welcome method, then calls methods to perform each of the following actions:
     * - Create the players (one of them a Human)
     * - Deal the initial two cards to each player
     * - Control the play of the game
     * - Print the final results
     */
    public void run() {
    	
        Scanner scanner = new Scanner(System.in);
        
        // Run the main function.
		System.out.println("Welcome to Simple 21!\n" + 
				"You'll play against 3 other players (computers).\n" + 
				"Try to get as close to 21 as possible, without going over.\n" + 
				"What is your name?");
		String humansName = scanner.next();
		createPlayers(humansName);	
		deal();			
		controlPlay(scanner);	
		scanner.close();	
		printResults();
        
    }
    
    /**
     * Creates one human player with the given humansName, and three computer players with hard-coded names.
     * @param humansName for human player
     */
    public void createPlayers(String humansName) {
       // Give name for each player.
    	
    	human = new HumanPlayer(humansName);
    	player1 = new ComputerPlayer("David");
    	player2 = new ComputerPlayer("Moises");
    	player3 = new ComputerPlayer("Jeniffer");
    }
    
    /**
     * Deals two "cards" to each player, one hidden, so that only the player who gets it knows what it is, 
     * and one face up, so that everyone can see it. (Actually, what the other players see is the total 
     * of each other player's cards, not the individual cards.)
     */
    public void deal() { 
        // Print the initial two cards for everyone.
    	System.out.println();
    	System.out.println(human.name + ":");
    	this.human.takeHiddenCard(nextCard());
    	this.human.takeVisibleCard(nextCard());
    	
    	System.out.println();
    	System.out.println(player1.name + ":");
    	this.player1.takeHiddenCard(nextCard());
    	this.player1.takeVisibleCard(nextCard());
    	
    	System.out.println();
    	System.out.println(player2.name + ":");
    	this.player2.takeHiddenCard(nextCard());
    	this.player2.takeVisibleCard(nextCard());
    	
    	System.out.println();
    	System.out.println(player3.name + ":");
    	this.player3.takeHiddenCard(nextCard());
    	this.player3.takeVisibleCard(nextCard());
    	  	
    }
    
    /**
     * Returns a random "card", represented by an integer between 1 and 10, inclusive. 
     * The odds of returning a 10 are four times as likely as any other value (because in an actual
     * deck of cards, 10, Jack, Queen, and King all count as 10).
     * 
     * Note: The java.util package contains a Random class, which is perfect for generating random numbers.
     * @return a random integer in the range 1 - 10.
     */
    public int nextCard() { 
    	// Generate random number from 1-13. If the number =11 or 12 or 13, convert it to 10.
    	
    	int card = random.nextInt(13) + 1;
    	if (card == 11 || card == 12 || card == 13) {
    		card = 10;
    	}   	
    	return card;
    }

    /**
     * Gives each player in turn a chance to take a card, until all players have passed. Prints a message when 
     * a player passes. Once a player has passed, that player is not given another chance to take a card.
     * @param scanner to use for user input
     */
    public void controlPlay(Scanner scanner) { 
        // While not everyone has passed, give each player in turn a chance to take a card or pass.
		
    	while (checkAllPlayersHavePassed() == false) {
    		if (human.passed == false) {
    			boolean humanResponse = human.offerCard(human, player1, player2, player3, scanner);
        		if (humanResponse==true) {
        			System.out.println();
        			System.out.println(human.name + ":");
        			int card0 = nextCard();
            		human.takeVisibleCard(card0);
        		} else {
        			human.passed =true;
        			System.out.println();
        			System.out.println(human.name + " passes.");
        		}	
        	} 
        	
        	if (player1.passed == false) {
        		boolean Player1Response = player1.offerCard(human, player1, player2, player3);
        		if (Player1Response==true) {
        			System.out.println();
            		System.out.println(player1.name + ":");
            		int card1 = nextCard();
            		player1.takeVisibleCard(card1);
        		} else {
        			player1.passed=true;
        			System.out.println();
        			System.out.println(player1.name + " passes.");
        		}
        	} 
        	
        	if (player2.passed == false) {
        		boolean Player2Response = player2.offerCard(human, player1, player2, player3);
        		if (Player2Response==true) {
        			System.out.println();
            		System.out.println(player2.name + ":");
            		int card2 = nextCard();
            		player2.takeVisibleCard(card2);
        		} else {
        			player2.passed=true;
        			System.out.println();
        			System.out.println(player2.name + " passes.");
        		}
        	} 
        	
        	if (player3.passed == false) {
        		boolean Player3Response = player3.offerCard(human, player1, player2, player3);
        		if (Player3Response==true) {
        			System.out.println();
            		System.out.println(player3.name + ":");
            		int card3 = nextCard();
            		player3.takeVisibleCard(card3);
        		} else {
        			player3.passed=true;
        			System.out.println();
        			System.out.println(player3.name + " passes.");
        		}
        	}    	
    	}
    }
     
    /**
     * Checks if all players have passed.
     * @return true if all players have passed
     */
    public boolean checkAllPlayersHavePassed() {
    	// If all players have passed, return true. Else, return false.
    	
    	if (human.passed == true && player1.passed == true && player2.passed == true && player3.passed ==true) {
    		return true;
    	} else {
    		return false;
    	}	  	
    }
    
    /**
     * Prints a summary at the end of the game.
     * Displays how many points each player had, and if applicable, who won.
     */
    public void printResults() { 
        // Print the final score of everyone and the winner information.
    	
    	System.out.println();
    	System.out.println("Game over.");
		System.out.println(human.name + " has " + human.getScore() + " total point(s).");
		System.out.println(player1.name + " has " + player1.getScore() + " total point(s).");
		System.out.println(player2.name + " has " + player2.getScore() + " total point(s).");
		System.out.println(player3.name + " has " + player3.getScore() + " total point(s).");
		printWinner();	
    }

    /**
     * Determines who won the game, and prints the results.
     */
    public void printWinner() { 
        // Sort the scores and decide who the winner is or if there is a tie.
    	
    	int[] nums={human.getScore(), player1.getScore(), player2.getScore(), player3.getScore()};
    	Arrays.sort(nums);
    	int max1 = nums[3];
    	int max2 = nums[2];
    	int max3 = nums[1];
    	int max4 = nums[0];
    	if (max4>21) {
    		System.out.println("Nobody wins.");
    	}
    	else if (max3>21 && max4<=21) {
    		if (max4 == human.getScore()) {
    			System.out.println(human.name + " wins with " + max4 + " point(s).");
    		}
    		if (max4 == player1.getScore()) {
    			System.out.println(player1.name + " wins with " + max4 + " point(s).");
    		}
    		if (max4 == player2.getScore()) {
    			System.out.println(player2.name + " wins with " + max4 + " point(s).");
    		}
    		if (max4 == player3.getScore()) {
    			System.out.println(player3.name + " wins with " + max4 + " point(s).");
    		}				
		}
    	else if (max3<=21 && max2>21) {
    		if (max3 == max4) {
    			System.out.println("Tie. Nobody wins.");
    		}
    		else {
    			if (max3 == human.getScore()) {
        			System.out.println(human.name + " wins with " + max3 + " point(s).");
        		}
        		if (max3 == player1.getScore()) {
        			System.out.println(player1.name + " wins with " + max3 + " point(s).");
        		}
        		if (max3 == player2.getScore()) {
        			System.out.println(player2.name + " wins with " + max3 + " point(s).");
        		}
        		if (max3 == player3.getScore()) {
        			System.out.println(player3.name + " wins with " + max3 + " point(s).");
        		}
    		}
    	}
    	else if (max2<=21 && max1>21) {
    		if (max2 == max3) {
    			System.out.println("Tie. Nobody wins.");
    		}
    		else {
    			if (max2 == human.getScore()) {
        			System.out.println(human.name + " wins with " + max2 + " point(s).");
        		}
        		if (max2 == player1.getScore()) {
        			System.out.println(player1.name + " wins with " + max2 + " point(s).");
        		}
        		if (max2 == player2.getScore()) {
        			System.out.println(player2.name + " wins with " + max2 + " point(s).");
        		}
        		if (max2 == player3.getScore()) {
        			System.out.println(player3.name + " wins with " + max2 + " point(s).");
        		}
    		}   		
    	}
    	else {
    		if (max1 == max2) {
    			System.out.println("Tie. Nobody wins.");
    		}
    		else {
    			if (max1 == human.getScore()) {
        			System.out.println(human.name + " wins with " + max1 + " point(s).");
        		}
        		if (max1 == player1.getScore()) {
        			System.out.println(player1.name + " wins with " + max1 + " point(s).");
        		}
        		if (max1 == player2.getScore()) {
        			System.out.println(player2.name + " wins with " + max1 + " point(s).");
        		}
        		if (max1 == player3.getScore()) {
        			System.out.println(player3.name + " wins with " + max1 + " point(s).");
        		}
    		} 
    	}  	
    }
}

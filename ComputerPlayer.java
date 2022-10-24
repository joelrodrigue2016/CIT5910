package simple21;

/**
 * Represents a computer player in this simplified version of the "21" card game.
 */
public class ComputerPlayer {

	/** 
	 * The name of the player.
	 */
    String name;
    
    /**
     * The player's one hidden card (a value from 1 - 10).
     */
    private int hiddenCard = 0;
    
    /** 
     * The sum of the player's cards, not counting the hidden card. 
     */
    private int sumOfVisibleCards = 0;
    
    /**
     * Flag indicating if the player has passed (asked for no more cards).
     */
    boolean passed = false;
    
    /**
     * Constructs a computer player with the given name.
     * @param name of the user.
     */
    public ComputerPlayer (String name) {
        this.name = name;
    }
    
    /**
     * Decides whether to take another card. In order to make this decision, this player considers 
     * their own total points (sum of visible cards + hidden card). 
     * This player may also consider other players' sum of visible cards, but not the value 
     * of other players' hidden cards.
     * @param human The other human player
     * @param player1 Another (computer) player
     * @param player2 Another (computer) player
     * @param player3 Another (computer) player
     * @return true if this player wants another card
     */
    public boolean offerCard(HumanPlayer human, ComputerPlayer player1, ComputerPlayer player2, ComputerPlayer player3) { 
    	// Give the computer players strategy to decide whether to pass or not.
    	
    	int visibleHuman = human.getSumOfVisibleCards();
    	int visiblePlayer1 = player1.sumOfVisibleCards;
    	int totalPlayer1 = player1.getScore();
    	int visiblePlayer2 = player2.sumOfVisibleCards;
    	int totalPlayer2 = player2.getScore();
    	int visiblePlayer3 = player3.sumOfVisibleCards;
    	int totalPlayer3 = player3.getScore();
    	
    	// Strategy for player1
    	if (this.name == player1.name) {
    		if (totalPlayer1<15) {
    			return true; // If the total score is lower than 15, take another card.
    		}
    		else if (visiblePlayer2 >= totalPlayer1 && visiblePlayer2 < 21) {
    			return true; // If the total score is not lower than 15 and player2 has higher score without reaching 21, take another card.
    		}
    		else if (visiblePlayer3 >= totalPlayer1 && visiblePlayer3 < 21) {
    			return true; // If the total score is not lower than 15 and player3 has higher score without reaching 21, take another card.
    		}
    		else if (visibleHuman >= totalPlayer1 && visibleHuman < 21) {
    			return true; // If the total score is not lower than 15 and human has higher score without reaching 21, take another card.
    		} else {
    			this.passed = true;
    			return false; //If the total score >=21, then pass.
    		}
    	}
    	
    	// Strategy for player2
    	if (this.name ==player2.name) {
    		if (totalPlayer2<15) {
    			return true; // If the total score is lower than 15, take another card.
    		}
    		else if (visiblePlayer3 >= totalPlayer2 && visiblePlayer3 < 21) {
    			return true; // If the total score is not lower than 15 and player3 has higher score without reaching 21, take another card.
    		}
    		else if (visiblePlayer1 >= totalPlayer2 && visiblePlayer1 < 21) {
    			return true; // If the total score is not lower than 15 and player1 has higher score without reaching 21, take another card.
    		}
    		else if (visibleHuman >= totalPlayer2 && visibleHuman < 21) {
    			return true; // If the total score is not lower than 15 and human has higher score without reaching 21, take another card.
    		} else {
    			this.passed = true;
    			return false; //If the total score >=21, then pass.
    		}
    		
    	}
    	
    	// Strategy for player3
    	if (this.name ==player3.name) {
    		if (totalPlayer3<15) {
    			return true; // If the total score is lower than 15, take another card.
    		}
    		else if (visiblePlayer1 >= totalPlayer3 && visiblePlayer1 < 21) {
    			return true; // If the total score is not lower than 15 and player1 has higher score without reaching 21, take another card.
    		}
    		else if (visiblePlayer2 >= totalPlayer3 && visiblePlayer2 < 21) {
    			return true; // If the total score is not lower than 15 and player2 has higher score without reaching 21, take another card.
    		}
    		else if (visibleHuman >= totalPlayer3 && visibleHuman < 21) {
    			return true; // If the total score is not lower than 15 and human has higher score without reaching 21, take another card.
    		} else {
    			this.passed = true;
    			return false; //If the total score >=21, then pass.
    		}    		
    	}    	
    	return false;  	
    }
    
    /**    
     * Puts the specified card in this player's hand as the hidden card.
     * Prints a message saying that the card is being taken, but does not print the value of the hidden card.
     * @param card being taken
     */
    public void takeHiddenCard(int card) {
    	// Tell a hidden card is being taken and record the card.
    	
    	this.hiddenCard += card;
    	System.out.println("A hidden card is being taken.");
    }
    
    /**
     * Adds the given card to the sum of the visible cards for this player.
     * Prints a message saying that the card is being taken.
     * @param card being taken
     */
    public void takeVisibleCard(int card) { 
    	// Tell what the visible card is and add it to the total score of visible cards.
    	
    	this.sumOfVisibleCards += card;
    	System.out.println(card + " is being taken.");
    }

    /**
     * Returns the total sum of this player's cards, not counting the hidden card. 
     * @return sumOfVisibleCards
     */
    public int getSumOfVisibleCards() { 
    	// Return the sum of the computer player's visible cards.
    	
    	return this.sumOfVisibleCards;
    	
    }
    
    /**
     * Return this player's total score (the total of all this player's cards).
     * That is to say, the sum of the visible cards + the hidden card.
     * @return total score 
     */
    public int getScore() { 
    	// Return the total sum of the computer player's cards.
    	
    	return this.sumOfVisibleCards + this.hiddenCard;
    }
}

import java.util.*;

public class tictactoe 
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int [] board = new int[9];
		tictactoe ob = new tictactoe();
		System.out.println("Enter the matrix:");
		for (int i = 0;i<9 ; i++)
		{	
			switch(sc.next().charAt(0))
			{
				case 'o':
				board[i] = 2;
				break;
				case 'x':
				board[i] = 1;
				break;
				case '_': //blank space condition
				board[i] = 0;
				break;
				default:
				System.out.println("Please enter a correct input!");
				board[i]=0;
			}
		}
		ob.printBoard(board);
		ob.getIndex(board);
	}

	void getIndex(int[]board)
	{
		int [] power = {6561,2187,729,243,81,27,9,3,0};
		int k=0;
		int index=0;
		for(int i:board)
		{
			index += i*power[k];
			k++;
		}
		System.out.println("\nIndex= "+index);

	}

	void printBoard(int[]board)
	{
		System.out.println("\nTicTacToe Board:");
		System.out.println(board[0]+"|"+board[1]+"|"+board[2]+"\n"+
						   board[3]+"|"+board[4]+"|"+board[5]+"\n"+
						   board[6]+"|"+board[7]+"|"+board[8]);
	}
}
public class tictactoeAIMain {
	public static void main(String[] args) {
		// { "X", "O", "0", "O", "0", "0", "O", "0", "X" };
		// Scanner sc = new Scanner(System.in);
		// String boardmatrix[] = new String[9];
		// System.out.println("Enter the matrix position:");
		// for (int i = 0; i < boardmatrix.length; i++) {
		// 	boardmatrix[i] = sc.next();
		// }
		String boardmatrix[] = { "x", "_", "o", "o", "_", "_", "o", "_", "x" };
		// x _ o
		// o _ _
		// o _ x
		int avlmove[][] = new int[9][9];
		int emptypos = 0;
		for (int i = 0; i < 9; i++) 
		{
			if (boardmatrix[i].equals("_") ) 
				emptypos += 1;	
		}

		int[] s = new int[emptypos];
		System.out.println("*******************************\nNo of Empty places on the board : " + emptypos+"\n");
		for (int x = 0; x < emptypos; x++) 
		{
			for (int y = 0; y < 9; y++) 
			{
				if (boardmatrix[y] == "x") 
					avlmove[x][y] = 1;
				 else if (boardmatrix[y] == "o") 
						avlmove[x][y] = 2;
				 else if (boardmatrix[y] == "_") 
						avlmove[x][y] = 0;
			}
		}

		int nextEmptyPos = 0;
		for (int x = 0; x < emptypos; x++) 
		{
			for (int y = nextEmptyPos; y < 9; y++) 
			{	
				if (avlmove[x][y] == 0) {
					avlmove[x][y] = 1;
					int elsescore = 0;
					
					if (y == 0 || y == 2 || y == 6 || y == 8) {
						elsescore += 3;
					} else if (y == 1 || y == 3 || y == 5 || y == 7) {
						elsescore += 2;
					} else if (y == 4) {
						elsescore += 4;
					}
					nextEmptyPos = y;
					nextEmptyPos++;
					s[x] = elsescore;
					break;
				}
			}
		}
		System.out.println("*******************************");
		System.out.println("Move Generator Matrix:");
		for (int i = 0; i < emptypos; i++) {
			System.out.print("Move "+(i+1)+": ");
			for (int j = 0; j < 9; j++) {
				System.out.print(avlmove[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println("*******************************");
		int count1 = 0;
		int count2 = 1;
		int count3 = 2;
		
		for (int i = 0; i < emptypos; i++) {
			int score = 0;
			for (int j = 0; j < 8; j++) {
				String line = null;
				line = Integer.toString(
						avlmove[i][count1]) + Integer.toString(avlmove[i][count2]) + Integer.toString(
								avlmove[i][count3]);
				while(true)
				{
					if(j==0)
					{
						line = Integer.toString(
								avlmove[i][0]) + Integer.toString(avlmove[i][1])
								+ Integer.toString(avlmove[i][2]);
						break;
					}
					else if(j==1)
					{
						line = Integer.toString(
								avlmove[i][3]) + Integer.toString(avlmove[i][4])
								+ Integer.toString(avlmove[i][5]);
						break;
					}
					else if(j==2)
					{
						line = Integer.toString(
								avlmove[i][6]) + Integer.toString(avlmove[i][7])
								+ Integer.toString(avlmove[i][8]);
						break;
					}
					else if(j==3)
					{
						line = Integer.toString(
								avlmove[i][0]) + Integer.toString(avlmove[i][3])
								+ Integer.toString(avlmove[i][6]);
						break;
					}
					else if(j==4)
					{
						line = Integer.toString(
								avlmove[i][1]) + Integer.toString(avlmove[i][4])
								+ Integer.toString(avlmove[i][7]);
						break;
					}
					else if(j==5)
					{
						line = Integer.toString(
								avlmove[i][2]) + Integer.toString(avlmove[i][4])
								+ Integer.toString(avlmove[i][5]);
						break;
					}
					else if(j==6)
					{
						line = Integer.toString(
								avlmove[i][0]) + Integer.toString(avlmove[i][4])
								+ Integer.toString(avlmove[i][8]);
						break;
					}
					else if (j == 7) 
					{
						line = Integer.toString(
								avlmove[i][2]) + Integer.toString(avlmove[i][4])
								+ Integer.toString(avlmove[i][6]);
						break;
					}
				}
					
				if (line.equals("111")) {
					score += 60;
					s[i] = score;
					// System.out.println("\nBest Score of X at move" + (i+1)+" empty cell is
					// "+score);
				} else if (line.equals("222")) {
					score += 40;
					s[i] = score;
					// System.out.println("\nScore of X at "+(i+1)+" empty cell : " + score);
				}
			}
		}
			int temp=0,max=0;
        for(int j=0;j<emptypos;j++){
            System.out.println("Move "+(j+1)+" score is "+s[j]);
            if(max<=s[j]){
                max=s[j];
               temp=j+1; 
            }
		}
		System.out.println("************************");
        System.out.println("Move "+(temp)+ " is the Best Move");
		}

	}


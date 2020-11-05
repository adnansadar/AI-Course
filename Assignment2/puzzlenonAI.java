/**
 * PuzzleProblem
 */
public class puzzlenonAI {
    public static void main(String[] args) {
        int[] initialstate = { 2, 8, 3, 1, 6, 4, 7, 0, 5 };
        // 2 8 3
        // 1 6 4
        // 7 0 5
        int[] goalstate = { 1, 2, 3, 8, 0, 4, 7, 6, 5 };
        // 1 2 3
        // 8 0 4
        // 7 6 5
        System.out.println("\nInitial State is:");
        for (int i :initialstate) {
            System.out.print(i + " ");
        }
        System.out.println("\nGoal State is");
        for (int i : goalstate) {
            System.out.print(i + " ");
        }
        heuristicFunction1(initialstate, goalstate);
        heuristicFunction2(initialstate, goalstate);
        heuristicFunction3(initialstate, goalstate);
        heuristicFunction4(initialstate, goalstate);
    }

    private static int checkMoves(int[] initialstate) {
        int moves = 0;
        for (int i = 0; i < initialstate.length; i++) {
            if (initialstate[i] == 0) {
                if (i == 0 || i == 2 || i == 6 || i == 8) //edge case
                    moves = 2;
                else if (i == 1 || i == 3 || i == 5 || i == 7) //middle elements
                    moves = 3;
                else
                    moves = 4; //center case
            }
        }
        return moves;
    }

    private static int[][] moveGenerator(int[] initialstate, int moves) {
        int[][] movestate = new int[4][9];
        for (int i = 0; i < moves; i++) { //filling movestate with initial state values
            for (int j = 0; j < 9; j++) {
                movestate[i][j] = initialstate[j];
            }
        }
        int up = 0, down = 0, left = 0, right = 0;
        for (int i = 0; i < moves; i++) {
            for (int j = 0; j < 9; j++) {
                if (movestate[i][j] == 0) {
                    if (j >= 3 && up == 0) { //up move check
                        movestate[i][j] = initialstate[j - 3];
                        movestate[i][j - 3] = initialstate[j];
                        up++;
                    } else if (j <= 5 && down == 0) { //down move check
                        movestate[i][j] = initialstate[j + 3];
                        movestate[i][j + 3] = initialstate[j];
                        down++;
                    } else if (((j == 2 || (j - 2) % 3 == 0) || ((j - 1) % 3 == 0 || j == 1)) && left == 0) { //left move check
                        movestate[i][j] = initialstate[j - 1];
                        movestate[i][j - 1] = initialstate[j];
                        left++;
                    } else if (((j == 0 || j % 3 == 0) || ((j - 1) % 3 == 0 || j == 1)) && right == 0) { //right move check
                        movestate[i][j] = initialstate[j + 1];
                        movestate[i][j + 1] = initialstate[j];
                        right++;
                    }
                }
            }
        }
        return movestate;
    }

    // no of misplaced tiles wrt goal state
    private static void heuristicFunction1(int[] initialstate, int[] goalstate) {
        int moves = checkMoves(initialstate);
        System.out.println("\nMoves available for the initial state are: " + moves);
        int movestate[][] = moveGenerator(initialstate, moves);
        int heuristicvalues1[] = new int[moves];
        for (int i = 0; i < moves; i++) { //counting no of misplaced tiles for each move
            int count = 0;
            System.out.println("Move " + (i + 1));
            for (int j = 0; j < 9; j++) {
                if (goalstate[j] != movestate[i][j]) //check if tile matching or not
                    count++;
                System.out.print(movestate[i][j] + " ");
            }
            System.out.println();
            heuristicvalues1[i] = count; //storing the count
        }
        System.out.println("\nHeuristic Function 1(no of misplaced tiles) values are:");
        for (int i = 0; i < heuristicvalues1.length; i++) {
            System.out.println("Move "+(i+1) + ": "+heuristicvalues1[i]);
        }
        int minindex = 0;
        for (int i = 1; i < heuristicvalues1.length; i++) { //finding the best move
            if(heuristicvalues1[i]<heuristicvalues1[minindex])
            minindex = i;
        }
        System.out.println();
        System.out.println("Move "+(minindex+1)+" is the best move");
        System.out.println("\n********************************************");

    }

    // Manhattan Distance
    private static void heuristicFunction2(int[] initialstate, int[] goalstate) {
        int moves = checkMoves(initialstate);
        System.out.println("\nMoves available for the initial state are: " + moves);
        int movestate[][] = moveGenerator(initialstate, moves);
         int heuristicvalues2[] = new int[moves];

        for (int i = 0; i < moves; i++) {
            int count = 0;
            System.out.println("Move " + (i + 1));
            for (int j = 0; j < 9; j++) {
                System.out.print(movestate[i][j]+" ");
                count+= Math.abs(goalstate[j]-movestate[i][j]); //absolute difference in values
            }
            System.out.println();
            heuristicvalues2[i] = count;
        }
        System.out.println("\nHeuristic Function 2 (Manhattan Distance)values are:");
        for (int i = 0; i < heuristicvalues2.length; i++) {
            System.out.println("Move " + (i + 1) + ": " + heuristicvalues2[i]);
        }
        int minindex = 0;
        for (int i = 1; i < heuristicvalues2.length; i++) {
            if (heuristicvalues2[i] < heuristicvalues2[minindex])
                minindex = i;
        }
        System.out.println();
        System.out.println("Move " + (minindex + 1) + " is the best move");
        System.out.println("\n********************************************");
    }

    // Euclidean Distance
    private static void heuristicFunction3(int[] initialstate, int[] goalstate) {
        int moves = checkMoves(initialstate);
        System.out.println("\nMoves available for the initial state are: " + moves);
        int movestate[][] = moveGenerator(initialstate, moves);
        double heuristicvalues3[] = new double[moves];

        for (int i = 0; i < moves; i++) {
            double ans = 0;
            double sum = 0;
            int x = 0;
            System.out.println("Move " + (i + 1));
            for (int j = 0; j < 9; j++) {
                System.out.print(movestate[i][j] + " ");
               x = goalstate[j] - movestate[i][j];
               sum += Math.pow(x, 2);
            }
            ans = Math.sqrt(sum);
            heuristicvalues3[i] = ans;
            System.out.println();
            
        }
        System.out.println("\nHeuristic Function 3(Euclidean Distance) values are:");
        for (int i = 0; i < heuristicvalues3.length; i++) {
            System.out.println("Move " + (i + 1) + ": " + heuristicvalues3[i]);
        }
        int minindex = 0;
        for (int i = 1; i < heuristicvalues3.length; i++) {
            if (heuristicvalues3[i] < heuristicvalues3[minindex])
                minindex = i;
        }
        System.out.println();
        System.out.println("Move " + (minindex + 1) + " is the best move");
        System.out.println("\n********************************************");
    }

    // Jaccard Distance
    private static void heuristicFunction4(int[] initialstate, int[] goalstate) {
        int moves = checkMoves(initialstate);
        System.out.println("\nMoves available for the initial state are: " + moves);
        int movestate[][] = moveGenerator(initialstate, moves);
        double heuristicvalues4[] = new double[moves];

        for (int i = 0; i < moves; i++) {
            double count = 0;
            System.out.println("Move "+(i+1));
            for (int j = 0; j < 9; j++) {
                System.out.print(movestate[i][j] + " ");
                if(movestate[i][j] != goalstate[j]) //similar to no of misplaced tiles
                    count+=1;
            }
            double newcount = count;
            heuristicvalues4[i] = newcount/9; //jaccard value
            System.out.println();
        }
        System.out.println("\nHeuristic Function 4(Jaccard Distance) values are:");
        for (int i = 0; i < heuristicvalues4.length; i++) {
            System.out.println("Move " + (i + 1) + ": " + heuristicvalues4[i]);
        }
        int minindex = 0;
        for (int i = 1; i < heuristicvalues4.length; i++) {
            if (heuristicvalues4[i] < heuristicvalues4[minindex])
                minindex = i;
        }
        System.out.println();
        System.out.println("Move " + (minindex + 1) + " is the best move");
        System.out.println("\n********************************************");
    }
}

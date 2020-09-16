/**
 * PuzzleProblem
 */
public class PuzzleProblem {
    public static void main(String[] args) {
        int[] initialstate = { 2, 8, 3, 1, 6, 4, 7, 0, 5 };
        int[] goalstate = { 1, 2, 3, 8, 0, 4, 7, 6, 5 };
        System.out.println("\nInitial State is:");
        for (int i = 0; i < initialstate.length; i++) {
            System.out.print(initialstate[i] + " ");
        }
        System.out.println("\nGoal State is");
        for (int i = 0; i < initialstate.length; i++) {
            System.out.print(goalstate[i] + " ");
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
                if (i == 0 || i == 2 || i == 6 || i == 8)
                    moves = 2;
                else if (i == 1 || i == 3 || i == 5 || i == 7)
                    moves = 3;
                else
                    moves = 4;
            }
        }
        return moves;
    }

    private static int[][] moveGenerator(int[] initialstate, int moves) {
        int[][] movestate = new int[4][9];
        for (int i = 0; i < moves; i++) {
            for (int j = 0; j < 9; j++) {
                movestate[i][j] = initialstate[j];
            }
        }
        int up = 0, down = 0, left = 0, right = 0;
        for (int i = 0; i < moves; i++) {
            for (int j = 0; j < 9; j++) {
                if (movestate[i][j] == 0) {
                    if (j >= 3 && up == 0) {
                        movestate[i][j] = initialstate[j - 3];
                        movestate[i][j - 3] = initialstate[j];
                        up++;
                    } else if (j <= 5 && down == 0) {
                        movestate[i][j] = initialstate[j + 3];
                        movestate[i][j + 3] = initialstate[j];
                        down++;
                    } else if (((j == 2 || (j - 2) % 3 == 0) || ((j - 1) % 3 == 0 || j == 1)) && left == 0) {
                        movestate[i][j] = initialstate[j - 1];
                        movestate[i][j - 1] = initialstate[j];
                        left++;
                    } else if (((j == 0 || j % 3 == 0) || ((j - 1) % 3 == 0 || j == 1)) && right == 0) {
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
        for (int i = 0; i < moves; i++) {
            int count = 0;
            System.out.println("Move " + (i + 1));
            for (int j = 0; j < 9; j++) {
                if (goalstate[j] != movestate[i][j])
                    count++;
                System.out.print(movestate[i][j] + " ");
            }
            System.out.println();
            heuristicvalues1[i] = count;
        }
        System.out.println("\nHeuristic Function 1(no of misplaced tiles) values are:");
        for (int i = 0; i < heuristicvalues1.length; i++) {
            System.out.print(heuristicvalues1[i] + " ");
        }
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
                count+= Math.abs(goalstate[j]-movestate[i][j]);
            }
            System.out.println();
            heuristicvalues2[i] = count;
        }
        System.out.println("\nHeuristic Function 2 (Manhattan Distance)values are:");
        for (int i = 0; i < heuristicvalues2.length; i++) {
            System.out.print(heuristicvalues2[i] + " ");
        }
        System.out.println("\n********************************************");
    }

    // Euclidean Distance
    private static void heuristicFunction3(int[] initialstate, int[] goalstate) {
        int moves = checkMoves(initialstate);
        System.out.println("\nMoves available for the initial state are: " + moves);
        int movestate[][] = moveGenerator(initialstate, moves);
        double heuristicvalues3[] = new double[moves];

        for (int i = 0; i < moves; i++) {
            double count = 0;
            System.out.println("Move " + (i + 1));
            for (int j = 0; j < 9; j++) {
                System.out.print(movestate[i][j] + " ");
               double x = Math.abs(goalstate[j] - movestate[i][j]);
               x = Math.pow(x, 2);
               double y = Math.abs(goalstate[j] - movestate[i][j]);
               y = Math.pow(y, 2);
               count += Math.sqrt(x+y);
            }
            heuristicvalues3[i] = count;
            System.out.println();
            
        }
        System.out.println("\nHeuristic Function 3(Euclidean Distance) values are:");
        for (int i = 0; i < heuristicvalues3.length; i++) {
            System.out.print(heuristicvalues3[i] + " ");
        }
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
                if(movestate[i][j] != goalstate[j])
                    count+=1;
            }
            double newcount = count;
            heuristicvalues4[i] = newcount/9;
            System.out.println();
        }
        System.out.println("\nHeuristic Function 4(Jaccard Distance) values are:");
        for (int i = 0; i < heuristicvalues4.length; i++) {
            System.out.print(heuristicvalues4[i] + " ");
        }
        System.out.println("\n********************************************");
    }
}

import java.io.*;
import java.util.*;
/**
 * PuzzleProblem
 */
public class PuzzleProblem {
    public static void main(String[] args) {
        int [] initialstate = {2,8,3,1,6,4,7,0,5};
        int [] goalstate = {1,2,3,8,0,4,7,6,5};
        System.out.println("\nInitial State is:");
        for (int i = 0; i < initialstate.length; i++) {
            System.out.print(initialstate[i]+" ");
        }
        System.out.println("\nGoal State is");
        for (int i = 0; i < initialstate.length; i++) {
            System.out.print(goalstate[i]+" ");
        }
        heuristicFunction1(initialstate,goalstate);
    }

    public static int checkMoves(int [] initialstate)
    {
        int moves = 0;
        for (int i = 0; i < initialstate.length; i++) {
            if(initialstate[i]==0)
            {
                if(i==0 || i==2 || i==6 || i==8)
                    moves = 2;
                else if(i==1 ||i==3 ||i==5||i==7)
                    moves = 3;
                else 
                    moves = 4;
            }          
        }
        return moves;
    }

    public static int[][] moveGenerator(int [] initialstate,int moves) {
        int [][] movestate = new int [4][9];
        for (int i = 0; i < moves; i++) {
            for (int j = 0; j < 9; j++) {
                movestate[i][j] = initialstate[j];
            }
        }
        int up = 0, down = 0, left = 0, right = 0;
        for (int i = 0; i < moves; i++) {
            for (int j = 0; j < 9; j++) {
                if(movestate[i][j]==0)
                {
                    if(j>=3 && up==0)
                    {
                        movestate[i][j] = initialstate[j-3];
                        movestate[i][j-3] = initialstate[j];
                        up++;
                    }
                    else if(j<=5 && down == 0)
                    {
                        movestate[i][j] = initialstate[j + 3];
                        movestate[i][j + 3] = initialstate[j];
                        down++;
                    }
                    else if(((j==2 || (j-2)%3==0)||((j-1)%3==0 || j==1))&& left==0)
                    {
                        movestate[i][j] = initialstate[j-1];
                        movestate[i][j-1] = initialstate[j];
                        left++;
                    }
                    else if (((j == 0 || j % 3 == 0) || ((j - 1) % 3 == 0 || j == 1)) && right == 0) {
                        movestate[i][j] = initialstate[j + 1];
                        movestate[i][j + 1] = initialstate[j];
                        right++;
                    }
                }
            }
        }
        return movestate;
    }

    private static void heuristicFunction1(int[] initialstate, int[] goalstate) {
        int moves = checkMoves(initialstate);
        System.out.println("\nMoves available for the initial state are: "+moves);
        int movestate[][] = moveGenerator(initialstate, moves);
        int heuristicvalues[] = new int[moves];
       for (int i = 0; i < moves; i++) {
           int count = 0;
           for (int j = 0; j < 9; j++) {
               if(goalstate[j] != movestate[i][j])
                count++;
           }
           heuristicvalues[i] = count;
       }
       System.out.println("\nHeuristic Function 1 values are:");
       for (int i = 0; i < heuristicvalues.length; i++) {
           System.out.print(heuristicvalues[i]+" ");
       }
       System.out.println("\n********************************************");
    }

    

    
}
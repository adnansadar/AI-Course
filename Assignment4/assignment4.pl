#Family Tree
/*                          John     Mary
                              |______|
                      Bob    Sue    Bill     Jane 
                       |______|       |________|
                        |____|             |
                     Nancy  Jeff          Ron                             

*/

#FACTS
male(john).
male(bob).
male(bill).
male(ron).
male(jeff).

female(mary).
female(sue).
female(nancy).
female(jane).

mother(mary, sue). 
mother(mary, bill).
mother(sue, nancy).
mother(sue, jeff).
mother(jane, ron).

father(john, sue).
father(john, bill).
father(bob, nancy).
father(bob, jeff).
father(bill, ron).

sibling(bob,bill).
sibling(sue,bill).
sibling(nancy,jeff).
sibling(nancy,ron).
sibling(jell,ron).


#RULES
aunt(X,Y) :-
  parent(Z,Y), sister(X,Z). 

uncle(X,Y) :-
  parent(Z,Y), brother(X,Z). 

sibling(X, Y) :-
      parent(Z, X),
      parent(Z, Y),
      X \= Y. 

sister(X, Y) :-
      sibling(X, Y),
      female(X).

brother(X, Y) :-
      sibling(X, Y),
      male(X).

parent(Z,Y) :- father(Z,Y).
parent(Z,Y) :- mother(Z,Y).

cousinsister(X,Y) :-
      female(X),
      parent(Z,X),
      parent(W,Y),
      sibling(W,Z).

cousinbrother(X,Y) :-
      male(X),
      parent(Z,X),
      parent(W,Y),
      sibling(W,Z).

husband(X,Y):-
      male(X),
      parent(X,Z),
      parent(Y,Z).

wife(X,Y):-
      female(X),
      parent(X,Z),
      parent(Y,Z).


grandfather(C,D) :- parent(C,E), parent(E,D).
grandmother(C,D) :- parent(C,E), parent(E,D).





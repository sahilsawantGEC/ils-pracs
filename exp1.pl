likes(john,rice).
likes(john,biryani).

male(adam).
male(joe).
male(john).
female(lavina).
female(neelda).
father(adam,joe).
father(adam,john).
father(adam,lavina).
father(adam,neelda).
siblings(X,Y):-father(Z,X),father(Z,Y).
brothers(A,B):-father(C,A),father(C,B),male(A),male(B).
sisters(P,Q):-father(R,P),father(R,Q),female(P),female(Q).


man(symbol).
man(marcus).
indian(symbol).
indian(marcus).
died(symbol,int).
died(P,T):-indian(P),gt(T,1979),write(''),write(P),write(' is dead').
alive(symbol,int).
alive(X,T):-not(died(X,T)).
gt(int,int).
gt(OP1,OP2):-OP1>OP2.
readname(symbol).
readname(N):-write('Enter your name'),read(N).
readyear(int).
readyear(Y):-write('Enter the year'),read(Y).
start:-readname(N),readyear(Y),died(N,Y).

move(1,8).
move(1,6).
move(2,9).
move(2,7).
move(3,4).
move(3,8).
move(4,3).
move(4,9).
move(6,1).
move(6,7).
move(7,2).
move(7,6).
move(8,1).
move(8,3).
move(9,2).
move(9,4).

path(X,Y):-move(X,Y).
path2(X,Y,Z):-path(X,Z),move(Z,Y).
path3(X,Y):-path2(X,Z,U),move(Z,Y),
nl,write('path exists and is from'),
nl,write(X),write('-'),write(U),
nl,write(U),write('-'),write(Z),
nl,write(Z),write('-'),write(Y);
write('Path does not exist').

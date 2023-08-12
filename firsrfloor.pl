room(library).
room(auditoriam).
room(passage).
room(incubationcenter).
room(cabin).
door(passage,incubationcenter).
door(incubationcenter,cabin).
door(passage,auditoriam).
door(passage,library).
location(waterfilter,passage).
location(computer_systems,incubationcenter).
location(desk,cabin).
location(laptop,cabin).
location(music_system,auditoriam).
location(projector,auditoriam).
location(bookshelf,library).
location(books,library).

connect(X,Y):- door(X,Y).
connect(X,Y):- door(Y,X).

list_things(Place):- location(X,Place),write(''),write(X),fail.
list_things(Place).

list_adjacent(Place):- connect(X,Place),write(''),write(X),fail.
list_adjacent(Place).

start():-write("Enter your location"),read(X),write("Your items in that place"),connect(X,_),list_things(X),nl,write("Your adjacent rooms are"),list_adjacent(X).
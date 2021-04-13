room(office).
room(lab).
room(hallway).
room(hallway_2).
room(classroom).


door(d_1).
door(d_2).
door(d_3).
door(d_4).


hasdoor(lab,d_1).
hasdoor(hallway,d_1).


hasdoor(hallway,d_2).
hasdoor(hallway_2,d_2).

hasdoor(office,d_3).
hasdoor(hallway,d_3).

hasdoor(classroom,d_4).
hasdoor(hallway_2,d_4).







location(R) :- room(R).

dooracc(R1,D,R2) :- hasdoor(R1,D), hasdoor(R2,D), R1 != R2, door(D), room(R1),
location(R2).
dooracc(R1,D,R2) :- dooracc(R2,D,R1).

acc(L1,L1) :- location(L1).
acc(L1,L2) :- acc(L2,L1), location(L1), location(L2). 
acc(L1,L2) :- acc(L1,L3), acc(L2,L3), location(L1), location(L2), location(L3).





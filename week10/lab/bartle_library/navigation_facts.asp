%%%%%% Fill in here with the facts about rooms and doors in the bartle library G floor
%%%%%%%%%%%%%%%%%%%%%% 

room(lng208).
room(polisci).
room(hallway_1).
room(hallway_2).


door(d_1).
door(d_2).


hasdoor(lng208,d_1).
hasdoor(polisci,d_2).
hasdoor(hallway_1,d_1).
hasdoor(hallway_1,d_2).
hasdoor(hallway_2,d_1).
hasdoor(hallway_2,d_2).




















%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


location(R) :- room(R).

dooracc(R1,D,R2) :- hasdoor(R1,D), hasdoor(R2,D), R1 != R2, door(D), room(R1),
location(R2).
dooracc(R1,D,R2) :- dooracc(R2,D,R1).

acc(L1,L1) :- location(L1).
acc(L1,L2) :- acc(L2,L1), location(L1), location(L2). 
acc(L1,L2) :- acc(L1,L3), acc(L2,L3), location(L1), location(L2), location(L3).





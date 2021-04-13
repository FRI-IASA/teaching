% Default
#const n = 3.

% Generate
{ color(X,1..n) } = 1 :- area(X).
% Test
:- hasborder(X,Y), color(X,C), color(Y,C).

% Areas

area(a).
area(b).
area(c).
area(d).
area(e).
area(f).

% Borders
hasborder(a,(b;c;d)).  
hasborder(b,(a;d;e;f)).  
hasborder(c,(a;d;e)).
hasborder(d,(a;b;c)).    
hasborder(e,(c;b;f)).  
hasborder(f,(e;b)).


% Display
#show color/2.
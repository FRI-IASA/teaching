bird(waldo).
bird(tux).
penguin(tux).
flies(X) :- bird(X), not -flies(X).
-flies(X) :- penguin(X).
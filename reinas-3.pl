% Calcula la posición de las reinas en un tablero de N-casillas de lado
% L-lista: cada posición es la columna del tablero, cada número es el
% renglón donde está la reina
reinas(N,L):-sol(N,L).

% La primera solución es una lista con N-elementos
% Después de generar la solución, comprobamos con sol2 si es correcta
sol(N,L):-
    meta(N,L), sol2(N,L).

% Construye la primera solución a partir del tamaño de N.
% Generamos una lista desde 1 hasta N y nos aseguramos que no estén
% duplicados los elementos antes de mandarlos a comprobar
meta(N,L):-length(L,N), maplist(between(1, N), L), not(duplicate(L)).
%% meta(N,L):-length(L,N), maplist(between(1, N), L).

% Comprobamos que dentro de la lista no haya dupicados.
duplicate(L):-
    append(X,Y,L),
    member(M,X),
    member(M,Y).

% N-columna, S-lista solucion
%% TODO: checar uno por uno si no se chocan [X|Xs]
sol2(N,[X|Xs]):-
    not(member(X, Xs)),
    % Comprobar que X no está en la misma diagonal con el resto de Xs
    no_ataca(N,X,Xs), !,
    sol2(N,Xs).

sol2(N,[]).

% Comprobar que los elementos anteriores en la S-solución no están en la diagonal
% Sigue calculando si ataca en la diagonal hacia abajo
% Los casos base es cuando tenemos una lista vacía o un cero
no_ataca_negativo(N,C,[]).
no_ataca_negativo(N,0,T).
no_ataca_negativo(N,C,[T|Ts]):-
    C1 is C - 1,
    C1 \= T,
    no_ataca_negativo(N,C1,Ts).
% Sigue calculando si ataca en la diagonal superior
% Los casos base es cuando tenemos una lista vacía o un cero
no_ataca_positivo(N,C,[]).
no_ataca_positivo(N,N + 1,T).
no_ataca_positivo(N,C,[T|Ts]):-
    C1 is C + 1,
    C1 \= T,
    no_ataca_positivo(N,C1,Ts).

% N-numero de Reinas y por lo tanto casillas en cada lado
% C-casilla actual
% S-Lista solución
no_ataca(N,C,[]).
no_ataca(N,C,S):-
    no_ataca_negativo(N,C,S),
    no_ataca_positivo(N,C,S).

% Escogemos un C-número desde 1 hasta N
sig(N,C):-
	  enum(1,N,L),
	  member(C,L).

% Creamos una L-lista con los elementos desde 1 hasta B
enum(A,A,[A]).
enum(A,B,[A|S]):-
	  A < B,
	  C is A + 1,
	  enum(C,B,S).

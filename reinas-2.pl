% Calcula la posición de las reinas en un tablero de N-casillas de lado
% L-lista: cada posición es la columna del tablero, cada número es el
% renglón donde está la reina
reinas(N,L):-sol2(N,[],L).

%% % La primera solución es una lista con N-elementos
%% sol2(N,[],L):-
%%     meta(N,L), sol2(N,L).

%% % Construye la primera solución a partir del tamaño de N.
%% meta(N,L):-length(L,N), maplist(between(1, N), L).

% N-columna, S-lista solucion
sol2(N,S,L):-
    % Escoge un C-número desde 1 hasta N
    sig(N,C),
    % Comprueba que C no pertenezca a la lista S-solucion.
    % Es decir, no está en el mismo renglón
    not(member(C,S)),
    % Comprobar que C no está en la misma diagonal
    no_ataca(N,C,S),
    sol2(N,[C|S],L).

% Comprobar que los elementos anteriores en la S-solución no están en la diagonal
% no_ataca(N,C,S).
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
no_ataca_positivo(N,N,T).
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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%             Servidor
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- use_module(library(socket)).

:- consult(reinas).

servidor:-
    tcp_socket(Socket), 
    tcp_bind(Socket, 50000), 
    tcp_listen(Socket, 5), 
    tcp_open_socket(Socket, AcceptFd, _),
    dispatch(AcceptFd).

dispatch(AcceptFd):-
    tcp_accept(AcceptFd, Socket, Peer),
    process_client(Socket, Peer).
%     thread_create(process_client(Socket, Peer), _,
%                      [ detached(true)
%                      ]).
    % dispatch(AcceptFd). % Con esta linea se pueden atender muchas llamadas
    % Sin ella solo se atiende una llamada

process_client(Socket, Peer) :-
        write(' Recibi llamada de: '), write(Peer), nl,
        setup_call_cleanup(
            tcp_open_socket(Socket, StreamPair),
            doService(StreamPair),
            close(StreamPair)).

%% Reinas
doService(Stream):-
    % Manda Varias cadenas
    repeat,
    %% N - numero de reinas, L - lista de soluciones
    read(Stream, N),
    %% read(Stream, L),
    %% (reinas(N, L), write(Stream, L), nl;
    %%  write(Stream, no)),
    %% reinas(N, L), write(Stream, L), write(Stream, 13),
    reinas(N, L), writeln(Stream, L),
    flush_output(Stream),
    E==fin, % Aca terminas
    !,
    write(' Adios '), nl.

%%% Lo del metro
%% doService(Stream):-
%%     % Manda Varias cadenas
%%     repeat,
%%        % Lee estacion del metro
%%        read(Stream,E),
%%        write('La estacion es '),write(E),nl,
%%        (linea(N,L),member(E,L),
%%        write(Stream, N), put(Stream, 13), put(Stream, 10),
%%        write(Stream, L), put(Stream, 13), put(Stream, 10);
%%         write(Stream, no), put(Stream, 13), put(Stream, 10)),
%%        flush_output(Stream),
%%     E==fin, % Aca terminas
%%     !,
%%     write(' Adios '), nl.

%%% Lo de las listas
%% doService(Stream):-
%%     % Manda Varias cadenas
%%     repeat,
%%     % Antes era member(X, [hola,esta,es,una,prueba,fin]),
%%     read(Stream,L),read(Stream,E),
%%     (member(E,L), write(Stream, yes), put(Stream, 13), put(Stream, 10);
%%      not(member(E,L)),write(Stream, no), put(Stream, 13), put(Stream, 10)),
%%     flush_output(Stream),
%%     E==fin, % Aca terminas
%%     !,
%%     write(' Adios '), nl.

member(X, [X|Xs]).
member(X, [Y|Ys]):-member(X,Ys).

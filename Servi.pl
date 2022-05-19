%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%             Servidor
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- use_module(library(socket)).

:- consult(reinas).

% Crear el servidor
servidor:-
    tcp_socket(Socket),
    tcp_bind(Socket, 50000),
    tcp_listen(Socket, 5), % Cambia el timeout del socket
    tcp_open_socket(Socket, AcceptFd, _),
    % Función que acepta las entradas y genera una respuesta
    dispatch(AcceptFd).

dispatch(AcceptFd):-
    tcp_accept(AcceptFd, Socket, Peer),
    process_client(Socket, Peer),
    dispatch(AcceptFd).

process_client(Socket, Peer):-
    write('Recibi llamada de: '), writeln(Peer),
    setup_call_cleanup(
        tcp_open_socket(Socket, In, Out),
        doService(In, Out),
        close_connection(In, Out)).

close_connection(In, Out):-
    close(In, [force(true)]),
    close(Out, [force(true)]).

%% Reinas
doService(In, Out):-
    repeat,
    read(In, N), writeln(N),
    (N == end_of_file -> true
    ;
    reinas(N, Sol), writeln(Out, Sol),
    %% setof(Sol, reinas(N, Sol),Bag), writeln(Out, Bag),  % Generar una lista con todas las soluciones
    flush_output(Out),
    doService(In, Out)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Para correr esta aplicación:
%% Primero: Correr el servidor de swipl con el comando:
%% swipl -l Servi.pl -g true -g servidor
%% Luego ejecutar la gui:
%% python GUIClase.py

%% Librería para hacer el servidor
:- use_module(library(socket)).

%% Leemos los predicados que tenemos en reinas.pl
:- consult(reinas).

% Crear el servidor
servidor:-
    % Crea un socket
    tcp_socket(Socket),
    % Lo monta en la dirección 50000
    tcp_bind(Socket, 50000),
    % Cambia el timeout del socket
    tcp_listen(Socket, 5),
    % Abre el socket y empieza a recibir peticiones
    tcp_open_socket(Socket, AcceptFd, _),
    % Función que acepta las entradas y genera una respuesta
    dispatch(AcceptFd).

%% Administra las peticiones al servidor
dispatch(AcceptFd):-
    %% Acepta las conexiones de clientes
    tcp_accept(AcceptFd, Socket, Peer),
    %% Crea un hilo para recibir el cliente y empezar a darle un
    %%   servicio
    process_client(Socket, Peer),
    %% Vuelve a administrar peticiones al servidor
    dispatch(AcceptFd).

%% Procesar las peticiones del cliente
process_client(Socket, Peer):-
    % Imprimir información del cliente en prolog
    write('Recibi llamada de: '), writeln(Peer),
    % Administrar los recursos para atender al cliente
    setup_call_cleanup(
        % Abre el socket para obtener y enviar datos
        tcp_open_socket(Socket, In, Out),
        % Función que se encarga de procesar la petición
        doService(In, Out),
        % Cerrar el socket al cerrar la conexión si el cliente cierra
        % la conexión
        close_connection(In, Out)).

%% Cerrar los Stream del socket
close_connection(In, Out):-
    % Entrada
    close(In, [force(true)]),
    % Salida
    close(Out, [force(true)]).

%% Procesar las entradas y ejecutar los predicados de reinas.pl
doService(In, Out):-
    % Volver a pedir entradas en el socket cuando se da una solución
    repeat,
    % Leer lo que se encuentra en el socket e imprimirlo en prolog
    read(In, N), writeln(N),
    % Acción si se cierra la conexión, para no detener el servidor
    (N == end_of_file -> true
    ;
    % Si hay algo en el socket, ejecutar reinas/2 en la entrada
    % La solución la mandamos al Stream de Out
    reinas(N, Sol), writeln(Out, Sol),  % Generar solo una solución
    %% setof(Sol, reinas(N, Sol),Bag), writeln(Out, Bag),  % Generar una lista con todas las soluciones
    % Limpiar el Stream de salida
    flush_output(Out), !,
    % Volver a repetir este predicado
    doService(In, Out)).

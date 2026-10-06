create table time(
    id number generated always as identity,
    nome varchar(30),
    vitorias number(2, 0),
    empates number(2, 0),
    jogos number(2, 0),
    primary key(id)
);

create table partida(
    id number generated always as identity,
    nome_mand varchar(30),
    placar_mand number(2, 0),
    id_mand number,
    nome_visi varchar(30),
    placar_visi number(2, 0),
    id_visi number,
    primary key(id),
    foreign key(id_mand) references time(id),
    foreign key(id_visi) references time(id)
);

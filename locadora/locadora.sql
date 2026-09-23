create table TB_VEICULO (
    id number generated always as identity,
    placa varchar(20) not null,
    ano number (4),
    modelo varchar(50) not null,
    marca varchar(50),
    cor varchar(20),
    km number (7),
    valor number (6, 2),
    unique (placa),
    primary key (id)
);

create table tb_cliente (
    id number generated always as identity,
    nome varchar(100) not null,
    telefone varchar(50) not null,
    PRIMARY KEY (id)
);

create table tb_locacao (
    id number generated always as identity,
    retirada date,
    entrega date,
    valor number (6, 2),
    km number (7),
    status varchar(10),
    id_veiculo number,
    id_cliente number,
    PRIMARY key (id),
    Foreign Key (id_veiculo) REFERENCES tb_veiculo (id),
    Foreign Key (id_cliente) REFERENCES tb_cliente (id)
);


insert into tb_cliente(nome, telefone) VALUES('Edu Gondo', '(11) 837432');
insert into tb_cliente(nome, telefone) VALUES('Thiago Yamamoto', '(11) 947352');
insert into tb_cliente(nome, telefone) VALUES('Alexandre Faria', '(11) 8493543');
insert into tb_cliente(nome, telefone) VALUES('Rose Almeida', '(11) 73495435');
insert into tb_cliente(nome, telefone) VALUES('Donald Trump', '(11) 9348523');

CREATE TABLE login (
cod_login INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
senha TEXT NOT NULL
);

CREATE TABLE crud_aluno(
cod_crud_aluno integer PRIMARY KEY AUTOINCREMENT,
nome text ( 50 ) NOT NULL,
data_nascimento	date NOT NULL,
endereco text ( 100 ) NOT NULL,
bairro text ( 50 ) NOT NULL,
cidade text ( 100 ) NOT NULL,
uf text ( 2 ) NOT NULL
);

create table marcar_excluir_aluno(
cod_marcar_excluir_aluno integer primary key autoincrement,
cod_crud_aluno integer not null,
data_marcou_excluir date not null, 
cod_usuario_marcou_excluir integer not null,
data_exclusao date, 
cod_usuario_excluiu integer,
excluido text(1) not null check(excluido in ('S', "N")),
constraint fk_marcar_excluir_aluno_cod_usuario_marcou_excluir 
foreign key (cod_usuario_marcou_excluir) references login(cod_login),
constraint fk_marcar_excluir_aluno_cod_usuario_excluiu 
foreign key (cod_usuario_excluiu) references login(cod_login)
);


/*Sql extra*/

/*Tabela CRUD*/
insert into crud_aluno
(nome, data_nascimento, endereco, bairro, cidade, uf) 
values ('MICHAEL', '27/02/1994', 'RUA A', 'BAIRRO A', 'CIDADE A', 'SP');

/*Tabela Historico exclusão*/
insert into marcar_excluir_aluno
(cod_crud_aluno, data_marcou_excluir,
cod_usuario_marcou_excluir, data_exclusao,
cod_usuario_excluiu, excluido)
values (2, '16/07/2020', 1, null, null, 'N');

/*Sql exibição Grade cru*/
select al.nome , al.data_nascimento,
al.endereco, al.bairro, al.cidade,
al.uf, ex.excluido
from crud_aluno al
join marcar_excluir_aluno ex
on (ex.cod_crud_aluno = al.cod_crud_aluno)
where ex.excluido = 'N';

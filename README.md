# ProjetoControleProducao

### Projeto utilizado na disciplina de Desenvolvimento de Sistemas em Python, apresentando como tema o controle de produção.

Neste contexto, o sistema deverá controlar o estoque de produtos e de matérias-primas, que serão cadastrados previamente (com estoque em 0). Com isso, o sistema irá controlar as produções que estão em processo e as produções já finalizadas. Toda produção apresenta um produto produzido e a sua quantidade esperada. Ao finalizar a produção, o estoque do produto deverá ser atualizado.

Toda produção apresenta também um ou mais processos, cada processo com sua hora inicial e final, que serão usadas para calcular o tempo gasto em cada processo e o tempo da produção inteira. Cada processo pode utilizar uma, nenhuma ou várias matérias-primas, que serão descontadas do estoque ao final de cada processo e serão utilizadas para calcular o custo do processo e da produção. O processo será realizado por um ou mais funcionários, além de possuir um supervisor, que poderá definir aquele processo como válido ou não. Ou seja, a produção pode apresentar processos repetidos, ou seja, com o mesmo tipo de processo (que será cadastrado previamente), aumentando o tempo e o custo da produção. Os funcionários apresentarão um cargo, já cadastrado no sistema.

Neste contexto não estão sendo controladas as vendas dos produtos e nem a compra de matéria-prima, que poderá ser um módulo implementado futuramente.
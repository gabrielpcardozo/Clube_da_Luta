# Clube da luta

A ideia dessa projeto é criar um jogo com um sistema de batalhas por turnos.

Aqui vai ser um teste de colocar dois lutadores para lutar e estudar como que eu posso trabalhar melhor com as intâncias para usar no PokeAPI.

No arquivo services.py
Primeira versão eu comecei criando somente duas variáveis com as informações necessárias e criei um Loop para simular um sistema de batalha, a luta em sí é simples, acabada quando um dos jogadores estiverem com a vida = 0.

No arquivo lutadores.py e no main.py estão a versão 2.
Nessa segunda versão eu vou adicionar os testes e modernizar ainda mais com funções e mais personagens. 

|Personagems| Tipo      |
|-----------|-----------|
| Mediv     | Mage      |
| Arthur    | Warrior   |
| Katarina  | Archer    |

Os personagens são mais para uma característica a mais mas os danos a princípio vão ser os mesmos.

Na versão 2 são classes nesse sistema de batalha realizando a troca de golpes, sendo que cada persongem tem um poder único porém todos aplicam o mesmo dano. 

Na versão 3 eu quero desenvolver algumas novidades.

Uma das ideias é criar um sistema de balanciamento, como por exemplo(Exemplo fora de contexto):
Agua tem vantagem contra fogo.

Tembém quero fazer uma batalha de times, onde sejam três de cada lado, simulando uma batalha de turno com mais personagens. 
    Para isso quero criar subclasses como Tank, DPs e Support. 
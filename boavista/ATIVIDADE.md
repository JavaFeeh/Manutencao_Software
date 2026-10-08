# 🏢 Bem-vindo(a) à Distribuidora Boa Vista!

Parabéns, você acabou de ser contratado(a) como **desenvolvedor(a) de manutenção**.

O sistema de pedidos da empresa foi feito pelo **João**, que trabalhou aqui sozinho de 2019 a 2021 e **saiu da empresa**. Ele não responde mais mensagens. O que ficou foi este repositório, algumas anotações e muitos usuários reclamando.

Seu gerente, **Carlos**, precisa que o sistema volte a funcionar direito. Ninguém sabe exatamente como ele funciona — descobrir isso faz parte do seu trabalho.

> **Regras da atividade**
> - Trabalhe em dupla ou trio.
> - Cada correção deve virar **um commit separado**, com uma mensagem clara (ex.: `corrige remoção de produto que apagava o item errado`).
> - Anote no arquivo `DIARIO.md` (crie você mesmo) **quanto tempo gastou entendendo** e **quanto tempo gastou alterando** em cada missão.
> - Não existe um "jeito único" de corrigir. Justifique suas decisões.

---

## 📄 Regras de negócio (enviadas pelo Carlos por e-mail)

1. Clientes **VIP** têm **10%** de desconto.
2. Pedidos com valor de produtos **acima de R$ 500,00** têm **5%** de desconto.
3. Os descontos **não são cumulativos**: vale apenas **o maior** deles.
4. Pedidos com valor de produtos **abaixo de R$ 100,00** pagam **frete de R$ 15,00**.
5. **Não é permitido** vender mais do que existe em estoque.
6. Valores em dinheiro sempre com **2 casas decimais** (ex.: `R$ 42,90`).
7. O relatório de vendas deve mostrar **exatamente a soma** dos totais dos pedidos.

---

## 🚪 Fase 1 — Primeiro dia: fazer o sistema rodar

**Missão 1.1** — Siga o `README.md` e tente rodar o sistema. Deu certo? Anote cada obstáculo que encontrou e como resolveu.

**Missão 1.2** — Faça login e liste os produtos. O arquivo `dados.json` tem 7 produtos cadastrados. Eles aparecem? Se não, descubra por quê.

**Missão 1.3** — Antes de mexer em qualquer coisa, faça um **mapa do sistema**: quais arquivos existem, quais são realmente usados, qual é o ponto de entrada e o que cada função faz.

---

## 🎫 Fase 2 — Chamados abertos pelos usuários

Os chamados foram escritos pelos usuários, do jeito que eles escrevem. Reproduza o problema **antes** de corrigir.

| Chamado | Aberto por | Descrição |
|---|---|---|
| **#101** | Vendedora Ana | "Toda vez que coloco Sabão em Pó num pedido aparece 'Ocorreu um erro' e o pedido some." |
| **#102** | Estoquista Paulo | "Fui remover o Feijão e o sistema apagou o Óleo!!!" |
| **#103** | Mercadinho São Jorge (VIP) | "Comprei 40 pacotes de café (R$ 700,00) e paguei R$ 538,65. Pelas regras eu deveria pagar R$ 630,00. Acho ótimo, mas o Carlos ficou furioso." |
| **#104** | Restaurante Sabor Caseiro (VIP) | "Sou cliente VIP e não recebo desconto nenhum." |
| **#105** | Estoquista Paulo | "O estoque de Detergente está **-47**. Como assim?" |
| **#106** | Carlos (gerente) | "O relatório de vendas diz um valor e a soma dos pedidos dá outro. Qual está certo?" |
| **#107** | Vendedora Ana | "Pesquiso 'arroz' e o sistema diz que não tem. Mas tem!" |
| **#108** | Vendedora Ana | "Tentei cadastrar um produto com preço 4,99 e deu erro." |
| **#109** | Estoquista Paulo | "Depois que removi um produto e cadastrei outro, ficaram **dois produtos com o mesmo ID**." |
| **#110** | Carlos (gerente) | "O João dizia que dava pra exportar os pedidos pra planilha. Cadê?" |
| **#111** | Vendedora Ana | "As datas dos pedidos estão cada uma de um jeito e os valores aparecem tipo `463.93155`." |

---

## 🧹 Fase 3 — Deixando a casa em ordem

Agora que o sistema funciona, deixe-o **mais fácil de manter** para a próxima pessoa (que pode ser você daqui a 6 meses).

- **3.1** — Existem **senhas e credenciais** escritas em lugares onde não deveriam. Encontre todas e proponha o que fazer.
- **3.2** — O cálculo do total do pedido aparece **em mais de um lugar** (e em mais de um arquivo). Deixe-o em um lugar só.
- **3.3** — Descubra o que é **código morto**, arquivos que ninguém usa e dependências desnecessárias. Remova o que for seguro remover (e justifique).
- **3.4** — Renomeie variáveis e funções para nomes que expliquem o que elas são. Padronize o estilo dos nomes.
- **3.5** — Substitua os "números mágicos" (0.1, 500, 15, 5...) por algo com nome. O `config.txt` serve pra alguma coisa?
- **3.6** — O sistema "engole" os erros. Faça com que erros sejam tratados e informados de forma útil.
- **3.7** — Escreva **testes automatizados** (ex.: `unittest` ou `pytest`) para as regras de negócio 1 a 4. O arquivo `teste.py` atual é um teste de verdade?
- **3.8** — Reescreva o `README.md` para que um novo desenvolvedor consiga rodar o sistema em 5 minutos.
- **3.9** — Crie um `.gitignore` adequado e um `requirements.txt` (se fizer sentido).

---

## 🚀 Fase 4 — Pedido novo do Carlos

> "Na Black Friday, produtos da categoria **limpeza** terão **20% de desconto**. Preciso disso pra semana que vem."

Implemente. Depois responda: **foi mais fácil ou mais difícil do que seria antes da Fase 3? Por quê?** Você encontrou algum problema nos dados que atrapalhou?

---

## 🤔 Reflexão final (entregar por escrito)

1. Classifique cada alteração que você fez como **corretiva**, **adaptativa**, **perfectiva** ou **preventiva**.
2. Qual porcentagem do seu tempo foi gasta **entendendo** o código versus **alterando**?
3. Quais informações do `NOTAS_DO_JOAO.txt` ajudaram? Quais estavam erradas ou atrapalharam?
4. Se o João tivesse deixado **uma única coisa** feita, o que você mais gostaria que fosse?
5. Que práticas você vai adotar nos seus próprios projetos para não deixar uma herança assim?

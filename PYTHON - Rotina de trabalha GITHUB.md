# ROTINA_GIT.md

## Rotina de trabalho com Git, GitHub e Streamlit

Este arquivo é um lembrete prático para trabalhar nos projetos
Python/Streamlit usando VS Code, GitHub e Streamlit Community Cloud.

> **Regra principal:** faça as alterações no computador, teste
> localmente, registre-as em um commit e só então envie ao GitHub. O
> Streamlit Cloud normalmente detecta o novo commit e atualiza o
> aplicativo automaticamente. Não é necessário apagar o repositório nem
> refazer o deploy.

------------------------------------------------------------------------

## 1. Antes de começar

Abra o Terminal integrado do VS Code na pasta correta do projeto.

Confira o ambient virtual
source .venv/bin/activate

Confira a situação:

``` bash
pwd
git status
git branch --show-current
git remote -v
```

-   `pwd` mostra a pasta atual.
-   `git status` mostra se há alterações pendentes.
-   `git branch --show-current` mostra a branch atual.
-   `git remote -v` mostra para qual repositório remoto o projeto
    aponta.

### Se a pasta estiver limpa

Se `git status` disser que a árvore de trabalho está limpa
(`working tree clean`), atualize sua cópia local:

``` bash
git pull --rebase origin main
```

**Atenção:** se houver arquivos modificados ou não rastreados, pare e
examine-os antes de fazer o `pull`. Não descarte alterações que você
ainda não conferiu.

------------------------------------------------------------------------

## 2. Fazer alterações e testar localmente

Edite os arquivos no VS Code. Evite editar os mesmos arquivos
diretamente no site do GitHub.

Para iniciar o BibleWaze:

``` bash
streamlit run BibleWaze.py
```

Em outro projeto, use o nome correto do arquivo principal, por exemplo:

``` bash
streamlit run falcon.py
```

Teste as funções que foram alteradas antes de publicar.

------------------------------------------------------------------------

## 3. Registrar as alterações

Adicione somente os arquivos que realmente fazem parte da mudança.

Exemplo para o BibleWaze:

``` bash
git add BibleWaze.py biblewaze.csv
git status
git commit -m "Descreve a alteração"
```

Exemplo de mensagem:

``` bash
git commit -m "Corrige ordenação dos livros"
```

O `git status` antes do commit permite conferir o que será incluído.
Evite adicionar arquivos temporários como `.DS_Store` e `__pycache__/`.

------------------------------------------------------------------------

## 4. Enviar ao GitHub

``` bash
git push origin main
```

Interpretação das mensagens:

-   `Everything up-to-date`: não há commits locais novos para enviar.
-   Mensagem de sucesso com objetos enviados: o commit foi enviado ao
    GitHub.
-   `rejected` ou `fetch first`: o remoto tem alterações que ainda não
    estão na cópia local. Não use `--force`. Pare e examine a situação
    antes de continuar.

**Lembrete:** `git push` envia commits. Ele não envia alterações que
ainda estão apenas no computador e não foram registradas com
`git commit`.

------------------------------------------------------------------------

## 5. Conferir o Streamlit Cloud

1.  Abra <https://share.streamlit.io/>.
2.  Localize o aplicativo correto.
3.  Confira se a publicação foi iniciada e se terminou sem erro.
4.  Se não atualizar, examine os logs e confirme se o aplicativo está
    ligado ao repositório, à branch e ao arquivo principal corretos.

Normalmente, um `git push` bem-sucedido dispara a atualização
automaticamente. Não apague o aplicativo para tentar resolver um erro.

------------------------------------------------------------------------

## 6. Se aparecer um conflito de Git

Marcadores como estes indicam que o Git não conseguiu conciliar duas
versões:

``` text
<<<<<<<
=======
>>>>>>>
```

O que fazer:

1.  Pare e execute `git status`.
2.  Identifique todos os arquivos indicados como conflitantes.
3.  Compare as versões e decida o conteúdo correto, preservando as
    alterações necessárias.
4.  Remova os marcadores e deixe o arquivo com código/dados válidos.
5.  Confira se não restaram marcadores.
6.  Marque os arquivos resolvidos com `git add`.
7.  Se estiver no meio de um rebase, continue com
    `git rebase --continue` somente depois de resolver todos os
    conflitos.

Não use `git rebase --skip`, `git rebase --abort` ou `git push --force`
sem entender as consequências.

------------------------------------------------------------------------

## 7. Três regras de ouro

1.  **Edite no VS Code.** Evite modificar o mesmo projeto em paralelo no
    computador e no GitHub.
2.  **Não apague o repositório ou o aplicativo** para tentar corrigir um
    problema de publicação.
3.  **Faça commits pequenos e frequentes.** Fica mais fácil localizar e
    corrigir problemas.

------------------------------------------------------------------------

## Checklist rápido

Antes de terminar uma sessão:

-   [ ] Testei o aplicativo localmente.
-   [ ] Conferi `git status`.
-   [ ] Adicionei apenas os arquivos necessários.
-   [ ] Criei um commit com uma mensagem clara.
-   [ ] Executei `git push origin main`.
-   [ ] Conferi a atualização no Streamlit Cloud.

**Importante:** adapte os nomes dos arquivos ao projeto em que estiver
trabalhando. Antes de executar comandos, confirme sempre que está na
pasta, no repositório e na branch corretos.



Sua rotina de atualização
# 1. Verificar alterações
git status

# 2. Adicionar os arquivos
git add falcon.py visitas.csv Colaboradores.txt Condominios.txt Funcionarios.txt Funcoes.txt Logo_Falcon.png requirements.txt Supervisores.txt 

# 3. Criar uma versão
git commit -m "Descreva sua alteração"

# 4. Enviar ao GitHub
git push origin main

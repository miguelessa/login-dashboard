# login-dashboard

Essa parte é a integração dos outros dois repositórios que postei. Basicamente ele joga você para a dashboard assim que você insere o usuario e senha corretos, fechando automaticamente o app do seu desktop. 

Passo a passo.

1- primeiro você deve abrir o VScode e abrir a pasta da dashboard.
2- então você abre o terminal e executa o comando 'streamlit run dashboards.py' (se você alterou o nome do arquivo, altere o nome no comando também0.
3- agora, você abre o código do login (app.py) e executa ele. (No canto superior direito tem um botão de play).
4- agora coloque o usuário que, por padrão, coloquei: usuario = usuario; senham = senha123 (podem ser alterados na linha 50 do código 'app.py'
5- assim que for efetuado o login, o seu usuário deve ser redirecionado para a página no caminho 'http://localhost:8501', fechando automaticamente o app no seu desktop.

(link para como deve ficar após todos os passos: https://streamable.com/2mfm8g).

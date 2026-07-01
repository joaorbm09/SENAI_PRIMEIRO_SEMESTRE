
<div align="center">
<h1>SERVIDOR WEB</h1>
</div>

<br>


<div align="justify">
<h2>MÉTODO GET 🤖</h2>
<img width="1919" height="1079" alt="Captura de tela 2026-03-20 091410" src="https://github.com/user-attachments/assets/9ed01f4d-519b-4d78-875e-fe5b1d5efd37" />


-- Aqui estou conectando a url do servidor que no caso é o endereço de IP, e no servidor recebo um pedido do tipo GET, ou seja estou visualizando quem  está entrando no meu servidor.

-- Ele responde com o código HTTP 200 (que significa "sucesso").

-- Ele envia de volta o texto "Servidor online". O b antes das aspas indica que você está enviando os dados em formato de bytes, que é o que o protocolo HTTP exige.
</div>


<br>


<div align="justify">
<h2>MÉTODO POST 🤖</h2>
<img width="1919" height="1079" alt="Captura de tela 2026-03-20 100506" src="https://github.com/user-attachments/assets/d416eeee-9cc9-4104-9808-1417f5fcd71e" />

--Aqui como ja estavamos conectados ao servidor, apenas mudamos de GET para POST, apartir deste momento modificamos o "Body" e o tipo de texto, para "raw" e JSON respectivamente.

--Depois de mudarmos o body e tipo de texto, vamos escrever o modo de escrita que o JSON funciona que é modo de chave para valor, para fazermos isso sempre vamos colocar ambos dentro de aspas para o servidor identificar o textos que sera enviado, a chave ficara separada do valor através do " : ". 

-- Após isso clicaremos no send para enviar a mensagem desejada para o servidor e ele ira detectar que o método do_POST foi acionado. Ele leu os bytes que vieram do Postman, depois ele executou o print. É por isso que você está vendo no seu Terminal (parte inferior do VS Code) o texto (Dados recebidos! "João Wictor" : "Aluno do Senai"...), E o servidor enviou um "joinha" de volta (Status 200 OK).
</div>

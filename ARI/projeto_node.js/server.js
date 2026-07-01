const express = require('express');
const cors = require('cors');
const app =  express();

app.use(cors());
app.use(express.json());

let historicoSensores = [
    {temperatura:30,umidade:40,hora:"09:00"},
    {temperatura:25,umidade:56,hora:"10:00"},
    {temperatura:20,umidade:30,hora:"11:00"}
];

app.get('/api/dados', (req,res) => {
    res.json(historicoSensores);
})

app.get('/api/dados/:id', (req,res) =>{
    const id = parseInt(req.params.id);

    const dadosId = historicoSensores.find(s => s.id === id);
    
    if(!dadosId){
        return res.status(404).json({mensagem:"ID não enontrado!"})
    }
    res.json(dadosId);
})


app.post('/api/dados', (req,res) =>{
    const{temperatura,umidade,hora} = req.body;    

    if (!temperatura || !umidade || !hora){
        return res.status(400).json({mensagem:"Dados incompletos! Verifique novamente!!"})
    } 

    const novosDados = {
        id: historicoSensores.length + 1,
        temperatura,
        umidade,
        hora
    }

    historicoSensores.push(novosDados);
    res.status(201).json({mensagem:"Dados enviados com sucesso!",dados:novosDados});
});

app.delete('/api/dados/:id',(req,res) => {
    const id = parseInt(req.params.id)
    const index = historicoSensores.findIndex (s => s.id === id);
    if(index === -1){
        return res.status(404).json({mensagem: "Não é possivel excluir um dado inexistente!"})
    }

    historicoSensores.splice(index,1);
    res.json({mensagem: "Dados excluídos com sucesso"})
})

app.put('/api/dados/:id', (req,res) => {
    const id = parseInt(req.params.id);
    const index = historicoSensores.findIndex (s => s.id === id);
    
    if (index === -1){
        return res.status(404).json({mensagem:"Não é possivel atualizar"})
    }

    const{temperatura,umidade,hora}=req.body;
    historicoSensores[index] = {temperatura,umidade,hora};
    
    res.json({mensagem:"dados atualizados com sucesso!"});
})

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`servidor rodando na porta ${PORT}`);
   
});


























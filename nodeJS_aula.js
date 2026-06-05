const express = require('express')
app = express()

app.get('/setcookie',(req,res)=>{
    res.cookie('Acessado em ${new Date()}');
    res.send('cookie salvo');
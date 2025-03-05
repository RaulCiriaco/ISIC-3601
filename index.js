// import express from ""express";
const express = require("express");
const cors = require("cors");
const PORT = 3000;

// declarar la instancia de express
const app = express();

// Middleware o Intermediario
app.use(express.json()); // interprete de jsom
app.use(cors()); //permite o niega el acceso a IPs

app.get("/",(req,res)=>{
    res.json(
        {
            mensaje: "Hola desde express"
        }
    );
});

app.get("/:nombre",(req,res)=>{
    // const nombre = req.params.nombre;
    const {nombre} = req.params;
    res.json({
        mensaje: "Hola usando una url personal de " +nombre
    });

});

app.get("/:n1/:n2",(req,res)=>{
    const {n1,n2} = req.params;
    if (isNaN(parseFloat(n1)) || isNaN(parseFloat(n2))) {
        res.status(400).json({message:"No todos los parametros son numero"})
    }else{
        const suma = parseInt(n1) + parseFloat(n2);
        res.json({suma});
    }
});


app.post("/",(req,res)=>{
    const{username,password} = req.body;
    res.status(201).json({username,password});

})



/*
 Existen dos tipos diferentes de funcion con flecha:
function funcion1(){
}
const funcion2 = ()=>{
}
*/

// Corriendo el servidor
app.listen(PORT, ()=>{
    console.log("Server Running in http://localhost:"+PORT)
});
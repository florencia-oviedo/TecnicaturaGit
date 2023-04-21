miFuncion(8, 2);//Esto se lo conoce como hoisting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;
}

//Llamando la función 
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una funcion de tipo expresion o anonima
let x = function(a, b){ //Necesita cierre con punto y coma
    return a + b;
};

resultado = x(5, 6);//al llamarla se pone la variable y parentesis
console.log(resultado);

//Funciones tipo self o invoking
(function(a,b){
    console.log("Ejecutando la función "+(a + b));
})(9,6);

console.log(typeof miFuncion);

function miFuncion2(a, b){
    console.log(arguments.length);
}

miFuncion2(5, 7, 3, 6);

//to string
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);

//funciones flecha
const sumarFuncionFlecha = (a , b) => a + b;
resultado = sumarFuncionFlecha(7,3); //asignamos el valor en una variable
console.log(resultado);

//Funcion de tipo expresion
let sumar  =function( a = 4, b = 8){
    console.log(arguments[0]);//muestra el parametro de a
    console.log(arguments[1]);//muestra el parametro de b
    console.log(arguments[2]);//muestra el parametro de c
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9); 
console.log(resultado);


//Sumar todos los argumentos
let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);

function sumarTodo(){
    let suma = 0;
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i]; //arguments es para arreglos   
    }
    return suma;
}

//Tipos primitivos
let k= 10;
function cambiarValor(a){
    a=20;
}
cambiarValor(k);
console.log(k);

//Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = "Ignacio";
    p1.apellido = "Perez";
}

cambiarValorObjeto(persona);
console.log(persona);
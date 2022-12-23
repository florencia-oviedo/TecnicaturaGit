// Tipos de Datos en JavaScript
/*
comentarios de multiples lineas
La sintaxis en lo que es comentarios 
es muy similar a la de Java
realmente diriamos que es identica
*/
var nombre = 'Ariel'; // Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
// Tipo numérico
var numero = 3000; 
console.log(numero);
// Tipo Object
var objeto = {
    nombre : "Ariel",
    Apellido : "Betancud",
    Telefono : "2614567893"
}
console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera);

// Tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

// Tipo de datos clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

// Tipo de dato undefined
var x ;
console.log(x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de un valor
var y = null; // null no es un tipo de dato,pero su origen es de tipo object
console.log(typeof y);

// tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z);
console.log(typeof z);
let x = 10;
console.log(x.length)
console.log("Tipos primitivos");
//objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma:'es',
    get lang(){ 
        return this.idioma.toUpperCase(); //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){//método o función
        return this.nombre + " "+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return "El nombre es: "+ this.nombre + ", Edad: "+this.edad;
    }
}
    

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando un objeto");

let persona2 = new Object(); //Debe crear un nuevo objeto en  memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "1234343523542";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona['apellido'])//Accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in");
//for in y accedemos al objeto como si fuera un arreglo
for( propiedad in persona){
    console.log(propiedad); //muestra las propiedades como nombre,apellido
    console.log(persona[propiedad]);//muestra el valor de la propiedad dada
}
console.log("Cambiamos y eliminamos un error");
persona.apellida = "Betancud";//cambiamos dinamicamente el valor del objeto
delete persona.apellida; //eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
console.log("Distintas formas de imprimir un objeto: forma 1");
//Numero 1 es la mas sencilla es concatenar cada valor de una propiedad
console.log(persona.nombre + ", "+persona.apellido)

//Numero 2 a traves de un ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for( propiedad in persona){
    console.log(persona[propiedad]);//muestra el valor de la propiedad dada
}

//Numero 3 La funcion Object.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4 Utilizaremos el  metodo JSON.stringfy()
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el método get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set de idioma');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ //constructor para definir propiedades para diferentes objetos q creamos
    this.nombre = nombre;
    this.apellido = apellido;
    this.email  = email;
    this.nombreCompleto = function(){
        return this.nombre+ " "+this.apellido;
    }
}
let padre = new Persona3('Leo','Lopez','lopez@gmail.com');
padre.nombre = 'Luis';
padre.telefono = '541866543212';
console.log(padre);
console.log(padre.nombreCompleto());

let madre = new Persona3('Laura','Contrera','contreral@gmail.com');
console.log(madre);
console.log(madre.telefono);//la propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//Caso objeto 1
let miObjeto = new Object(); //Esta opcion es formal
//Caso objeto 2
let miObjeto2 = {}; //opcion breve y recomendada

//caso String 1
let micadena = new String('Hola'); //Sintaxis formal
//caso String 2
let micadena2  = 'Hola';//esta es la sintaxis breve y recomendada

//caso numero 1
let minumero =new Number(1); //formal no recomendable
//caso numero 2
let minumero2 = 1;

//caso boolean 1
let miboolean = new Boolean(false);//formal
//caso boolean 2
let miboolean2 = true;//sintaxis recomendada

//caso arreglo 1
let miarreglo = new Array();
//caso arreglo 2
let miarreglo2 = []; //sintaxis recomendada

//caso funcion 1
let mifuncion1 = new function(){};//todo despues de new es considerado un objeto
//caso funcion 2
let mifuncion2 = function(){};//notacion simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = '1234656';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '151234656';
console.log(madre.telefono);

//uso de call
let persona4 = {
    nombre:'Juan',
    apellido:'Perez',
    nombreCompleto2 : function(titulo,telefono){
        return titulo + ': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre + ' ' + this.apellido;
    }
}
let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}
console.log(persona4.nombreCompleto2('Lic.','1456341654'));
console.log(persona4.nombreCompleto2.call(persona5,'Ing.','123546'));

//Método apply
let arreglo= ['Ing.','12643'];
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));
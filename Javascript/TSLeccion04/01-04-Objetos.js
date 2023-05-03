let x = 10;
console.log(x.length)
console.log("Tipos primitivos");
//objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function(){//método o función
        return this.nombre + " "+this.apellido;

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
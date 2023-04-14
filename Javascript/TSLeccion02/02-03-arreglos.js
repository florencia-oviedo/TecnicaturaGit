//Creación de Array o arreglos

//let autos = new Array('Ferrari','Renault','BMW'); esta es la sintaxis vieja
const autos = ['Ferrari','Renault','BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+" : "+autos[i]);
}

//Modificamos los elementos de un arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); //agregamos un elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elementos
autos[autos.length] = 'Porche';
console.log(autos);

//Tercer forma de agregar elementos CUIDADO
autos[6] = 'Renault';
console.log(autos)

//Como preguntar si es un Array o Arreglo
console.log(Array.isArray(autos)); //Devuelve un booleano

//Otra forma
console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array
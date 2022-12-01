//Ejercicio 1: Calcular la estación del año
//Ejercicio 2: Hora del día
let mes = 9;
let estacion;
if(mes == 1 || mes == 2 || mes == 12) {
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "valor incorrecto";
}
console.log("El valor corresponde a la estación de: "+ estacion);

//Ejercicio 2: Hora del día
/*
de 6 a 11 nos saluda: Good morning
de 12 a 16 nos saluda: Good afternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good Night
Trabajaremos con 24 horas
*/
let horaDia = 7;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good morning";
}
else if(horaDia>= 12 && horaDia <= 16){
    mensaje ="Good afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good night";
}
else{
    mensaje = "valor incorrecto";
}
console.log(mensaje);

// Estructura switch(la sintaxis es igual a Java)
switch(mes){// No solo se pueden utilizar numeros, también cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "valor incorrecto";

}
console.log("Bienvenido a la estación de "+ estacion);

//Ampliando el uso de var,let y const
/*
 con var puedes reasignar en cualquier momento
 este forma parte del ambito global
 Un error es que se sobreescriba
*/
var nombre = "Ariel";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
//console.log(nombre3); // Aquí no lee el dato de la función

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); // en la función funciono correctamente, en la estructura if fallo

/*
 let: este puede ser reasignada en cualquier momento
 la diferencia es que su ambito es de bloque,
 solo disponible dentro de un bloque de llaves
 o dentro de una función
*/

function saludar2(){
    let nombre2 = "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
 const se utiliza pra valores constantes que no pueden ser reasignadas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //Solo se ejecuta el console anterior

//Evitar repetir nuestro codigo
// Dry don't repeat yourself
let days = 1;
switch(days){
    case 1:
        console.log('Hoy es Lunes');
        break;
    case 2:
        console.log('Hoy es Martes');
        break;
    case 3:
        console.log('Hoy es Miercoles');
        break;
    case 4:
        console.log('Hoy es Jueves');
        break;
    case 5:
        console.log('Hoy es Viernes');
        break;
    case 6:
        console.log('Hoy es Sábado');
        break;
    case 7:
        console.log('Hoy es Domingo');
        break;
    default:
        console.log('Error en el ingreso del dia de la semana');
        break;
}

//Esta es la version mejorada
let days2 =['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado', 'Domingo'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(3));

//Hacer un ejercicio similar al que esta hecho, pero ahora con los
//meses del año, debes hacerlo con la estructura switch y luego con
//la funcion la opcion mejorada
let month= 1;
switch(month){
    case 1:
        console.log('Enero');
        break;
    case 2:
        console.log('Febrero');
        break;
    case 3:
        console.log('Marzo');
        break;
    case 4:
        console.log('Abril');
        break;
    case 5:
        console.log('Mayo');
        break;
    case 6:
        console.log('Junio');
        break;
    case 7:
        console.log('Julio');
        break;
    case 8:
        console.log('Agosto');
        break;
    case 9:
        console.log('Septiembre');
        break;
    case 10:
        console.log('Octubre');
        break;
    case 11:
        console.log('Noviembre');
        break;
    case 12:
        console.log('Diciembre');
        break;
    default:
        console.log('Error en el ingreso del mes del año');
        break;
}

//Esta es la version mejorada
let month2 =['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error('out of range');
    }
    return month2[n-1];
}
console.log(getMonth(1));
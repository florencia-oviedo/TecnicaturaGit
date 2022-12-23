// Ejercio para encontrar números pares e impares
let parImpar = 10;
if( parImpar % 2 == 0){
    console.log("Es un número par");
}
else{
    console.log("Es un número impar");
}

//Es mayor de edad
let edad = 14, adulto = 18;
if(edad >= adulto){
    console.log("Usted es una persona adulta");
}
else{
    console.log("Usted es una persona de menor de edad");
}

//Ejercicio: dentro de un rango
let dentroRango = 10; //Aquí vamos a ir cambiando el valor
let valMin = 0 , valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log("Está dentro del rango establecido");
}
else{
    console.log("Esta fuera del rango establecido");
}

// Ejercicio : Si el padre puede asistir al juego de su hijo

let vacaciones = true, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo");
}
else{
    console.log("El padre no puede asistir al juego de su hijo");
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero":"Falso";
console.log(resultado2);
// ejercicio par o impar con operador ternario
let numero = 12;
resultado2 = numero%2 == 0 ? "Es un número PAR":"Es un número IMPAR";
console.log(resultado2);

//Convertir String a Number
let miNumero = "21"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero);
console.log(typeof edad2);
//Función isNaN
if(isNaN(edad2)){ //No es un número: is Not a Number (devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numero");
}
else{
    if(edad2>=18){
        console.log("Puede votar");
    }
    else{
        console.log("Muy joven para votar");
    }
}
//Operador ternario
let resultado3 = edad2 >=18 ? "Puede votar":"Muy joven para votar";
console.log(resultado3);




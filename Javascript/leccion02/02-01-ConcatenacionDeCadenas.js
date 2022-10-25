var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido; // Primera Concatenación
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Betancud'; // Segunda Concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izq a derecha siguiendo la cadena lee el num como str
console.log(juntos);
juntos = nombre + 78 + 17; // Aquí se puede diferenciar a tráves de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera Concatenación usando el operador simplificado
console.log(nombre);
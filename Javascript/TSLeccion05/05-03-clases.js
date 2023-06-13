//Sintaxis basica para definir una clase
//let persona3 = new Persona('Carla','Ponce'); esto no se puede hacer Persona is not defined
class Persona{
    constructor(nombre,apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre(){
        return this._nombre
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){ //funcion no es necesario el function
        return this._nombre+' '+this._apellido;
    }
    toString(){//regresa un string, sobreescribiendo el metodo de la clase padre Object
        //se aplica el polimorfismo que significa =  multiples formas de ejecucion
        //El metodo que se ejecuta depende de la referencia de tipo padre o tipo hija
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{//Clase Hija
    constructor(nombre,apellido,departamento){
        super(nombre,apellido);
        this._departamento = departamento;

    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura
    nombreCompleto(){ 
        return super.nombreCompleto() + ', '+this._departamento;
    }

}



let persona1 = new Persona('Martín','Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);
console.log(persona1.apellido);
persona1.apellido = 'Roldan';
console.log(persona1.apellido);


let persona2 = new Persona('Carlos','Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//console.log(persona2);
console.log(persona2.apellido);
persona2.apellido = 'Larrea';
console.log(persona2.apellido);

let empleado1  = new Empleado('Maria','Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

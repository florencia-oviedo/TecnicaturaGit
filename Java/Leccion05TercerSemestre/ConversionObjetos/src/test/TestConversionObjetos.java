
package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan",35000,TipoEscritura.CLASICO);
        System.out.println("empleado = " + empleado);
        System.out.println(empleado.obtenerDetalles());//Si queremos acceder a metodos Escritor
        //empleado.getTipoEscritura(); da error porque esta solo en la clase escritura! y no puede acceder desde empleado
        //Downcasting
        //((Escritor)empleado).getTipoEscritura();//tenemos dos opciones esta es una
        Escritor escritor = (Escritor)empleado;//segunda opcion
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
        
    }
}


package test;

import domain.*;


public class TestSobreescritura {
    public static void main(String[] args) {
        
        Empleado empleado = new Empleado("Juan",10000);
        //System.out.println("empleado = " + empleado.obtenerDetalles());
        
        empleado = new Gerente("José",5000,"Sistemas");
        //System.out.println("gerente = " + gerente.obtenerDetalles());
        imprimir(empleado);
        //imprimir(gerente);
        
        
    }
    public static void imprimir(Empleado empleado){
        String detalles = empleado.obtenerDetalles();
        System.out.println("detalles = " + detalles);
    }
}

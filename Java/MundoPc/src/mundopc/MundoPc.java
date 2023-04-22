
package mundopc;

import ar.com.system2023.mundopc.*; //importamos las clases con el package 


public class MundoPc {
    public static void main(String[] args) {
        //Creamos objetos 
        Monitor monitorHP = new Monitor("HP",13);
        Teclado tecladoHP = new Teclado("Bluetooth","HP");
        Raton ratonHP = new Raton("Bluetooth","HP");
        Computadora computadoraHP = new Computadora("Computadora HP",monitorHP,tecladoHP,ratonHP);
        
        //Creamos otros objetos
        Monitor monitorGamer = new Monitor("Gamer",32);
        Teclado tecladoGamer = new Teclado("Bluetooth","Gamer");
        Raton ratonGamer = new Raton("Bluetooth","Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer",monitorGamer,tecladoGamer,ratonGamer);
        Computadora computadoraVarias = new Computadora("Computadora de diferentes marcas", monitorHP,tecladoGamer, ratonHP);
        Orden orden1 = new Orden(); //inicializamos el arreglo vacio con la creacion del objeto
        Orden orden2 = new Orden(); //Nueva lista
        
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        orden1.mostrarOrden();
        
        orden2.agregarComputadora(computadoraVarias);
        orden2.mostrarOrden();
        
        //Tarea crear mas objetos de tipo computadora
        //llegar a mas de 10 elementos en la orden 1
        Monitor monitorSamsung = new Monitor("Samsung",20);
        Teclado tecladoSamsung = new Teclado("Bluetooth","Samsung");
        Raton ratonSamsung = new Raton("Bluetooth","Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung",monitorSamsung,tecladoSamsung,ratonSamsung);
        
        Monitor monitorDell = new Monitor("Dell",25);
        Teclado tecladoDell = new Teclado("Bluetooth","Dell");
        Raton ratonDell = new Raton("Bluetooth","Dell");
        Computadora computadoraDell = new Computadora("Computadora Dell",monitorDell,tecladoDell,ratonDell);
        
        
        
        
        orden1.agregarComputadora(computadoraSamsung);
        orden1.agregarComputadora(computadoraDell);
        orden1.mostrarOrden();
        
        
        
    }
}

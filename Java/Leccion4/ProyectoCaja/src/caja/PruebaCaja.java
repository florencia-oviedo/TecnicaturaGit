/* Proyecto Caja:
  Ejercicio 1: Crear un proyecto según las especificaciones 
  mostradas a continuación.
  La formula es: volumen = ancho * alto * profundidad
*/
package caja;

public class PruebaCaja {
    public static void main(String[] args) { // Método main
        //Variables locales
        int medidaAncho  = 3; // Valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacío
        caja1.alto = medidaAlto;
        caja1.ancho = medidaAncho;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al método
        //Primer resultado
        System.out.println("El resultado del volumen de la caja 1 es: " + resultado);
        
        Caja caja2 = new Caja(2,4,6); // Llamamos al constructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al método para un nuevo cálculo
        System.out.println("El resultado del volumen de la caja 2 es: " + caja2.calcularVolumen());
    }
}

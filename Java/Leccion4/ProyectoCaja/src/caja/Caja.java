/* Proyecto Caja:
  Ejercicio 1: Crear un proyecto según las especificaciones 
  mostradas a continuación.
  La formula es: volumen = ancho * alto * profundidad
*/
package caja; //package

public class Caja { //clase publica caja
    // Atributos de la clase (características)
    int ancho;
    int alto;
    int profundo;
    // Métodos y constructores (acciones)
    public Caja(){ //constructor 1= vacío   
    }
    // Constructor con parámetros
    public Caja(int ancho,int alto, int profundo){ 
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    //Método para calcular el volumen
    public int calcularVolumen(){
        return ancho * alto * profundo;
    }
    
}

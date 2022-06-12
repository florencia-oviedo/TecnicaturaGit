
package ejercicio_5;

import java.util.Scanner;

public class Ejercicio_5 {
  
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        
        // Codigo hecho por mi
        /*System.out.println("Ingrese la calificacion 1: ");
        float calificacion1 = Float.parseFloat(entrada.nextLine());
        System.out.println("Ingrese la calificacion 2: ");
        float calificacion2 = Float.parseFloat(entrada.nextLine());
        System.out.println("Ingrese la calificacion 3: ");
        float calificacion3 = Float.parseFloat(entrada.nextLine());
        
        float sumaCalif= calificacion1 + calificacion2 + calificacion3 ;
        
        System.out.println("La suma de las 3 calificaciones es = " + sumaCalif);*/
        
        //Codigo hecho por el profe 
        float nota1,nota2,nota3,suma ;
        System.out.println("Digite las 3 calificaciones: ");
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());
        suma= nota1 + nota2 + nota3;
        System.out.println("\nLa suma es = " + suma);
    }
    
}

/*
 * Ejercicio 12: Pedir un número y calcular su factorial
   Hacerlo con las dos clases, Scanner y JOptionPane
 */
package ciclos12;

import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        Scanner  entrada = new Scanner(System.in);
       int numero;
       long factorial;
       factorial = 1;
       System.out.println("Digite un número para calcular su factorial: ");
       numero = Integer.parseInt(entrada.nextLine());
       for(int i =1; i<= numero;i++){
           factorial *= i;
       }
        System.out.println("El factorial de "+ numero + " es: "+ factorial);
    
    } 
}

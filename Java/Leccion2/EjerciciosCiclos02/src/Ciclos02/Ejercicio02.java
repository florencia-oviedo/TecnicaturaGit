/* Ejercicio 2: leer un número e indicar si es positivo o  negativo
El proceso se repetirá hasta que se introduzca un 0
con clase Scanner
*/
package Ciclos02;

import java.util.Scanner;

public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero > 0){
                System.out.println( numero + " es un número positivo");
            }
            else{
                System.out.println( numero + " es un número negativo");
            }
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa ha finalizado por ingresar 0");
    }
}


/*
 Ejercicio 8: Pedir un número N , y mostrar todos los números 
 del 1 al N
*/
package Ciclos08;

import java.util.Scanner;

public class Ciclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextLine());
        // mi forma
        //for(var i = 1; i<=numero;i++){
            //System.out.println(i);
        int i = 1;
        while(i<=numero){
            System.out.println(i);
            i++;   
        }
    }
}

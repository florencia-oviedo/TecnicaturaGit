/*
 Ejercicio 5: Realizar un juego para adivinar un número,
 para ello generar un número aleatorio del 0-100 y luego ir
 pidiendo números indicando si "es mayor" o "es menor" según
 sea mayor o menor a con respecto a N
 El proceso termina cuando el usuario acierta y mostramos el 
 números de intentos hechos.
 */
package Ciclos05;

import java.util.Scanner;


public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,aleatorio,conteo=0;
        aleatorio = (int)(Math.random()*100); //genera un numero aleatorio de 0 a 100
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un número mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un número menor");
            }
            else{
                System.out.println("¡¡Felicidades!!! Haz adivinado el número!!!");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el número en "+conteo+" intentos");
    }
}

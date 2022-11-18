/*
Asistencia Noviembre
Alumna: Florencia Micaela Oviedo
Grupo: CodeStyle
    Ejercicio 1: Leer 5 números, guardarlos en un arreglo y
    mostrarlos en el mismo orden introducidos.
 */
package arreglos_ejercicio_1;

import java.util.Scanner;


public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        
        System.out.println("Guardando los datos en el arreglo");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println((i+1)+". Digite un número: ");
            numeros[i] = entrada.nextFloat();
        }
        System.out.println("\nImprimir los elementos del arreglo");
        
        for (float i:numeros){
            System.out.print(i+" ");
        }
        System.out.println("\n");
        
        
        
    }
    
}

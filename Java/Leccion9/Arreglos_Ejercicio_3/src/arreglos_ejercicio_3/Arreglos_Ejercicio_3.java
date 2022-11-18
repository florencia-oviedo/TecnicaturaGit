/*
  Ejercicio 3: Leer 5 números por teclado, almacenarlos en
  un arreglo y a continuación realizar la media de los 
  numeros positivos, la media de los negativos y contar el
  número de ceros.
 */
package arreglos_ejercicio_3;

import java.util.Scanner;

public class Arreglos_Ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int contadorPos = 0, contadorNeg = 0, contadorCeros = 0;
        float numeros[] = new float[5];
        float mediaPos, mediaNeg, sumaPos = 0, sumaNeg = 0;

        System.out.println("Guardando los datos en el arreglo");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println((i + 1) + " .Digite un número: ");
            numeros[i] = entrada.nextFloat();
            if (numeros[i] > 0) {
                sumaPos += numeros[i];
                contadorPos++;
            } else if (numeros[i] < 0) {
                sumaNeg += numeros[i];
                contadorNeg++;
            } else {
                contadorCeros++;
            }
        }
        //Positivos
        if (contadorPos == 0) {
            System.out.println("\nNo se puede calcular la media de los números positivos");
        } else {
            mediaPos = sumaPos / contadorPos;
            System.out.println("\nLa media de los n° positivos es: " + mediaPos);
        }

        //Negativos
        if (contadorNeg == 0) {
            System.out.println("\nNo se puede calcular la media de los números negativos");
        } else {
            mediaNeg = sumaNeg / contadorNeg;
            System.out.println("La media de los n° negativos es: " + mediaNeg);
        }

        System.out.println("La cantidad de n° ceros es: " + contadorCeros);

    }
}

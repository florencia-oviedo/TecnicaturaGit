/*
  Ejercicio 7: Pedir números hasta que se introduzca uno negativo
  y calcular el promedio
 */
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
    public static void main(String[] args) {
        int numero,conteo = 0,suma = 0;
        float promedio = 0 ;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){ //Mientras el numero no sea negativo
            suma += numero;
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null, "\n Error, la división entre 0 no existe");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "\n El promedio es: "+ promedio);
        }
    }
}

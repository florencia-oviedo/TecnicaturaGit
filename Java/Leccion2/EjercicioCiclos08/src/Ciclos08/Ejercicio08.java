/*
  Ejercicio 8: Pedir un número N , y mostrar todos los números 
 del 1 al N
 */
package Ciclos08;

import javax.swing.JOptionPane;


public class Ejercicio08 {
    public static void main(String[] args) {
       
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        // mi forma
        //int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        //for(var i = 1; i<=numero;i++){
            //JOptionPane.showMessageDialog(null, i);
        int i = 1;
        while(i<=numero){
            JOptionPane.showMessageDialog(null, i);
            i++;   
    }
  }
}

/* Ejercicio 2: leer un número e indicar si es positivo o  negativo
El proceso se repetirá hasta que se introduzca un 0
con clase JOptionPane
*/
package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El número es positivo");
            }
            else {
                JOptionPane.showMessageDialog(null, "El número es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa");
        
        }
        
    }


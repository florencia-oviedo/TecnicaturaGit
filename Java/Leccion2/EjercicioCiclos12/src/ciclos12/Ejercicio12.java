/*
 * Ejercicio 12: Pedir un número y calcular su factorial
   Hacerlo con las dos clases, Scanner y JOptionPane
 */
package ciclos12;

import javax.swing.JOptionPane;

public class Ejercicio12 {
    public static void main(String[] args) {
        int numero;
        long factorial;
       factorial = 1;
       
       numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
       for(int i =1; i<= numero;i++){
           factorial *= i;
       }
        JOptionPane.showMessageDialog(null,"El factorial de "+ numero + " es: "+ factorial);
    }
}

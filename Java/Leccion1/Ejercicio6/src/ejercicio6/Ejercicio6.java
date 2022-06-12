package ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        //Hecho por mi
        /*System.out.println("Digite la cantidad de dolares de guillermo: ");
        float guille = Float.parseFloat(entrada.nextLine());
        float juan, luis, total;
        luis = guille / 2;
        juan = (guille + luis) / 2;
        total = guille + luis + juan;
        System.out.println("guille = " + guille);
        System.out.println("luis = " + luis);
        System.out.println("juan = " + juan);
        System.out.println("total de los 3 es = " + total);*/
        
        //Hecho por el profe
        float guillermo, luis, juan, total;
        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        luis= guillermo/2;
        juan= (luis + guillermo)/2;
        total= luis + guillermo + juan ;
        System.out.println("\n El dinero de luis es : US$" + luis);
        System.out.println("El dinero de Juan es: US$" + juan);
        System.out.println("El total de dinero entre los tres es: US$" + total);
                

    }

}

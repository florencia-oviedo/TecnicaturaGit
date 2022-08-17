package clase11;

import java.util.Scanner;

public class clase11 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        //Determinar si un alumno aprueba o reprueba un curso, sabiendo que
        //aprobara si su promedio de tres calificaciones es mayor o igual a 70
        // reprueba caso contrario
        /*System.out.println("Digite la nota 1:");
        var nota1 = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite la nota 2: ");
        var nota2 = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite la nota 3: ");
        var nota3 = Float.parseFloat(entrada.nextLine());

        var promedio = (nota1 + nota2 + nota3) / 3;
        
        if (promedio >= 70) {
            System.out.println("Aprueba el curso");
        }
        else {
            System.out.println("Reprueba el curso");
        }*/
        
        
        
        // En un almacen se hace un 20% de descuento a los clientes
        // Cuya compra supere los $100 ¿Cual sera la cantidad que
        // pagará una persona por su compra?
        
       /* System.out.println("Digite el valor de su compra: ");
        var compra = Float.parseFloat(entrada.nextLine());
        double valorFinal, descuento;
        if (compra > 100){
            descuento= compra*0.20;
            valorFinal = compra - descuento;
        }
        else {
            valorFinal= compra;
        }
        
        System.out.println("La cantidad de pesos a pagar es: $" +  valorFinal);*/
       
       //Leer dos numeros, si son iguales que los multiplique, si el
       //primero es mayor que el segundo que los reste y si no que los sume
       
        System.out.println("Digite un numero: ");
        var num1 = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Digite otro numero: ");
        var num2 = Integer.parseInt(entrada.nextLine());
        int resultado;
        if (num1 == num2) {
            resultado= num1*num2;
        }
        else if (num1 > num2){
            resultado = num1 - num2;
        }
        else {
            resultado= num1 + num2;
        }
        System.out.println("El resultado es = " + resultado);

    }
}

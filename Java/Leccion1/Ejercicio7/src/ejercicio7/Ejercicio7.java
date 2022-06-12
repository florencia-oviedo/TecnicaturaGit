package ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Hecho por mi
       /*final int salario = 1000 ;
        System.out.println("Digite la cantidad de carros vendidos: ");
        int carros = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el valor del carro: ");
        float precioCarro = Float.parseFloat(entrada.nextLine());
        var salarioTotal= salario + carros*150 + precioCarro*carros*0.05 ;
        
        System.out.println("El salario total es : $" + salarioTotal);*/
       
       //Hecho por el profe
       final int salario = 1000;
       int comision= 150 , venta;
       float salarioMensual, ventaCarro,porcVenta, totalPrecio;
       System.out.println("Digite la cantidad de carros vendidos: ");
       venta= Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio de un carro: ");
        ventaCarro= Float.parseFloat(entrada.nextLine());
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;
        System.out.println("\nEl salario mensual es :" + salarioMensual);
        
        
        
    }

}


package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;


public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Día 1: " + Dias.LUNES);
        //indicarDiaSemana(Dias.MARTES); //Las enumeraciones se tratan como cadenas
        //Ahora no se deben utilizar comillas, se accede a traves del operador de punto
        System.out.println("");
        System.out.println("Continente n°4: " + Continentes.AMERICA);
        System.out.println("N° de paises en el 4to Continente: " + Continentes.AMERICA.getPaises());
        System.out.println("N° de habitantes en el 4to Continente: " + Continentes.AMERICA.getHabitantes());
    }
    
    private static void indicarDiaSemana(Dias dias){
        
        switch(dias){
            case LUNES:
                System.out.println("Primer día de la semana");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana");
                break;
            case DOMINGO:
                System.out.println("Séptimo día de la semana");
                break;
        }
    }
}

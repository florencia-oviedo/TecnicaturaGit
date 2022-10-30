
package test;

import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57000,false);
        System.out.println("persona1: " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificar a tráves de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //ya no se puede utilizar
        //System.out.println("nombre = " + persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        // Tarea Crear otro Objeto de tipo Persona, asignar valores iniciales
       // y imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("persona1: " + persona1);
       Persona persona2 = new Persona("Florencia",60000,true);
        System.out.println("persona2 nombre: " + persona2.getNombre());
        System.out.println("persona2 sueldo: " + persona2.getSueldo());
        System.out.println("persona2 booleano: " + persona2.isEliminado());
        persona2.setNombre("Giselle");
        persona2.setSueldo(80000);
        persona2.setEliminado(false);
        System.out.println("persona2 nombre modificado: " + persona2.getNombre());
        System.out.println("persona2 sueldo modificado: " + persona2.getSueldo());
        System.out.println("persona2 booleano modificado: " + persona2.isEliminado());
    }
}

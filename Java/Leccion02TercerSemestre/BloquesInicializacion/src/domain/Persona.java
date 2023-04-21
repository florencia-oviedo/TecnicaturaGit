
package domain;


public class Persona {
    
    private final int idPersona;
    private static int contadorPersonas;
    
    static{//Bloque de inicialización estatico
        System.out.println("Ejecución bloque estatico");
        ++Persona.contadorPersonas;
        //idPersona= 10; No es un atributo estatico por esto tenemos un error
    }
  
    //Bloque de inicializacion no estatico(contexto dinamico)
    {
        System.out.println("Ejecución del bloque no estatico");
        this.idPersona = Persona.contadorPersonas++;//incrementamos el atributo
    }
    //Los bloques de inicializacion se ejecutan antes del constructor
    
    public Persona(){
        System.out.println("Ejecución del constructor");
    }
    
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
}

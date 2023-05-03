
package paquete1;

public class Clase1 {
    
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor Atributo Protected";
    
    protected Clase1(String atributo){
        System.out.println("Constructor protected");
        
    }
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    
    
    public void metodoPublic(){
        System.out.println("Metodo publico");
    }
    
    protected void metodoProtected(){
        System.out.println("Método protected");
    }
    
}

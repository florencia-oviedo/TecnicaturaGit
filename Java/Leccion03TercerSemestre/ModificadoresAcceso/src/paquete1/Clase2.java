
package paquete1;

class Clase2 {
    
    String atributoDefault = "Valor del atributo Default";
    
    Clase2(){
        System.out.println("Constructor default");
    }
    /*
    public Clase2(){
        super();
        this.atributoDefault = "Modificación del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }*/
    
    void metodoDefault(){
        System.out.println("Método Default");
    }
}

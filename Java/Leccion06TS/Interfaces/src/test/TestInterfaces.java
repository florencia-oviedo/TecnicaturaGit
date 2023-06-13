
package test;

import accesodatos.*;

public class TestInterfaces {
    public static void main(String[] args) {
        //definimos un tipo interface
        //no podemos instanciar una interface
        IAccesoDatos datos = new ImplementacionMysql();
        //datos.listar();
        imprimir(datos);
        datos = new ImplementacionOracle();
        //datos.listar();
        imprimir(datos);
    }
    public static void imprimir(IAccesoDatos datos){//metodo generico
        datos.listar();
    }
}


package test;

import domain.*;

public class TestAbstractas {
    public static void main(String[] args) {
        //las clases abstractas no se pueden instanciar por eso usamos la clase Rectangulo
        FiguraGeometrica figura = new Rectangulo("Rectangulo");//upcasting
        figura.dibujar();
    }
}

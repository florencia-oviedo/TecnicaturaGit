
package domain;


public class Rectangulo extends FiguraGeometrica {
    //constructor
    public Rectangulo(String tipoFigura) {
        super(tipoFigura);
    }

    @Override
    public void dibujar() { //implementando el metodo de la clase abstracta
        System.out.println("Se imprime un: "+ this.getClass().getSimpleName());
    }
    
}

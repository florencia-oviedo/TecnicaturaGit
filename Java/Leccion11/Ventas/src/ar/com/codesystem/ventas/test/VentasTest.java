
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;


public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalón",9500.00);
        Producto producto2 = new Producto("Vestido",35000.00);
        Producto producto3 = new Producto("Medias",500.00);
        Producto producto4 = new Producto("Remera",1500.00);
        Producto producto5 = new Producto("Jean",15000.00);
        Producto producto6 = new Producto("Buzo",17000.00);
        Producto producto7 = new Producto("Zapatillas",45000.00);
        Producto producto8 = new Producto("Short",11200.00);
        Producto producto9 = new Producto("Blusa",13000.00);
        Producto producto10 = new Producto("Gorro",2000.00);
        Producto producto11 = new Producto("Pollera",12000.00);
        Producto producto12 = new Producto("Camiseta",2500.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto1);
        orden2.agregarProducto(producto2);
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto4);
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);
        
        orden3.mostrarOrden();
        
        
        //Tarea:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2 más
    }
}

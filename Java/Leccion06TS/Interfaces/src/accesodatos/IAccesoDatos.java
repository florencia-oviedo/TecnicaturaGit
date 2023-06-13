
package accesodatos;


public interface IAccesoDatos {
    //interface : para indicar un comportamiento. No hereda de Object
    //Puede heredar de interfaces
    //solo constantes y metodos abstractos
    //estatic final son pero no es necesario aclararlo
    //necesita si o si una asignacion porque no tiene constructores
    int MAX_REGISTROS=10;
    
    //metodo insertar abstracto y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
    
}

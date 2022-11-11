
package domain;


public class Empleado extends Persona {
    private int IdEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //Es para incrementar
    //Constructores
    public Empleado(){ //constructor 1
        this.IdEmpleado = ++ Empleado.contadorEmpleados;
    }
    public Empleado(String nombre, double sueldo) { //constructor 2
        //super(nombre);
        this(); // Estamos llamando desde aquí al constructor vacío(llamar a un constructor interno)
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.IdEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{IdEmpleado=").append(IdEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
}

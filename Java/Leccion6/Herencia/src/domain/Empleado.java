
package domain;


public class Empleado extends Persona {
    private int IdEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //Es para incrementar

    public Empleado(String nombre, double sueldo) {
        super(nombre);
        this.IdEmpleado = ++ Empleado.contadorEmpleados;
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

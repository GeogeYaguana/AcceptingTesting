Scenario: Editar una tarea existente
  Given la lista de tareas contiene:
    | Título            | Descripción                  | Fecha       | Estado   |
    | Comprar víveres   | Comprar leche, pan y huevos  | 2024-05-01  | Pending  |
  When el usuario edita la tarea "Comprar víveres" cambiando la descripción a "Comprar leche, pan, huevos y queso"
  Then la tarea "Comprar víveres" debe tener la descripción "Comprar leche, pan, huevos y queso"


Scenario: Eliminar una tarea individual
  Given la lista de tareas contiene:
    | Título          | Descripción             | Fecha       | Estado   |
    | Pagar facturas  | Pagar las cuentas       | 2024-05-03  | Pending  |
  When el usuario elimina la tarea "Pagar facturas"
  Then la lista de tareas no debe contener "Pagar facturas"

function imprimir(){
    ventana_imprimir = window.open('#','','width=740,height=480,menubar=no,scrollbars=yes,toolbar=no,location=no,directories=no,resizable=no,top=0,left=0');
    ventana_imprimir.document.write("<style>body{font-size:10px;}</style>");
    ventana_imprimir.document.write("<br><br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_codigo_alumno").val()+"</p>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_alumno").val()+"</p>");
    ventana_imprimir.document.write("<br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_carrera").val()+"&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_turno").val()+"</p>");
    ventana_imprimir.document.write("<br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_ciclo_seccion").val()+"&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_contro_pago").val()+"</p>");
    ventana_imprimir.document.write("<br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_concepto").val()+"</p>");
    ventana_imprimir.document.write("<br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_fecha_emision").val()+"</p>");
    ventana_imprimir.document.write("<br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_monto").val()+"</p>");
    ventana_imprimir.document.write("<br>");
    ventana_imprimir.document.write("<p>&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+$("#id_saldo").val()+"</p>");
    ventana_imprimir.print();
}
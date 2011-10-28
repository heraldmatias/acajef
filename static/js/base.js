var academicomenu=null;
var pagomenu=null;
var divmenu=null;

function run(){
    divmenu = $("#col3_content");
    menu();
}

function getPagoMenu(){
	if(pagomenu==null)
		pagomenu = $.ajax({
			url: "/wvb/pago",
			dataType: "html",
			async: false
			}).responseText;
	divmenu.html(pagomenu);
	menu();
}

function menu(){
	$('#hierarchybreadcrumb').menu({
		content: $('#hierarchybreadcrumb').next().html(),
		backLink: false
	});
}

function getAcademicoMenu(){
	if(academicomenu==null)
		academicomenu = $.ajax({
			url: "/wvb/academico",
			dataType: "html",
			async: false
			}).responseText;
	divmenu.html(academicomenu);
   	menu();
}

function confirmar(mensaje){
	if (confirm(mensaje))
		return true;
	return false;
}

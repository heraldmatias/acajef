var academicofdMenu=null;
var pagofdMenu=null;
var divfdMenu=null;

function run(){
    divfdMenu = $("#col3_content");
    fdMenu();
}

function getPagofdMenu(){
	if(pagofdMenu==null)
		pagofdMenu = $.ajax({
			url: "/wvb/pago",
			dataType: "html",
			async: false
			}).responseText;
	divfdMenu.html(pagofdMenu);
	fdMenu();
}

function fdMenu(){
	$('#hierarchybreadcrumb').fdmenu({
		content: $('#hierarchybreadcrumb').next().html(),
		backLink: false
	});
}

function getAcademicofdMenu(){
	if(academicofdMenu==null)
		academicofdMenu = $.ajax({
			url: "/wvb/academico",
			dataType: "html",
			async: false
			}).responseText;
	divfdMenu.html(academicofdMenu);
   	fdMenu();
}

function confirmar(mensaje){
	if (confirm(mensaje))
		return true;
	return false;
}

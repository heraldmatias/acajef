var academicomenu=null;
var pagomenu=null;
var carrera=null;
var divcont=null;
var divform=null;
var divbienvenida=null;

function run(){
	divcont=$("#col3_content");
    divbienvenida=$("#col1_content");
    divform=$("#col1");
	$('#hierarchybreadcrumb').menu({
		content: $('#hierarchybreadcrumb').next().html(),
		backLink: false
	});
}

function getPagoMenu(){
	if(pagomenu==null)
		pagomenu = $.ajax({
			url: "/wvb/pago",
			dataType: "html",
			async: false
			}).responseText;
	divcont.html(pagomenu);
	menuacademico();
}

function menuacademico(){
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
	divcont.html(academicomenu);
   	menuacademico();
}

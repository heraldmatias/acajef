var pagomenu=null,academicomenu=null;

function runMenu(){
	$('#hierarchybreadcrumb').menu({
		content: $('#hierarchybreadcrumb').next().html(),
		backLink: false
	});
}

function getPagoMenu(){
	if(pagomenu==null)
		pagomenu = $.ajax({
			url: "/wvb/include/menupago",
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
			url: "/wvb/include/menuacademico",
			dataType: "html",
			async: false
			}).responseText;
	divcont.html(academicomenu);
   	menuacademico();
}

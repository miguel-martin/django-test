function confirmar(msg="¿Estás seguro?", goto){
	if (confirm(msg)){
		window.location.href = goto;
	}
}

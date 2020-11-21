function register() {
	postData("/register", {
		uname: $("#uname").val(),
		pw1: $("#pw1").val(),
		pw0: $("#pw0").val(),
		
	}).then(data => {
		$("#message").text(data["status"]);
	}

	);
}
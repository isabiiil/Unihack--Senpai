function register() {
	postData("/register", {
		uname: $("#uname").val(),
		pw1: $("#pw1").val(),
		pw0: $("#pw0").val(),
	}

	).then(data => {
		if (data["status"] === "Password's must match") {
			console.log("PASSWRODS BAD")
		}
		else {
			console.log("users have been registered :))")
		}
	}

	);
}
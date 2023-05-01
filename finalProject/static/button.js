var button_on = $("#activate_button");
var button_off = $("#deactivate_button");

button_on.click(function() {
	console.log(button_on.text());
	$.ajax({
	url: "/activate",
	type: "post",
	success: function(response) {
		console.log(response);
		}
		});
});

button_off.click(function() {
	console.log(button_off.text());
	//if (button_off.text() === "Deactivate Camera") {
	$.ajax({
	url: "/deactivate",
	type: "post",
	success: function(response) {
		console.log(response);
		//button_off.text("Activate Camera");
		}
		});
	//} else {
		//$.ajax({
			//url: "/activate",
			//type: "post",
			//success: function() {
				//button_off.text("Deactivate Camera");
			//}
		//})
	//}
});

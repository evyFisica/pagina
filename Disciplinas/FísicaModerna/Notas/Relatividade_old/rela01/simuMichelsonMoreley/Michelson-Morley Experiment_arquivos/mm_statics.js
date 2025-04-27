// Author: Lawrence Hook
window.addEventListener("load", function () {
	var windowHeight = $(window).height(),
		windowWidth = $(window).width(),
		sizeConstraint = Math.min(windowHeight, windowWidth) * 0.93,
		canvasDim = sizeConstraint / 1.2,
		midx = canvasDim / 2,
		midy = canvasDim / 2,
		canvasRadius = (canvasDim / 2) - 2,
		mirrorLength = sizeConstraint / 7.5,
		mirrorWidth = sizeConstraint / 75,
		canvas = $('#static_canvas').get(0),
		context = canvas.getContext('2d'),
		platform = new Circle(canvasRadius, "black"),
		translucentMirror = new Rectangle(midx, midy, mirrorWidth, mirrorLength, Math.PI / 4),
		rightMirror = new Rectangle(canvasDim - mirrorWidth, midy, mirrorWidth, mirrorLength / 2, 0),
		topMirror = new Rectangle(midx, mirrorWidth, mirrorWidth, mirrorLength / 2, Math.PI / 2),
		bottomMirror = new Rectangle(midx, canvasDim - mirrorWidth, mirrorWidth, mirrorLength, Math.PI / 2);

	rightMirror.fillcolor = utils.parseColor("#6dc4c3");
	topMirror.fillcolor = utils.parseColor("#6dc4c3");
	bottomMirror.fillcolor = utils.parseColor("#535353");

	// Resize the canvas(es) and place buttons below them
	canvas.width = canvasDim;
	canvas.height = canvasDim;
	$("#buttondiv").get(0).style.top = canvasDim + "px";
	$("#sliderdiv").get(0).style.top = canvasDim + "px";
	$("#explanation").css("top", canvasDim + "px");

	// Add a background gradient
	var gradient = context.createRadialGradient(midx, midy, canvasRadius, midx, midy, 0);
	gradient.addColorStop(0,"gray");
	gradient.addColorStop(1,"white");
	context.beginPath();
	context.arc(midx, midy, canvasRadius, 2 * Math.PI, false);
	context.fillStyle = gradient;
	context.fill();

	// Place objects in their respective positions
	platform.x = midx;
	platform.y = midy;
	platform.lineWidth = 2;

	// Draw mirrors and platform
	translucentMirror.draw(context);
	rightMirror.draw(context);
	topMirror.draw(context);
	bottomMirror.draw(context);
	platform.draw(context);

});
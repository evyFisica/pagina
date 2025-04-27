// Author: Lawrence Hook
window.addEventListener("load", function () {
	var windowHeight = $(window).height(),
		windowWidth = $(window).width(),
		sizeConstraint = Math.min(windowHeight, windowWidth) * 0.93,
		mirrorLength = sizeConstraint / 50,
		mirrorWidth = sizeConstraint / 75,
		LIGHT_SPEED = mirrorWidth / 5.5,
		canvas = $('#canvas').get(0),
		context = canvas.getContext('2d'),
		lightRadius = sizeConstraint / 200,
		arrowRadius = sizeConstraint / 300,
		light1 = new Light(lightRadius, "yellow"),
		light2 = new Light(lightRadius, "red"),
		playBool = true,
		canvasDim = sizeConstraint / 1.2,
		pastMid1 = false,
		pastMid2 = false,
		luminiferousAetherSpeed = 0,
		platformAngle = 0,
		pStartAngle = 0,
		mouseStartAngle = 0,
		touchStartAngle = 0,
		isClicked = false,
		isTouched = false,
		hasStarted = false,
		aaCount = 8,
		aetherArrows = new Array(aaCount * aaCount);

	// Initialize misc variables
	var dx, dy, i = 0;
	
	// Initialize aether arrows
	var aetherInterval = canvasDim / (aaCount - 1);
	for (i = 0; i < aaCount * aaCount; i++) {
		aetherArrows[i] = new Arrow(arrowRadius, "#fef59d");
		aetherArrows[i].rotation = Math.PI;
		aetherArrows[i].x = aetherInterval * (i % aaCount);
		aetherArrows[i].y = aetherInterval * Math.floor(i / aaCount);
	}

	// Resize the canvas
	canvas.width = canvasDim;
	canvas.height = canvasDim;

	// Place all objects in their starting positions
	var midx = canvasDim / 2,
		midy = canvasDim / 2;

	light1.x = lightRadius * 3;
	light1.y = midy;
	light1.rotation = 3 * Math.PI / 2;
	
	light1.vx = 0;
	light1.vy = 0;

	light2.x = midx;
	light2.y = midy;
	light2.rotation = Math.PI;

	// Create slider
	$("#slider").uislider({
		step: 0.025,
		min: 0,
		max: 0.5,
		stop: function(event, ui) {
			luminiferousAetherSpeed = -ui.value;
		}
	});

	// Add event listener to canvas to rotate canvas
	var mouse = utils.captureMouse(canvas);
	var touch = utils.captureTouch(canvas);
	canvas.addEventListener('mousedown', function (event) {
		isClicked = true;
		$("#mm canvas").css("cursor", "grabbing");

		dx = mouse.x - midx;
		dy = mouse.y - midy;

		pStartAngle = platformAngle;
		mouseStartAngle = Math.atan2(dy, dx);
	});
	canvas.addEventListener('mouseup', function (event) {
		$("#mm canvas").css("cursor", "grab");
		isClicked = false;
	});
	canvas.addEventListener('mouseleave', function (event) {
		$("#mm canvas").css("cursor", "grab");
		isClicked = false;
	});

	// Add button functionality
	$("#play-button").get(0).addEventListener("click", play, false);
	$("#reset").get(0).addEventListener("click", reset, false);

	// Begin animation!
	drawFrame();

	function play() {
		if (!hasStarted) {
			hasStarted = true;
			light1.vx = LIGHT_SPEED;
			$("#play-button span").get(0).className = "glyphicon glyphicon-pause";
		} else {
			if (playBool) {
				playBool = false;
				$("#play-button span").get(0).className = "glyphicon glyphicon-play";
			} else {
				playBool = true;
				$("#play-button span").get(0).className = "glyphicon glyphicon-pause";
				drawFrame();
			}
		}
	}

	function reset() {
		if (!hasStarted) {
			platformAngle = 0;
			return;
		}

		light1.x = lightRadius * 3;
		light1.y = midy;
		light1.rotation = 3 * Math.PI / 2;
		
		light1.vx = 0;
		light1.vy = 0;

		light2.x = midx;
		light2.y = midy;
		light2.rotation = Math.PI;

		light2.vx = 0;
		light2.vy = 0;

		platformAngle = 0;

		pastMid1 = false;
		pastMid2 = false;

		light1.color = utils.parseColor("yellow");
		light2.color = utils.parseColor("red");

		if (!playBool) {
			drawFrame();
		}
		
		hasStarted = false;
		playBool = true;
		$("#play-button span").get(0).className = "glyphicon glyphicon-play";
	}

	function checkmid() {
		if (!pastMid1 && light1.x >= midx) {
			light2.vy = -light1.vx;
			light2.vx = 0;

			light1.color = utils.parseColor("green");

			pastMid1 = true;
		}

		if (pastMid1 && !pastMid2 && light1.x < midx) {
			light1.x = midx;
			light1.y = midy;

			light1.vy = -light1.vx;
			light1.vx = 0;
			light1.rotation = 0;

			pastMid2 = true;
		}
	}

	function moveBody(body) {
		var left = 0,
			right = canvas.width - 3*lightRadius - mirrorWidth,
			top = 0 + lightRadius*3 + mirrorWidth,
			bottom = canvas.height - 3*lightRadius - 1.5*mirrorWidth;

		body.x += body.vx;
		body.x += (body.vx != 0) ? luminiferousAetherSpeed * Math.sin(platformAngle) : 0;
		body.y += body.vy;
		body.y += (body.vy != 0) ? luminiferousAetherSpeed * Math.cos(platformAngle) : 0;

		// Bouncing off the walls
		if (body.x > right) {
			body.x = right;
			body.vx *= -1;
			body.rotation = Math.PI + body.rotation;
		}

		if (body.y > bottom) {
			body.y = bottom;
			body.color = utils.parseColor("yellow");
			body.vy = 0;
		} else if (body.y < top) {
			body.y = top;
			body.vy *= -1;
			body.rotation = Math.PI + body.rotation;
		}
	}

	function handleRotation() {
		if (isClicked) {
			dx = mouse.x - midx;
			dy = mouse.y - midy;

			dAlpha = Math.atan2(dy, dx) - mouseStartAngle;
			platformAngle = pStartAngle + dAlpha;

			context.font = "30px Arial";
			var formattedAngle = utils.mod((180 * platformAngle / Math.PI), 360).toPrecision(3) + "°";
			var formattedAngle = utils.mod((180 * platformAngle / Math.PI), 360).toPrecision(3) + "°";
			context.fillText(formattedAngle, midx, midy - 2 * mirrorLength);
		}
		if (touch.isPressed) {
			if (touch.event.type === "touchstart") {
				dx = touch.x - midx;
				dy = touch.y - midy;

				pStartAngle = platformAngle;
				touchStartAngle = Math.atan2(dy, dx);
			} else {
				dx = touch.x - midx;
				dy = touch.y - midy;

				dAlpha = Math.atan2(dy, dx) - touchStartAngle;
				platformAngle = pStartAngle + dAlpha;
				context.font = "30px Arial";
				var formattedAngle = utils.mod((180 * platformAngle / Math.PI),360).toPrecision(3) + "°";
				context.fillText(formattedAngle, midx, midy - 2 * mirrorLength);
			}
		}

		// Rotate static canvas
		$("#static_canvas").get(0).style.transform = "rotate(" + platformAngle + "rad)";
	}

	function drawDynamics() {
		context.save();
		context.translate(midx, midy);
		context.rotate(platformAngle);
		context.translate(-midx, -midy);
			light1.draw(context);
			if (pastMid1) {
				light2.draw(context);
			}
		context.restore();

		if (luminiferousAetherSpeed != 0) {
			drawAether();
		}
	}

	function drawAether() {
		for (i = 0; i < aaCount * aaCount; i++) {
			var tempArrow = aetherArrows[i];
			tempArrow.y += luminiferousAetherSpeed;
			tempArrow.y = utils.mod(tempArrow.y, canvasDim);
			tempArrow.draw(context);
		}
	}

	// animate!
	function drawFrame() {
		if (playBool) {
			window.requestAnimationFrame(drawFrame, canvas);
		}
		context.clearRect(0, 0, canvas.width, canvas.height);
		checkmid();

		moveBody(light1);
		moveBody(light2);

		drawDynamics();

		handleRotation();
	}
});

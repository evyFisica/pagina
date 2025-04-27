function Light (radius, color) {
	if (color === undefined) { color = "#ff0000"; }
	this.x = 0;
	this.y = 0;
	this.mass = 0;
	this.vx = 0;
	this.vy = 0;
	this.rotation = 0;
	this.scaleX = 1;
	this.scaleY = 1;
	this.color = utils.parseColor(color);
	this.lineWidth = 1;

	this.wid1 = radius;
	this.wid2 = 2 * radius;
	this.len = 3 * radius;
}

Light.prototype.draw = function (context) {
	context.save();
	context.translate(this.x, this.y);
	context.rotate(this.rotation);
	context.scale(this.scaleX, this.scaleY);

	context.lineWidth = this.lineWidth;
	context.fillStyle = this.color;
	context.strokeStyle = this.color;
	context.beginPath();
	// x, y, radius, start_angle, end_angle, anti-clockwise
	// context.arc(0, 0, this.radius, 0, (Math.PI * 2), true);
	context.moveTo(-this.wid1,-this.len);
	context.lineTo(-this.wid1,0);
	context.stroke();
	context.lineTo(-this.wid2,0);
	context.stroke();
	context.lineTo(0,this.len);
	context.stroke();
	context.lineTo(this.wid2,0);
	context.stroke();
	context.lineTo(this.wid1,0);
	context.stroke();
	context.lineTo(this.wid1,-this.len);
	context.stroke();
	context.lineTo(-this.wid1,-this.len);
	context.stroke();

	// context.closePath();
	context.fill();
	if (this.lineWidth > 0) {
		context.stroke();
	}
	context.restore();
}

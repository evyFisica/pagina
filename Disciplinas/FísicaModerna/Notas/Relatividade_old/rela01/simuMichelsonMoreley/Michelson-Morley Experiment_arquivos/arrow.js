// Author: Lawrence Hook
function Arrow (radius, color) {
	if (color === undefined) { color = "#ff0000"; }
	this.x = 0;
	this.y = 0;
	this.vx = 0;
	this.vy = 0;
	this.rotation = 0;
	this.scaleX = 1;
	this.scaleY = 1;
	this.color = utils.parseColor(color);
	this.lineWidth = .1;

	this.len1 = radius;
	this.len2 = 2 * radius;
}

Arrow.prototype.draw = function (context) {
	context.save();
	context.translate(this.x, this.y);
	context.rotate(this.rotation);
	context.scale(this.scaleX, this.scaleY);

	context.lineWidth = this.lineWidth;

	context.fillStyle = this.color;
	context.strokeStyle = utils.parseColor("gray");
	
	context.beginPath();
	context.moveTo(-this.len2, -this.len1);
	context.lineTo(0, this.len2);
	context.stroke();
	context.lineTo(this.len2, -this.len1);
	context.stroke();
	context.lineTo(0, 0);
	context.stroke();
	context.lineTo(-this.len2,-this.len1);

	context.fill();
	if (this.lineWidth > 0) {
		context.stroke();
	}
	context.restore();
}

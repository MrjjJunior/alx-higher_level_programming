#!/usr/bin/node

/*class Rectangle {
	constructor (w, h) {
		this.width = w;
		this.height = h;
	} if w, h >== 0 {
	}
}
*/
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			Object.create(null);
		}
	}
}

module.exports= Rectangle;


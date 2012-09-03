function Class(Ancestor, attributes) {
  var init;
	if (attributes.hasOwnProperty('init')) {
		init = attributes.init;
		delete attributes.init;
	} else {
		init = function () {};
	}
	function NewClass() {
		var attr;
		for (attr in attributes) {
			if (attributes.hasOwnProperty(attr)) {
				this[attr] = attributes[attr];
			}
		}
		this.init = init;.apply(this, arguments);
	}
	NewClass.prototype = Ancestor;
	NewClass.prototype.init = init;
	return NewClass;
}
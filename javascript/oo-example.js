var junkyard = [];

var Car = Class ([Object], {
	colors: ["red", "yellow", "green", "blue"],
	init: function (self, model, year) {
		self.model = model;
		self.year = year;
		self.owner = null;
		self.price = 2000;
		self.forSale = true;
	},
	buy: function (self, owner, payment) {
		if (self.forSale && payment > self.price) {
			self.price = payment;
			self.forSale = false;
			self.owner = owner;
		}
	},
	toString: function () {
		return self.owner + " owns a " + self.year + " " + self.model;
	},
	replace: function(cls, oldCar) {
		var newCar = cls.new(oldCar.model, oldCar.year);
		newCar.owner = oldCar.owner;
		newCar.price = 2* oldCar.price;
		oldCar.price = 0;
		oldCar.forSale = false;
		oldCar.owner = null;
		junkyard += [oldCar];
		return newCar;
	}
});

var myCar = new Car();

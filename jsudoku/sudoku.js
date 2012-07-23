var sudoku = function () {
// VARIABLES
var b, i, j, k, m, n, o, p;
var puzzle, candidates, numFound;
var line, c, num, blockDim, goodNs, fountHtml;
var coordLog;

// FUNCTIONS

var cellHtmlCoords = function (x, y) {
	return "#candidates .r" + x + " .c" + y;
};

var numHtmlCoords = function (x, y, n) {
	return cellHtmlCoords(x, y) + " .n" + n;
}

var blockDim = function (coord, size) {
	var block = Math.floor(coord/size);
	return {"start": 3*block, "end": 3*(block+1)};
}

// CLASSES

function Candidates () {
	this.candidates = [];
	for (i = 0; i < 9; i++) {
		line = [];
		for (j = 0; j < 9; j++) {
			c = []
			for (k = 0; k < 9; k++) {
				c.push(true);
			}
			line.push(c);
		}
		this.candidates.push(line);
	}
	
	this.clear = function (x, y, num) {
		this.candidates[x][y][num-1] = false;
		$(numHtmlCoords(x,y,num)).html("&ensp;");
	};
	
	this.isGood = function (x, y, n) {
		return this.candidates[x][y][n];
	};
	
	this.log = function () { console.dir(this.candidates); };
}

// START

puzzle = [];

for (i = 0; i < 9; i++) {
	line = [];
	for (j = 0; j < 9; j++) {
		line.push(0);
	}
	puzzle.push(line);
}
puzzle[0][2] = 9;
puzzle[0][3] = 3;
puzzle[0][5] = 7;
puzzle[0][8] = 6;
puzzle[1][1] = 7;
puzzle[1][3] = 9;
puzzle[2][1] = 1;
puzzle[2][5] = 5;
puzzle[2][8] = 2;
puzzle[3][0] = 7;
puzzle[4][0] = 6;
puzzle[4][1] = 8;
puzzle[4][2] = 1;
puzzle[4][3] = 5;
puzzle[5][2] = 5;
puzzle[5][4] = 7;
puzzle[5][5] = 9;
puzzle[6][1] = 5;
puzzle[6][6] = 1;
puzzle[7][1] = 2;
puzzle[7][4] = 3;
puzzle[7][5] = 8;
puzzle[7][7] = 7;
puzzle[8][0] = 9;
puzzle[8][2] = 8;

candidates = new Candidates();

numFound = 0;

while (numFound < 81) {
	for (i = 0; i < 9; i++) {
		b = { "i": blockDim(i,3) };
		for (j = 0; j < 9; j++) {
			num = puzzle[i][j];
			if (num != 0) {
				b["j"] = blockDim(j,3);
				for (n = 1; n < 10; n++) {
					if (n != num) {
						candidates.clear(i,j,n);
					}
				}
				for (m = 0; m < 9; m++) {
					if (m != j) {
						candidates.clear(i,m,num);
					}
					if (m != i) {
						candidates.clear(m,j,num);
					}
				}
			
				for (m=b.i.start; m < b.i.end; m++) {
					for (n=b.j.start; n < b.j.end; n++) {
						if ( m != i && n != j) {
							candidates.clear(m,n,num);
						}
					}
				}
			
			}
		}
	}
	numFound = 0;
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			goodNs = [];
			for (n = 0; n < 9; n++) {
				if (candidates.isGood(i,j,n)) {
					goodNs.push(n);
				}
			}
			if (goodNs.length == 1) {
				o = goodNs[0] + 1;
				fountHtml = "<span class=\"found\">" + o + "</span>";
				$(cellHtmlCoords(i,j)).html(fountHtml);
				puzzle[i][j] = o;
				numFound++;
			}
		}
	}
}
		
// END
};

$(document).ready( function () {
	sudoku();
});

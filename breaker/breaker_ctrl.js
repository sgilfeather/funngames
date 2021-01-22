
const canvas = document.getElementById('can');
const ctx = canvas.getContext('2d');

let x = canvas.width/2;
let y = canvas.height-60;
var interval; let count = 0;
let dx = 2.0; let dy = 2; let paddlex = 0.5*canvas.width-45;


var bricks = []; let brickX, brickY;
for (let c = 0; c < 5; c++) {
    bricks[c] = [];
    for (let r = 0; r < 3; r++) {
        brickX = c*(75 + 10) + 30;
        brickY = r*(20 + 10) + 60;
        bricks[c][r] = { x: brickX, y: brickY, stat: 1};
    }
}

function drawGame() {
    ctx.beginPath();
    ctx.arc(x, y, 16, 0, Math.PI*2);
    ctx.fillStyle = "rgba(0,66,255,0.5)";
    ctx.fill();
    ctx.closePath();

    ctx.beginPath();
    ctx.fillRect(paddlex, canvas.height-30, 90, 15);
    ctx.closePath();

    ctx.beginPath();
    ctx.fillStyle = "rgba(180, 180, 180, 1)";
    ctx.font = "48px sans-serif"; ctx.fontFamily = "Rockwell";
    ctx.fillText(count.toString(), 0.5*canvas.width-15, canvas.height-90);
    ctx.closePath();

    for (let c = 0; c < 5; c++) {
        for (let r = 0; r < 3; r++) {
            let b = bricks[c][r];
            if (b.stat == 1){
                ctx.beginPath();
                ctx.fillStyle = "rgba(255,66,0,0.5)";
                ctx.fillRect(b.x, b.y, 75, 20);
                ctx.closePath();
            }
        }
    }
}
function draw() {
    ctx.clearRect(0,0,canvas.width, canvas.height);
    drawGame();
    checkEdges();
    x += dx;
    y += dy;

}

let leftPress = false; let rightPress = false;
function keyDown(e) {
    if (e.key == "Right" || e.key == "ArrowRight"){ rightPress = true; }
    else if (e.key == "Left" || e.key == "ArrowLeft"){ leftPress = true; }

}
function keyUp(e) {
    if (e.key == "Right" || e.key == "ArrowRight"){ rightPress = false; }
    if (e.key == "Left" || e.key == "ArrowLeft"){leftPress = false; }
}

document.addEventListener("keydown", keyDown, false);
document.addEventListener("keyup", keyUp, false);

function checkEdges() {
    if (x < 8) { dx = 2.0; }
    if (y === 8) { dy = 2; }
    if (x > canvas.width-8) { dx = -2.0; }
    if (x < paddlex+106 && x > paddlex-16 && y === canvas.height-46) {
        dy = -2;
        dx = 4*(((paddlex+45)-x)/90);
    }
    if (y === canvas.height-8 || count == 15) {
        document.getElementById('gmo').style.visibility = 'visible';
        document.getElementById('gmo').addEventListener('click',
            function () { document.location.reload(); clearInterval(interval); }, false);
    }

    for (let c = 0; c < 5; c++) {
        for (let r = 0; r < 3; r++) {
            let b = bricks[c][r];
            if (b.stat !== 0){
                if (x+8 > b.x && x-8 < b.x+75 && y-8 > b.y && y+8 < b.y+20) {
                    dy = -dy;
                    b.stat = 0;
                    count++;
                }
            }
        }
    }

    if (leftPress) {
        paddlex -= 4;
        if (paddlex < 0) { paddlex = 0; }
    }
    if (rightPress) {
        paddlex += 4;
        if (paddlex + 90 > canvas.width) { paddlex = canvas.width - 90; }
    }
}



interval = setInterval(draw, 10);

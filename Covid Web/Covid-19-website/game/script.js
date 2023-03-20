let initial = {x: 0, y: 0}; 
const foodSound = new Audio('food.mp3');
const gameOverSound = new Audio('gameover.mp3');
const moveSound = new Audio('move.mp3');
const musicSound = new Audio('music.mp3');
let speed = 5;
let score = 0;
let lastPaintTime = 0;
let snakearray = [
    {x: 15, y: 15}
];

food = {x: 7, y: 7};

// Game Functions
function main(ctime) {
    musicSound.play();

    window.requestAnimationFrame(main);
    if((ctime - lastPaintTime)/1000 < 1/speed){
        return;
    }
    lastPaintTime = ctime;
    gameEngine();
}

function Collide(snake) {
    // If you bump into yourself 
    for (let i = 1; i < snakearray.length; i++) {
        if(snake[i].x === snake[0].x && snake[i].y === snake[0].y){
            return true;
        }
    }
    // If you bump into the wall
    if(snake[0].x >= 30 || snake[0].x <=0 || snake[0].y >= 25 || snake[0].y <=0){
        return true;
    }
        
    return false;
}

function gameEngine(){

    if(Collide(snakearray)){
        gameOverSound.play();
        musicSound.pause();
        initial =  {x: 0, y: 0}; 
        alert("Game Over !");
        snakearray = [{x: 15, y: 15}];
        musicSound.play();
        scoreBox.innerHTML = "Score:0 "
        score = 0;
        speed=5;
    }

    // If you have eaten the food, increment the score and regenerate the food
    if(snakearray[0].y === food.y && snakearray[0].x ===food.x){
        foodSound.play();
        score += 1;
         
        scoreBox.innerHTML = "Score: " + score;
        snakearray.unshift({x: snakearray[0].x + initial.x, y: snakearray[0].y + initial.y});
        let a =1,b=30;
        let p=1,q=25;
        food = {x: Math.round(a + (b-a)* Math.random()), y: Math.round(p + (q-p)* Math.random())}
    }

    // Moving the snake
    for (let i = snakearray.length-2; i>=0; i--) { 
        snakearray[i+1] = {...snakearray[i]};
    }

    snakearray[0].x += initial.x;
    snakearray[0].y += initial.y;

    // Display the snake
    box.innerHTML = "";
    snakearray.forEach((e, index)=>{
        snakeElement = document.createElement('div');
        snakeElement.style.gridRowStart = e.y;
        snakeElement.style.gridColumnStart = e.x;

        if(index === 0){
            snakeElement.classList.add('head');
        }
        else{
            snakeElement.classList.add('tail');
        }
        box.appendChild(snakeElement);
    });
    // Display the food
    foodElement = document.createElement('div');
    foodElement.style.gridRowStart = food.y;
    foodElement.style.gridColumnStart = food.x;
    foodElement.classList.add('food')
    box.appendChild(foodElement);

    // speed
    if (score > 2 && score <= 5) {
      speed=8;  
    }
    if (score > 5 && score <= 8) {
      speed=11;  
    }
    if (score > 8 && score <= 15) {
      speed=15;  
    }
    if (score > 15 && score <= 20) {
      speed=18;  
    }
    if (score > 20 ) {
      speed=20;  
    }
}


// Main
window.requestAnimationFrame(main);
//musicSound.play();
window.addEventListener('keydown', e =>{
    initial = {x: 0, y: 1} 
    moveSound.play();
    switch (e.key) {
        case "ArrowUp":
            
            initial = {x:0,y:-1};
            break;

        case "ArrowDown":
            initial = {x:0,y:1};
            break;

        case "ArrowLeft":
            initial = {x:-1,y:0};
            break;

        case "ArrowRight":
            initial = {x:1,y:0};
            break;
        default:
            break;
    }

});
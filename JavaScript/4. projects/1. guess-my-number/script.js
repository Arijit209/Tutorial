let sectretNumber = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highscore = 0;

const displayMessage = function (message) {
    document.querySelector('.message').textContent = message;
}

document.querySelector('.check').addEventListener('click', function () {
    const guess = Number(document.querySelector('.guess').value);
    if (!guess) {
        displayMessage('No number!');
    } else if (guess === sectretNumber) {
        displayMessage('Correct Number!');
        document.querySelector('.number').textContent = sectretNumber;
        document.querySelector('body').style.backgroundColor = '#60b347';
        if (score > highscore) {
            highscore = score;
            document.querySelector('.highscore').textContent = highscore;
        }
    } else if (guess !== sectretNumber) {
        if (score > 1) {
            displayMessage(guess > sectretNumber ? 'Too high!' : 'Too low!');
            score--;
            document.querySelector('.score').textContent = score;
        } else {
            displayMessage('You lost the game!');
            document.querySelector('.score').textContent = 0;
        }
    }
});

document.querySelector('.again').addEventListener('click', function () {
    score = 20;
    sectretNumber = Math.trunc(Math.random() * 20) + 1; 
    displayMessage('Start guessing...');
    document.querySelector('.score').textContent = score;
    document.querySelector('.number').textContent = '?';
    document.querySelector('.guess').value = '';
    document.querySelector('body').style.backgroundColor = '#222';
});
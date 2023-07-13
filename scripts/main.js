const url = "http://localhost:8000/play";

const score = {0: "rock", 1: "paper", 2: "scissors"};

document.querySelector(".new-game").addEventListener("click", function() {
    location.reload();
});

function compImage (comp) {
    document.querySelector(".computer-outcome").innerHTML = `
    <img src="images/${score[comp]}.png" class="emoji">`;
}

async function play (user) {
    const param = {params: {player_action : Number(user)}};
    const response = await axios.post(url, null, param);
    const compResult = await response.data;        

    if (user == 0 && compResult == 0 || user == 1 && compResult == 1 || user == 2 && compResult == 2) {
        document.querySelector(".result").innerHTML = "You TIED";
        document.querySelector(".tied-score").innerHTML ++;
    }
    else if (user == 0 && compResult == 1 || user == 1 && compResult == 2 || user == 2 && compResult == 0) {
        document.querySelector(".result").innerHTML = "You LOST";
        document.querySelector(".lost-score").innerHTML ++;
    }
    else {
        document.querySelector(".result").innerHTML = "You WON!!!";
        document.querySelector(".won-score").innerHTML ++;
    }
    compImage(compResult);
}

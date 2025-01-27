const gameboard = document.querySelector("#gameboard")
const InfoDisplay = document.querySelector("#info")
const startCells = [
    "", "", "","", "", "","", "", ""
]

let go = "Kreis"
InfoDisplay.textContent = "Kreis ist zuerst";
    

function createBoard() {
    startCells.forEach((_cell, index) => {
        const cellElement = document.createElement("div");
        cellElement.classList.add("square");
        cellElement.id = index;
        cellElement.addEventListener("click", addGo);
        gameboard.append(cellElement);
    });
}
createBoard();

function addGo(e) {
    const goDisplay = document.createElement("div");
    goDisplay.classList.add(go);
    e.target.append(goDisplay);
    go = go === "Kreis" ? "Kreuz" : "Kreis";
    InfoDisplay.textContent = "Jetzt ist " + go + " drann."
    e.target.removeEventListener("click", addGo)
    checkScore();
}

function checkScore() {
    const allSquares = document.querySelectorAll(".square")
    const winningCombos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    winningCombos.forEach(Array => {
        const circleWins= Array.every(cell => allSquares[cell].firstChild?.classList.contains("Kreis"))
       
        if (circleWins) {
            InfoDisplay.textContent = "Kreis gewinnt!"
            allSquares.forEach(square => square.replaceWith(square.cloneNode(true)))
            return;
        }
    
    });
    winningCombos.forEach(Array => {
        const crossWins= Array.every(cell => allSquares[cell].firstChild?.classList.contains("Kreuz"))
       
        if (crossWins) {
            InfoDisplay.textContent = "Kreuz gewinnt!"
            allSquares.forEach(square => square.replaceWith(square.cloneNode(true)))
            return;
        }
    });

}


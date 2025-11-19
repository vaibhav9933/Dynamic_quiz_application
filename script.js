const quizData = {
    gk: {
        easy: [
            {q:"National animal of India?", a:["Tiger","Lion","Elephant","Leopard"], c:0},
            {q:"Capital of India?", a:["Delhi","Mumbai","Kolkata","Pune"], c:0},
            {q:"National bird of India?", a:["Peacock","Sparrow","Crow","Parrot"], c:0},
            {q:"Largest continent?", a:["Asia","Africa","Europe","Australia"], c:0},
            {q:"Planet known as Red Planet?", a:["Mars","Venus","Mercury","Earth"], c:0}
        ],
        medium: [
            {q:"Who wrote 'Discovery of India'?", a:["Jawaharlal Nehru","Gandhi","Subhash Chandra Bose","Rabindranath Tagore"], c:0},
            {q:"How many states are in India?", a:["28","29","30","27"], c:0},
            {q:"International Yoga Day?", a:["21 June","5 June","15 August","1 May"], c:0},
            {q:"Largest river in the world?", a:["Nile","Amazon","Ganga","Yangtze"], c:1},
            {q:"Nobel Prize is awarded in?", a:["Sweden","USA","Japan","Italy"], c:0}
        ],
        hard: [
            {q:"First Indian to win Nobel Prize?", a:["Rabindranath Tagore","C V Raman","Mother Teresa","Amartya Sen"], c:0},
            {q:"Who discovered Zero?", a:["Aryabhata","Brahmagupta","Ramanujan","Newton"], c:1},
            {q:"The term ‘Satyagraha’ was first used in?", a:["South Africa","India","UK","France"], c:0},
            {q:"Largest democracy in the world?", a:["India","USA","China","Russia"], c:0},
            {q:"First man in space?", a:["Yuri Gagarin","Neil Armstrong","Buzz Aldrin","Alan Shepard"], c:0}
        ]
    },

    cs: {
        easy: [
            {q:"Father of Computer?", a:["Charles Babbage","Newton","Einstein","Edison"], c:0},
            {q:"HTML stands for?", a:["HyperText Markup Language","HighTech Machine Language","Hyper Tabular ML","None"], c:0},
            {q:"Binary uses the digits?", a:["0 & 1","1 & 2","2 & 3","3 & 4"], c:0},
            {q:"RAM means?", a:["Random Access Memory","Read Access Memory","Rapid Access Machine","None"], c:0},
            {q:"CPU stands for?", a:["Central Processing Unit","Computer Power Unit","Core Programming Unit","None"], c:0}
        ],
        medium: [
            {q:"Operating System is?", a:["System Software","Application Software","Utility Software","Compiler"], c:0},
            {q:"TCP stands for?", a:["Transmission Control Protocol","Transfer Code Program","Total Communication Process","None"], c:0},
            {q:"Which is a frontend language?", a:["JavaScript","C","Java","Python"], c:0},
            {q:"SQL used for?", a:["Database Query","Graphics","Networking","OS"], c:0},
            {q:"Which is not an OS?", a:["Python","Windows","Linux","MacOS"], c:0}
        ],
        hard: [
            {q:"What is Big O Notation?", a:["Algorithm Complexity","Network Speed","Memory Size","Compiler"], c:0},
            {q:"Which loop guarantees at least one execution?", a:["do-while","for","while","none"], c:0},
            {q:"Primary key must be?", a:["Unique & Not Null","Duplicate","Null","Encrypted"], c:0},
            {q:"AI stands for?", a:["Artificial Intelligence","Automated Integration","Analog Input","None"], c:0},
            {q:"Which data structure uses FIFO?", a:["Queue","Stack","Tree","Graph"], c:0}
        ]
    }
};


let questions = [], current = 0, correct = 0, wrong = 0, timer;
let timePerQuestion = 10;

document.getElementById("startBtn").addEventListener("click", () => {
    let cat = document.getElementById("category").value;
    let diff = document.getElementById("difficulty").value;
    questions = quizData[cat][diff];

    document.getElementById("settings").classList.add("hidden");
    document.getElementById("quizBox").classList.remove("hidden");

    loadQuestion();
});

function loadQuestion() {
    if (current >= questions.length) return finishQuiz();

    resetTimer();
    const q = questions[current];
    document.getElementById("question").innerText = q.q;
    let opts = "";
    q.a.forEach((opt, i) => {
        opts += `<div class='option' onclick="checkAnswer(${i})">${opt}</div>`;
    });
    document.getElementById("options").innerHTML = opts;
}

function resetTimer() {
    clearInterval(timer);
    let countdown = timePerQuestion;
    document.getElementById("timer").innerText = countdown;

    timer = setInterval(() => {
        countdown--;
        document.getElementById("timer").innerText = countdown;
        if (countdown <= 0) {
            wrong++;
            nextQuestion();
        }
    }, 1000);
}

function checkAnswer(i) {
    if (i === questions[current].c) correct++;
    else wrong++;
    nextQuestion();
}

function nextQuestion() {
    current++;
    loadQuestion();
}

function finishQuiz() {
    clearInterval(timer);
    document.getElementById("quizBox").classList.add("hidden");
    document.getElementById("resultBox").classList.remove("hidden");

    document.getElementById("correct").innerText = correct;
    document.getElementById("wrong").innerText = wrong;
    document.getElementById("score").innerText = `${(correct/questions.length)*100}%`;
}

document.getElementById("nextBtn").onclick = nextQuestion;

document.addEventListener('DOMContentLoaded', function () {
    let correct = document.getElementsByClassName('correct')[0]
    correct.addEventListener('click', function () {
        correct.style.backgroundColor = 'green'
        document.getElementById('ans1').innerHTML = 'Correct'
    })

    let incorrect = document.querySelectorAll('.incorrect')
    for (let i = 0; i < incorrect.length; i++) {
        incorrect[i].addEventListener('click', function () {
            incorrect[i].style.backgroundColor = 'red'
            document.getElementById('ans1').innerHTML = 'Incorrect'
        })
    }


    let button = document.getElementById('submit')
    button.addEventListener('click', function () {
        let input = document.getElementsByName('answer')[0]
        if (input.value.toLowerCase() === "switzerland") {
            input.style.backgroundColor = 'green'
            document.getElementById('ans2').innerHTML = 'Correct'

        }
        else {
            input.style.backgroundColor = 'red'
            document.getElementById('ans2').innerHTML = 'incorrect'
        }
    })
})
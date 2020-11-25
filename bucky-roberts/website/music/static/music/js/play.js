console.log('loaded javascript file successfully.')

const source = document.getElementById("source");
const player = document.getElementById("player");
//const duration = document.getElementById('duration');


const links = document.querySelectorAll("input[class='song']");
// for-of loop
// gives us a constant value for each "link" in our list of links:
links.forEach(link => {
    // we can then use this link and add an event listener:
    console.log(link);
    link.addEventListener("change", setSong);
});

// 7. change to setSong function name to match above -test/done:
function setSong(e) {
    console.log(e.target.checked, e.target);
    label = e.target.nextElementSibling;
    const playBtn = label.querySelector('#play');
    const pauseBtn = label.querySelector('#pause');

    //  control play/pause btn.
    if(e.target.checked) {      /* song is playing */
        playBtn.hidden = true;
        pauseBtn.hidden = false;
        //  duration.hidden = false;
    }
    else {
        playBtn.hidden = false;
        pauseBtn.hidden = true;
        //  duration.hidden = true;
        player.play();
        return;
    }

    source.url = e.target.dataset.path

    player.load();
    player.play();
}

function playAudio() {
  if (player.readyState) {
    player.play();
  }
}

function pauseAudio() {
  player.pause();
}
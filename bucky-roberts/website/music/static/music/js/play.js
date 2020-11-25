console.log('loaded javascript file successfully.')


const links = document.querySelectorAll("input.song");


console.log(links);


// for-of loop
// gives us a constant value for each "link" in our list of links:

for (const link of links) {
    console.log(link);
    // we can then use this link and add an event listener:
    link.addEventListener("change", setSong);
}


function setSong(e) {

    name = e.target.dataset.key;
    console.log(name)

    sound = document.querySelector(`audio[data-key="${name}"]`)
    let label =  e.target.nextElementSibling;
    let playBtn = label.querySelector('#play');
    let stopBtn = label.querySelector('#stop');
//    const playBtn = e.target.nextElementSibling.children[0];
//    const stopBtn = e.target.nextElementSibling.children[1];


    //  control play/pause btn.
    if(e.target.checked) {
        console.log('playing', e.target.dataset.key);
        playBtn.hidden = true;      //  hide
        stopBtn.hidden = false;     //  un-hide

        sound.play();
    }

    else {
        console.log('paused');
        playBtn.hidden = false;     //  un-hide
        stopBtn.hidden = true;      //  hide
        sound.pause()
        sound.currentTime = 0;
        return;
    }


}

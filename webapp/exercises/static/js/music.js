document.addEventListener("DOMContentLoaded", function () {
    const playButton = document.getElementById("play-button");

    playButton.addEventListener("click", function (event) {
        event.stopPropagation();
        playRandomVideo();
    });
});


let player;
const videoIds = [
    'HVsDg7Nfeno',
    'TROsj_xtEgM',
    'GNHWGKNvjho',
    'ywyewY5cPKc',
    'xfwRTZBY2tw',
    'j8v6vRJgcF8',
    'LmX18rxPrC4',
    'C4MpzSMkinw',
    'RpRiiEUc67Y',
    'QGMkBZ7SMoo',
    'Y0ptv4MMzxc',
    'fwrflawejvE',
    '00KtAKMKBA8'
];

function adjustVolume() {
    const volumeSlider = document.getElementById("volume-slider");
    const volume = volumeSlider.value;

    if (player) {
        // Set the volume of the YouTube player (values between 0 and 100)
        player.setVolume(volume);
    }
}

function onYouTubeIframeAPIReady() {
    const randomVideoId = getRandomVideoId();
    player = new YT.Player('youtube-player', {
        height: '360',
        width: '640',
        videoId: randomVideoId,
        playerVars: {
            'autoplay': 0,
            'controls': 1,
        },
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange,
        },
        volume: 50,
    });
}


function onPlayerReady(event) {
    const playIcon = document.querySelector("#play-button i.fa-play");
    const pauseIcon = document.querySelector("#play-button i.fa-pause");
    const loadingSpinner = document.querySelector("#play-button i.fa-spinner");

    playIcon.style.display = "block";
    pauseIcon.style.display = "none";
    loadingSpinner.style.display = "none";
}

function onPlayerStateChange(event) {
    if (event.data === YT.PlayerState.BUFFERING) {

        const loadingSpinner = document.querySelector("#play-button i.fa-spinner");
        const playIcon = document.querySelector("#play-button i.fa-play");
        const pauseIcon = document.querySelector("#play-button i.fa-pause");

        loadingSpinner.style.display = "block";
        playIcon.style.display = "none";
        pauseIcon.style.display = "none";
    } else if (event.data === YT.PlayerState.PLAYING) {
        const loadingSpinner = document.querySelector("#play-button i.fa-spinner");
        const pauseIcon = document.querySelector("#play-button i.fa-pause");

        loadingSpinner.style.display = "none";
        pauseIcon.style.display = "block";
    } else if (event.data === YT.PlayerState.PAUSED || event.data === YT.PlayerState.ENDED) {
        const loadingSpinner = document.querySelector("#play-button i.fa-spinner");
        const playIcon = document.querySelector("#play-button i.fa-play");

        loadingSpinner.style.display = "none";
        playIcon.style.display = "block";
    }
}

function getRandomVideoId() {
    const randomIndex = Math.floor(Math.random() * videoIds.length);
    return videoIds[randomIndex];
}

function playRandomVideo() {
    event.stopPropagation();
    const playIcon = document.querySelector("#play-button i.fa-play");
    const pauseIcon = document.querySelector("#play-button i.fa-pause");

    if (playIcon.style.display === "block") {
        const randomVideoId = getRandomVideoId();
        player.loadVideoById({
            videoId: randomVideoId,
            startSeconds: getRandomStartTime()
        });
        resetVideo();
        player.playVideo();

        playIcon.style.display = "none";
        pauseIcon.style.display = "block";
    } else {
        player.pauseVideo();

        playIcon.style.display = "block";
        pauseIcon.style.display = "none";
    }
}


function getRandomStartTime() {
    const videoDuration = player.getDuration();
    const halfDuration = videoDuration / 2;
    const randomStartTime = Math.random() * halfDuration;
    return randomStartTime;
}

    function resetVideo() {
        if (player) {
            const videoDuration = player.getDuration();
            const randomStartTime = Math.random() * (videoDuration / 2); // Generate a random time within the first half of the video
            player.seekTo(randomStartTime);
            player.playVideo();
        }
    }

// Select important DOM elements
const nextBtn = document.querySelector('.next');
const prevBtn = document.querySelector('.prev');
const slider = document.querySelector('.slider');
const sliderList = slider.querySelector('.list');
const thumbnail = document.querySelector('.thumbnail');

// Create a loader element
const loader = document.createElement('div');
loader.classList.add('slider-loader');
slider.appendChild(loader); // Append the loader to the slider container

// Move the first thumbnail to the end initially
thumbnail.appendChild(thumbnail.querySelectorAll('.item')[0]);

// Function to move slider
function moveSlider(direction) {
    const sliderItems = sliderList.querySelectorAll('.item');
    const thumbnailItems = thumbnail.querySelectorAll('.item');

    if (direction === 'next') {
        sliderList.appendChild(sliderItems[0]); // Move first slide to the end
        thumbnail.appendChild(thumbnailItems[0]); // Move first thumbnail to the end
        slider.classList.add('next'); // Add animation class
    } else if (direction === 'prev') {
        sliderList.prepend(sliderItems[sliderItems.length - 1]); // Move last slide to the start
        thumbnail.prepend(thumbnailItems[thumbnailItems.length - 1]); // Move last thumbnail to the start
        slider.classList.add('prev'); // Add animation class
    }

    // Remove animation class after the animation ends
    slider.addEventListener('animationend', () => {
        slider.classList.remove('next', 'prev');
    }, { once: true }); // Ensure the listener is removed after execution
}

// Add click functionality to navigation buttons
nextBtn.addEventListener('click', () => {
    moveSlider('next');
    resetAutoSlide(); // Reset the automatic slider timer on manual interaction
});
prevBtn.addEventListener('click', () => {
    moveSlider('prev');
    resetAutoSlide(); // Reset the automatic slider timer on manual interaction
});

// Add keyboard arrow functionality
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') {
        moveSlider('next');
        resetAutoSlide(); // Reset the automatic slider timer on manual interaction
    } else if (event.key === 'ArrowLeft') {
        moveSlider('prev');
        resetAutoSlide(); // Reset the automatic slider timer on manual interaction
    }
});

// Automatic sliding functionality
let autoSlideInterval = setInterval(() => {
    moveSlider('next');
    startLoader(); // Restart the loader animation
}, 5000); // Change slides every 5 seconds

// Reset the automatic slider timer
function resetAutoSlide() {
    clearInterval(autoSlideInterval); // Clear the current interval
    autoSlideInterval = setInterval(() => {
        moveSlider('next');
        startLoader(); // Restart the loader animation
    }, 5000); // Restart the interval with the same delay
    startLoader(); // Reset loader animation
}

// Start the loader animation
function startLoader() {
    loader.style.animation = 'none'; // Reset the animation
    setTimeout(() => {
        loader.style.animation = 'slide-loader 5s linear infinite'; // Restart the animation
    }, 0);
}

// Start the loader initially
startLoader();

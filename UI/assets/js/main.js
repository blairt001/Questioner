//Main js ,ES6 standard
//Tony
let questionBtn = document.querySelector(".question-btn");
let rsvpBtn = document.querySelector(".rsvp-btn");
let upVoteBtn = document.querySelector(".up-vote-btn");
let downVoteBtn = document.querySelector(".down-vote-btn");
let commentBtn = document.querySelector(".comment-btn");

let askQuestionContainer = document.querySelector(".hidden-question-container");
let rsvpIcon = document.querySelector(".fa-calendar-check");
let upVoteAmount = document.querySelector(".up-vote-amount").innerHTML;
let downVoteAmount = document.querySelector(".down-vote-amount").innerHTML;
let commentContainer = document.querySelector(".comment-div");

let toggleState = 0;
let voteCheck =0;
let upVoteCount =1;
let downVoteCount =1;
// toggle display of question input form
questionBtn.onclick = function () {
  if (toggleState == 0) {
    askQuestionContainer.classList.remove("d-none")
    askQuestionContainer.classList.add("d-flex")
    toggleState = 1;

  } else {
    askQuestionContainer.classList.add("d-none")
    askQuestionContainer.classList.remove("d-flex")
    toggleState = 0;
  }
}

// Toggle rsvp user effect(color)
rsvpBtn.onclick = function () {
  if (toggleState == 0) {
    rsvpIcon.classList.remove("text-grey")
    rsvpIcon.classList.add("text-blue")
    document.querySelector(".rsvp-tooltip-text").innerHTML = "Click here to cancel";
    toggleState = 1;

  } else {
    rsvpIcon.classList.add("text-grey")
    rsvpIcon.classList.remove("text-blue")
    document.querySelector(".rsvp-tooltip-text").innerHTML = "Click here to rsvp";
    toggleState = 0;
  }
}

// upvote funtion
function upVote() {
  upVoteAmount = Number(upVoteAmount);
  voteCheck = upVoteAmount + 1;
  if (voteCheck%2 !== 0) {
    upVoteAmount += 1;
    let newUpVoteAmount = document.querySelector(".up-vote-amount");
    newUpVoteAmount.textContent = upVoteAmount;
    upVoteBtn.classList.add("text-blue")
  } else if (voteCheck%2 === 0) {
    upVoteAmount -= 1;
    let newUpVoteAmount = document.querySelector(".up-vote-amount");
    newUpVoteAmount.textContent = upVoteAmount;
    upVoteBtn.classList.remove("text-blue")
  }
}
upVoteBtn.onclick = function () {

  if (downVoteCount%2 !== 0) {
    upVote();
  } else {
    return
  }

  upVoteCount ++;
}

// downvote funtion
function downVote() {
    downVoteAmount = Number(downVoteAmount);
    voteCheck = downVoteAmount + 1;
    if (voteCheck%2 !== 0) {
      downVoteAmount += 1;
      let newDownVoteAmount = document.querySelector(".down-vote-amount");
      newDownVoteAmount.textContent = downVoteAmount;
      downVoteBtn.classList.add("text-red")
    } else if (voteCheck%2 === 0) {
      downVoteAmount -= 1;
      let newDownVoteAmount = document.querySelector(".down-vote-amount");
      newDownVoteAmount.textContent = downVoteAmount;
      downVoteBtn.classList.remove("text-red")
    }
}
downVoteBtn.onclick = function () {
  if (upVoteCount%2 !== 0) {
    downVote();
  } else {
    return
  }
  downVoteCount ++;
}

// toggle display of comment input form
commentBtn.onclick = function () {
  if (toggleState == 0) {
    commentContainer.classList.remove("d-none")
    commentContainer.classList.add("d-block")
    toggleState = 1;

  } else {
    commentContainer.classList.add("d-none")
    commentContainer.classList.remove("d-block")
    toggleState = 0;
  }
}

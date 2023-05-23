// twitter handle regex
const twitterHandleRegex = /^@[\w\d]+$/;

// the handle of the APis

const handle = "@myUsername123";

// verify if exists
if (twitterHandleRegex.test(handle)) {
  console.log("Valid Twitter handle");
} else {
  console.log("Invalid Twitter handle");
}
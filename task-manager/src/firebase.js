// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyC5uc2EW0BPKAZ2bZ9UsCY0u1GUIQsXtQA",
    authDomain: "task-manager-c5803.firebaseapp.com",
    projectId: "task-manager-c5803",
    storageBucket: "task-manager-c5803.appspot.com",
    messagingSenderId: "39297573184",
    appId: "1:39297573184:web:30bcee112b3d19b5a95aa5",
    measurementId: "G-YQVXSPJJNH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);

const db = firebase.firestore();
const auth = firebase.auth();

export { db, auth };
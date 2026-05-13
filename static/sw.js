self.addEventListener("install", () => {
  console.log("ConvoMate SW installed");
});

self.addEventListener("fetch", () => {
  // basic offline pass-through
});
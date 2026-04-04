console.log("AIP-HSD Static HUD Active.");
// Simple fetch logic for polyglot backends
fetch('http://localhost:8000/api/threats')
    .then(r => r.json())
    .then(data => console.log("Static HUD: Received Intel", data))
    .catch(e => console.warn("Static HUD: Backend offline"));

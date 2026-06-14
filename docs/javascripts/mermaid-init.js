document.addEventListener("DOMContentLoaded", function () {
  if (!window.mermaid) {
    return;
  }

  document.querySelectorAll("pre.mermaid").forEach(function (block) {
    var code = block.querySelector("code");
    var diagram = document.createElement("div");
    diagram.className = "mermaid";
    diagram.textContent = code ? code.textContent : block.textContent;
    block.replaceWith(diagram);
  });

  window.mermaid.initialize({
    startOnLoad: false,
    theme: "default",
    securityLevel: "loose"
  });

  window.mermaid.run({
    querySelector: ".mermaid"
  });
});

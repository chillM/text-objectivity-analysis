function analyzeText (node) {

    console.log("analyzing " + node.textContent);

    if (node.nodeType === Node.TEXT_NODE) {
        let content = node.textContent;
        let result;
        let resultString;

        //break content into sentences
        let sentences = content.split('.');

        //run content through model one sentence at a time
        sentences.forEach(sentence => {

            //run model on sentence
            result = Math.floor(Math.random() * 2); //0 or 1

            //build the resulting DOM content
            if( result === 0) {
                //objective
                resultString += sentence + ".";
            }
            else {
                //subjective
                resultString += "<span class='opinionate-highlight'>" + sentence + ".</span>";
                console.log("Added highlighting");
            }
        });

        node.innerHTML = resultString;

    }
    else { //the node is not a text node
        // call analyzeText() on each of its children.
        for (let i = 0; i < node.childNodes.length; i++) {
            analyzeText(node.childNodes[i]);
        }  
    }

}

analyzeText(document.body);

//watch the page for any changes to highlight them as well
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.addedNodes && mutation.addedNodes.length > 0) {
        // This DOM change was new nodes being added. Run our substitution
        // algorithm on each newly added node.
        for (let i = 0; i < mutation.addedNodes.length; i++) {
          const newNode = mutation.addedNodes[i];
          analyzeText(newNode);
        }
      }
    });
  });
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
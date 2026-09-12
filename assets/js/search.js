/**
 * Fluente-Mente
 * Search JavaScript
 *
 * Ricerca client-side degli articoli pubblicati.
 */

document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.querySelector("#search-input");
  const searchResults = document.querySelector("#search-results");
  const searchStatus = document.querySelector("#search-status");

  if (!searchInput || !searchResults) {
    return;
  }

  let articles = [];

  /**
   * Normalizza il testo:
   * - minuscolo
   * - rimozione degli accenti
   * - rimozione degli spazi inutili
   */
  function normalize(text) {
    return String(text || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .trim();
  }

  /**
   * Evita che contenuti provenienti dai dati
   * vengano interpretati come HTML.
   */
  function escapeHtml(text) {
    return String(text || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  /**
   * Carica l'indice JSON generato da Jekyll
   * all'interno di search.md.
   */
  function loadSearchIndex() {
    const indexElement = document.querySelector("#search-index");

    if (!indexElement) {
      return;
    }

    try {
      articles = JSON.parse(indexElement.textContent);

      if (!Array.isArray(articles)) {
        articles = [];
      }
    } catch (error) {
      console.error(
        "Fluente-Mente: impossibile caricare l'indice di ricerca.",
        error
      );

      articles = [];
    }
  }

  /**
   * Aggiorna il messaggio accessibile
   * per gli utenti che utilizzano screen reader.
   */
  function updateStatus(message) {
    if (searchStatus) {
      searchStatus.textContent = message;
    }
  }

  /**
   * Mostra i risultati della ricerca.
   */
  function renderResults(results, query) {
    if (!query) {
      searchResults.innerHTML = "";
      updateStatus("");
      return;
    }

    if (results.length === 0) {
      searchResults.innerHTML = `
        <div class="search-empty">
          <h2>Nessun risultato</h2>
          <p>
            Non abbiamo trovato articoli per
            “${escapeHtml(query)}”.
          </p>
          <p>
            Prova con un'altra parola, un'espressione
            o una situazione.
          </p>
        </div>
      `;

      updateStatus("Nessun risultato trovato.");
      return;
    }

    searchResults.innerHTML = results
      .map(function (article) {
        const rubric = article.rubric_name || article.rubric || "";

        return `
          <article class="search-result-card">

            <a
              class="search-result-link"
              href="${escapeHtml(article.url)}"
            >

              ${
                rubric
                  ? `
                    <span class="search-result-rubric">
                      ${escapeHtml(rubric)}
                    </span>
                  `
                  : ""
              }

              <h2 class="search-result-title">
                ${escapeHtml(article.title)}
              </h2>

              ${
                article.description
                  ? `
                    <p class="search-result-description">
                      ${escapeHtml(article.description)}
                    </p>
                  `
                  : ""
              }

              ${
                article.level
                  ? `
                    <span class="search-result-level">
                      Livello: ${escapeHtml(article.level)}
                    </span>
                  `
                  : ""
              }

            </a>

          </article>
        `;
      })
      .join("");

    updateStatus(
      results.length === 1
        ? "1 risultato trovato."
        : `${results.length} risultati trovati.`
    );
  }

  /**
   * Calcola la rilevanza dei risultati.
   */
  function search(query) {
    const normalizedQuery = normalize(query);

    if (!normalizedQuery) {
      renderResults([], "");
      return;
    }

    const terms = normalizedQuery.split(/\s+/);

    const results = articles
      .map(function (article) {
        const title = normalize(article.title);
        const description = normalize(article.description);
        const rubric = normalize(article.rubric);
        const rubricName = normalize(article.rubric_name);
        const macroTheme = normalize(article.macro_theme);
        const level = normalize(article.level);

        const keywords = Array.isArray(article.keywords)
          ? article.keywords.map(normalize)
          : [];

        const searchableText = [
          title,
          description,
          rubric,
          rubricName,
          macroTheme,
          level,
          keywords.join(" ")
        ].join(" ");

        let score = 0;

        terms.forEach(function (term) {
          if (!term) {
            return;
          }

          // Titolo: priorità massima
          if (title.includes(term)) {
            score += 10;
          }

          // Keyword
          if (
            keywords.some(function (keyword) {
              return keyword.includes(term);
            })
          ) {
            score += 7;
          }

          // Rubrica
          if (
            rubric.includes(term) ||
            rubricName.includes(term)
          ) {
            score += 5;
          }

          // Macro tema
          if (macroTheme.includes(term)) {
            score += 4;
          }

          // Livello
          if (level.includes(term)) {
            score += 2;
          }

          // Descrizione / testo generale
          if (searchableText.includes(term)) {
            score += 1;
          }
        });

        return {
          article: article,
          score: score
        };
      })
      .filter(function (item) {
        return item.score > 0;
      })
      .sort(function (a, b) {
        return b.score - a.score;
      })
      .map(function (item) {
        return item.article;
      });

    renderResults(results, query);
  }

  /**
   * Carica i dati iniziali.
   */
  loadSearchIndex();

  /**
   * Ricerca mentre l'utente digita.
   */
  searchInput.addEventListener("input", function () {
    search(searchInput.value);
  });

  /**
   * ESC:
   * - cancella la ricerca
   * - chiude il campo attivo
   */
  searchInput.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      searchInput.value = "";
      search("");
      searchInput.blur();
    }
  });
});

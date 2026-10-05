/* Enhance the shared HTML catalog; collection and lab order comes from Python. */
(async () => {
  const $ = (id) => document.getElementById(id);
  const fields = {subject: "Subject", niche: "Niche", status: "Status", skill: "Skill", tool: "Tool", goal: "Goal", provider: "Source", type: "Type"};
  const create = (tag, text) => { const node = document.createElement(tag); if (text !== undefined) node.textContent = text; return node; };
  const count = (n) => `${n} lab${n === 1 ? "" : "s"}`;
  try {
    const response = await fetch(document.body.dataset.catalog);
    if (!response.ok) throw new Error("Catalog unavailable");
    const data = await response.json();
    const entries = new Map([...$("work-results").querySelectorAll(".lab")].map((node) => [node.dataset.path, node.cloneNode(true)]));
    const collections = new Map([...$("work-results").querySelectorAll(".collection")].map((node) => {
      const template = node.cloneNode(true); template.querySelector('.labs').replaceChildren();
      return [node.dataset.collection, template];
    }));
    if (data.version !== 1 || data.labs.some((item) => !entries.has(item.path))) throw new Error("Snapshot mismatch");
    const values = (item, key) => key === "subject" ? [item.domain + (item.subdomain ? "/" + item.subdomain : "")] : key === "skill" ? item.skills : key === "tool" ? item.tools : key === "goal" ? item.goals : [item[key]];
    const label = (key, value, item) => key === "subject" ? item.subject_title : key === "provider" ? item.source_name : key === "status" ? data.status_labels[value] : key === "goal" ? data.goals[value] || value : data.labels[value] || value;
    const choices = {};
    for (const [key, title] of Object.entries(fields)) {
      const options = new Map();
      data.labs.forEach((item) => values(item, key).forEach((value) => {
        const option = options.get(value) || {value, title: label(key, value, item), count: 0};
        option.count++; options.set(value, option);
      }));
      choices[key] = [...options.values()].sort((a, b) => a.title.localeCompare(b.title, "en"));
      const group = create("optgroup"); group.label = title;
      choices[key].forEach(({value, title}) => { const option = create("option", title); option.value = JSON.stringify([key, value]); group.append(option); });
      if (options.size) $("filter").append(group);
    }
    const read = () => {
      const params = new URLSearchParams(location.search);
      return {q: params.get("q") || "", sort: params.get("sort") || "order", lab: params.get("lab"), filters: Object.keys(fields).flatMap((key) => params.getAll(key).map((value) => [key, value]))};
    };
    let state = read(), timer, browseFacet = "skill";
    function browseOptions() {
      document.querySelectorAll('[data-facet]').forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.facet === browseFacet)));
      $("browse-search-label").textContent = `Find a ${browseFacet}`;
      $("browse-value-label").textContent = fields[browseFacet];
      const query = $("browse-search").value.toLowerCase().trim();
      const matches = choices[browseFacet].filter((option) => `${option.title} ${option.value}`.toLowerCase().includes(query));
      const placeholder = create('option', matches.length ? `Choose a ${browseFacet}…` : 'No matches'); placeholder.value = '';
      $("browse-value").replaceChildren(placeholder);
      matches.forEach(({value, title, count: n}) => { const option = create('option', `${title} · ${count(n)}`); option.value = value; $("browse-value").append(option); });
      const active = state.filters.find(([key]) => key === browseFacet);
      $("browse-value").value = active && matches.some((option) => option.value === active[1]) ? active[1] : '';
    }
    function render() {
      $("search").value = state.q; $("sort").value = state.sort;
      $("filter").value = state.filters.length === 1 ? JSON.stringify(state.filters[0]) : "";
      const selected = data.labs.filter((item) => (!state.lab || item.path === state.lab) && Object.keys(fields).every((key) => {
        const wanted = state.filters.filter(([facet]) => facet === key).map(([, value]) => value);
        return !wanted.length || wanted.some((value) => values(item, key).includes(value));
      }) && state.q.toLowerCase().split(/\s+/).every((word) => [item.title, item.summary, item.path, item.subject_title, item.source_name, ...item.collection_breadcrumb, ...item.tags, ...item.goals.map((goal) => data.goals[goal] || goal)].join(" ").toLowerCase().includes(word)));
      const active = state.filters.map(([key, value]) => `${fields[key]}: ${choices[key].find((option) => option.value === value)?.title || value}`);
      if (state.lab) active.push(data.labs.find((item) => item.path === state.lab)?.title || "Unknown lab");
      $("result-count").textContent = `${selected.length} of ${data.labs.length} labs` + (active.length ? " · " + active.join("; ") : "");
      $("empty-state").hidden = selected.length !== 0;
      const opened = new Set([...$("work-results").querySelectorAll('.collection[open]')].map((node) => node.dataset.collection));
      const groups = new Map();
      // Filtering preserves the catalog's path order across niches.
      selected.forEach((item) => { if (!groups.has(item.collection_path)) groups.set(item.collection_path, []); groups.get(item.collection_path).push(item); });
      $("work-results").replaceChildren();
      let subject;
      for (const group of groups.values()) {
        const first = group[0], key = first.domain + "/" + (first.subdomain || "");
        if (key !== subject) { $("work-results").append(create("h2", first.subject_title)); subject = key; }
        const collection = collections.get(first.collection_path).cloneNode(true);
        collection.querySelector('.count').textContent = ` · ${count(group.length)}`;
        collection.open = Boolean(state.lab) || opened.has(first.collection_path);
        if (state.sort !== 'order') group.sort((a, b) => (state.sort === "updated" ? b.dates.updated.localeCompare(a.dates.updated) : 0) || a.title.localeCompare(b.title, "en") || a.path.localeCompare(b.path, "en"));
        group.forEach((item) => collection.querySelector('.labs').append(entries.get(item.path).cloneNode(true)));
        $("work-results").append(collection);
      }
      browseOptions();
    }
    function navigate() {
      clearTimeout(timer);
      const params = new URLSearchParams();
      if (state.q) params.set("q", state.q);
      if (state.sort !== "order") params.set("sort", state.sort);
      if (state.lab) params.set("lab", state.lab);
      state.filters.forEach(([key, value]) => params.append(key, value));
      history.pushState(null, "", location.pathname + (params.size ? "?" + params : "")); render();
    }
    render();
    for (const id of ['result-count', 'controls', 'browse-controls']) $(id).hidden = false;
    $("browse-fallback").hidden = true;
    $("controls").addEventListener("submit", (event) => { event.preventDefault(); state.q = $("search").value.trim(); navigate(); });
    $("search").addEventListener("input", () => { clearTimeout(timer); state.q = $("search").value.trim(); timer = setTimeout(navigate, 200); });
    $("filter").addEventListener("change", () => { state.filters = $("filter").value ? [JSON.parse($("filter").value)] : []; state.lab = null; navigate(); });
    $("sort").addEventListener("change", () => { state.sort = $("sort").value; navigate(); });
    $("reset").addEventListener("click", () => { state = {q: "", sort: "order", lab: null, filters: []}; $("browse-search").value = ''; navigate(); });
    window.addEventListener("popstate", () => { clearTimeout(timer); state = read(); render(); });
    document.querySelectorAll('[data-facet]').forEach((button) => button.addEventListener('click', () => { browseFacet = button.dataset.facet; $("browse-search").value = ''; browseOptions(); }));
    $("browse-search").addEventListener('input', browseOptions);
    $("browse-value").addEventListener('change', () => {
      if (!$("browse-value").value) return;
      state.filters = [[browseFacet, $("browse-value").value]]; state.lab = null; state.q = '';
      $("all-labs").open = true; navigate();
    });
  } catch (error) { $("load-warning").hidden = false; }
})();

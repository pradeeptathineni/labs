/* Filter existing HTML; keep the full catalog usable without JavaScript. */
(async () => {
  const $ = (id) => document.getElementById(id);
  const fields = {subject: "Subject", niche: "Niche", status: "Status", skill: "Skill", tool: "Tool", goal: "Goal", provider: "Source", type: "Type"};
  const create = (tag, text) => { const element = document.createElement(tag); if (text !== undefined) element.textContent = text; return element; };
  try {
    const response = await fetch(document.body.dataset.catalog);
    if (!response.ok) throw new Error("Catalog unavailable");
    const data = await response.json();
    const entries = new Map([...$("work-results").querySelectorAll(".lab")].map((item) => [item.dataset.path, item.cloneNode(true)]));
    if (data.version !== 1 || data.labs.some((item) => !entries.has(item.path))) throw new Error("Snapshot mismatch");
    const values = (item, key) => key === "subject" ? [item.domain + (item.subdomain ? "/" + item.subdomain : "")] : key === "skill" ? item.skills : key === "tool" ? item.tools : key === "goal" ? item.goals : [item[key]];
    const label = (key, value, item) => key === "subject" ? item.subject_title : key === "provider" ? item.source_name : key === "status" ? data.status_labels[value] : key === "goal" ? data.goals[value] || value : data.labels[value] || value;
    for (const [key, title] of Object.entries(fields)) {
      const group = create("optgroup"); group.label = title;
      const options = new Map();
      data.labs.forEach((item) => values(item, key).forEach((value) => options.set(value, label(key, value, item))));
      [...options].sort(([a], [b]) => a.localeCompare(b, "en")).forEach(([value, title]) => {
        const option = create("option", title); option.value = JSON.stringify([key, value]); group.append(option);
      });
      if (options.size) $("filter").append(group);
    }
    const read = () => {
      const params = new URLSearchParams(location.search);
      return {q: params.get("q") || "", sort: params.get("sort") || "order", lab: params.get("lab"), filters: Object.keys(fields).flatMap((key) => params.getAll(key).map((value) => [key, value]))};
    };
    let state = read();
    function render() {
      $("search").value = state.q; $("sort").value = state.sort;
      $("filter").value = state.filters.length === 1 ? JSON.stringify(state.filters[0]) : "";
      const selected = data.labs.filter((item) => (!state.lab || item.path === state.lab) && Object.keys(fields).every((key) => {
        const wanted = state.filters.filter(([facet]) => facet === key).map(([, value]) => value);
        return !wanted.length || wanted.some((value) => values(item, key).includes(value));
      }) && state.q.toLowerCase().split(/\s+/).every((word) => [item.title, item.summary, item.path, item.subject_title, item.source_name, ...item.collection_breadcrumb, ...item.skills, ...item.tools, ...item.goals, ...item.goals.map((goal) => data.goals[goal] || goal)].join(" ").toLowerCase().includes(word)));
      $("result-count").textContent = `${selected.length} of ${data.labs.length} labs`;
      $("result-count").hidden = false; $("controls").hidden = false;
      $("empty-state").hidden = selected.length !== 0;
      const groups = new Map();
      selected.forEach((item) => { if (!groups.has(item.collection_path)) groups.set(item.collection_path, []); groups.get(item.collection_path).push(item); });
      $("work-results").replaceChildren();
      let subject;
      const ordered = [...groups.values()].sort((a, b) => (a[0].domain + "/" + (a[0].subdomain || "") + "/" + a[0].collection_path).localeCompare(b[0].domain + "/" + (b[0].subdomain || "") + "/" + b[0].collection_path, "en"));
      for (const group of ordered) {
        const first = group[0], key = first.domain + "/" + (first.subdomain || "");
        if (key !== subject) { $("work-results").append(create("h2", first.subject_title)); subject = key; }
        $("work-results").append(create("h3", `${first.collection_breadcrumb.join(" / ")} (${group.length})`));
        group.sort((a, b) => (state.sort === "updated" ? b.dates.updated.localeCompare(a.dates.updated) : state.sort === "order" && a.order !== null && b.order !== null ? a.order - b.order : 0) || a.title.localeCompare(b.title, "en") || a.path.localeCompare(b.path, "en"));
        const list = create("ul"); list.className = "labs";
        group.forEach((item) => list.append(entries.get(item.path).cloneNode(true)));
        $("work-results").append(list);
      }
    }
    function navigate() {
      const params = new URLSearchParams();
      if (state.q) params.set("q", state.q);
      if (state.sort !== "order") params.set("sort", state.sort);
      if (state.lab) params.set("lab", state.lab);
      state.filters.forEach(([key, value]) => params.append(key, value));
      history.pushState(null, "", location.pathname + (params.size ? "?" + params : "")); render();
    }
    render();
    let timer;
    $("controls").addEventListener("submit", (event) => { event.preventDefault(); clearTimeout(timer); state.q = $("search").value.trim(); navigate(); });
    $("search").addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => { state.q = $("search").value.trim(); navigate(); }, 200); });
    $("filter").addEventListener("change", () => { state.filters = $("filter").value ? [JSON.parse($("filter").value)] : []; state.lab = null; navigate(); });
    $("sort").addEventListener("change", () => { state.sort = $("sort").value; navigate(); });
    $("reset").addEventListener("click", () => { clearTimeout(timer); state = {q: "", sort: "order", lab: null, filters: []}; navigate(); });
    window.addEventListener("popstate", () => { clearTimeout(timer); state = read(); render(); });
  } catch (error) { $("load-warning").hidden = false; }
})();

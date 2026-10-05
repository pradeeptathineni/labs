/* Progressive enhancement: the complete, linked catalog already exists in HTML. */
(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const facets = {
    domain: "Subject", niche: "Niche", status: "Status", subdomain: "Specialization",
    tool: "Tool", goal: "Goal / certification", collection: "Collection", provider: "Source",
    skill: "Skill", type: "Lab type", difficulty: "Difficulty", priority: "Atlas priority"
  };
  let data, state;
  const entries = {work: new Map(), atlas: new Map()};
  document.querySelectorAll(".lab[data-id]").forEach((node) => entries.work.set(node.dataset.id, node.cloneNode(true)));
  document.querySelectorAll(".opportunity[data-id]").forEach((node) => entries.atlas.set(node.dataset.id, node.cloneNode(true)));
  const node = (tag, text, className) => {
    const element = document.createElement(tag);
    if (text !== undefined) element.textContent = text;
    if (className) element.className = className;
    return element;
  };
  const readState = () => {
    const params = new URLSearchParams(location.search);
    const result = {view: params.get("view") || "work", q: params.get("q") || "", sort: params.get("sort") || "order", lab: params.get("lab"), opportunity: params.get("opportunity")};
    Object.keys(facets).forEach((key) => { result[key] = [...new Set(params.getAll(key))]; });
    return result;
  };
  const values = (item, key) => {
    if (key === "tool") return item.tools;
    if (key === "goal") return item.goals;
    if (key === "skill") return item.skills;
    if (key === "collection") return [item.collection_path];
    if (key === "subdomain") return item.subdomain ? [`${item.domain}/${item.subdomain}`] : [];
    return item[key] ? [item[key]] : [];
  };
  const label = (key, value, items) => {
    if (key === "goal") return data.goals[value]?.title || value;
    if (key === "status") return data.status_labels[value] || value;
    const item = items.find((entry) => values(entry, key).includes(value));
    if (key === "provider") return item?.source_name || value;
    if (key === "collection") return item ? `${item.subject_title} · ${item.collection_breadcrumb.join(" / ")}` : value;
    if (key === "subdomain") return item?.subject_title || value;
    return data.labels[value] || value.replaceAll("-", " ").replace(/^./, (letter) => letter.toUpperCase());
  };
  function navigate() {
    const params = new URLSearchParams();
    if (state.view !== "work") params.set("view", state.view);
    if (state.q) params.set("q", state.q);
    if (state.sort !== "order") params.set("sort", state.sort);
    for (const key of ["lab", "opportunity"]) if (state[key]) params.set(key, state[key]);
    Object.keys(facets).forEach((key) => state[key].forEach((value) => params.append(key, value)));
    const query = params.toString();
    history.pushState(null, "", location.pathname + (query ? `?${query}` : ""));
    render();
  }
  function controls(items) {
    const open = new Set([...document.querySelectorAll(".facet[open]")].map((item) => item.dataset.facet));
    $("primary-filters").replaceChildren();
    $("secondary-filters").replaceChildren();
    for (const [key, title] of Object.entries(facets)) {
      if ((state.view === "atlas" && ["status", "skill", "difficulty"].includes(key)) || (state.view !== "atlas" && key === "priority")) continue;
      const candidates = key === "subdomain" && state.domain.length ? items.filter((item) => state.domain.includes(item.domain)) : items;
      const available = [...new Set([...candidates.flatMap((item) => values(item, key)), ...state[key]])].sort((a, b) => label(key, a, items).localeCompare(label(key, b, items), "en"));
      if (!available.length) continue;
      const detail = node("details", undefined, "facet");
      detail.dataset.facet = key;
      detail.open = open.has(key);
      detail.append(node("summary", `${title}${state[key].length ? ` (${state[key].length})` : ""}`));
      const options = node("div", undefined, "facet-options");
      options.setAttribute("role", "group");
      options.setAttribute("aria-label", title);
      for (const value of available) {
        const option = node("label");
        const checkbox = node("input");
        checkbox.type = "checkbox";
        checkbox.value = value;
        checkbox.name = key;
        checkbox.checked = state[key].includes(value);
        checkbox.addEventListener("change", () => {
          state[key] = checkbox.checked ? [...state[key], value] : state[key].filter((item) => item !== value);
          if (key === "domain") {
            const compatible = items.filter((item) => !state.domain.length || state.domain.includes(item.domain)).flatMap((item) => values(item, "subdomain"));
            const oldLength = state.subdomain.length;
            state.subdomain = state.subdomain.filter((item) => compatible.includes(item));
            if (oldLength !== state.subdomain.length) {
              $("load-warning").textContent = "The specialization filter was cleared because it does not belong to the selected subject.";
              $("load-warning").hidden = false;
            }
          }
          navigate();
          // Re-rendered controls retain the keyboard user's point of interaction.
          [...document.querySelectorAll("input[type=checkbox]")].find((input) => input.name === key && input.value === value)?.focus();
        });
        option.append(checkbox, node("span", label(key, value, items)));
        options.append(option);
      }
      detail.append(options);
      $(["domain", "niche", state.view === "atlas" ? "priority" : "status"].includes(key) ? "primary-filters" : "secondary-filters").append(detail);
    }
  }
  function matches(item) {
    if (state.lab && item.id !== state.lab) return false;
    if (state.opportunity && item.id !== state.opportunity) return false;
    if (!Object.keys(facets).every((key) => !state[key].length || state[key].some((value) => values(item, key).includes(value)))) return false;
    const search = [item.title, item.summary, item.deliverable, item.path, item.collection_path, item.source_name, item.subject_title, item.niche,
      ...item.collection_breadcrumb, ...item.skills, ...item.tools, ...item.goals, ...item.goals.map((goal) => data.goals[goal]?.title || goal)].filter(Boolean).join(" ").toLocaleLowerCase("en");
    return state.q.toLocaleLowerCase("en").split(/\s+/).filter(Boolean).every((term) => search.includes(term));
  }
  function sorted(items) {
    return [...items].sort((a, b) => {
      if (state.sort === "updated") {
        const difference = (b.dates?.updated || b.checked_on || "").localeCompare(a.dates?.updated || a.checked_on || "", "en");
        if (difference) return difference;
      }
      if (state.sort === "order" && a.order !== null && a.order !== undefined && b.order !== null && b.order !== undefined && a.order !== b.order) return a.order - b.order;
      return a.title.localeCompare(b.title, "en") || a.id.localeCompare(b.id, "en");
    });
  }
  function render() {
    const view = state.view === "atlas" ? "atlas" : "work";
    const items = view === "atlas" ? data.opportunities : data.labs;
    const filtered = ["work", "atlas"].includes(state.view) && ["order", "updated", "title"].includes(state.sort) ? items.filter(matches) : [];
    $("work-results").hidden = view === "atlas";
    $("atlas-fallback").hidden = view !== "atlas";
    $("controls").hidden = false;
    $("search").value = state.q;
    $("sort").value = state.sort;
    $("sort").options[1].textContent = view === "atlas" ? "Evidence review date" : "Last content update";
    document.querySelectorAll(".view-nav a").forEach((link) => {
      if (link.dataset.view === view) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
    });
    $("view-title").textContent = view === "atlas" ? "Directions worth exploring." : "A place for each problem.";
    $("view-description").textContent = view === "atlas" ? "Reviewed sources, meaningful units and proposed destinations. These are choices, not accomplishments. Next marks the current Kubernetes focus; later and explore keep other interests visible." : "Browse by subject, with related kinds of work together. Open a collection to find its exercises. Skills are targets; goals describe preparation.";
    controls(items);
    $("result-count").textContent = `${filtered.length} of ${items.length} ${view === "atlas" ? "opportunities" : "adopted labs"}`;
    $("active-filters").replaceChildren();
    const active = (text, clear) => {
      const button = node("button", `${text} ×`);
      button.type = "button";
      button.setAttribute("aria-label", `Remove ${text}`);
      button.addEventListener("click", () => { clear(); navigate(); $("reset").focus(); });
      $("active-filters").append(button);
    };
    if (state.q) active(`Search: ${state.q}`, () => { state.q = ""; });
    for (const key of ["lab", "opportunity"]) if (state[key]) active(`${key}: ${state[key]}`, () => { state[key] = null; });
    for (const [key, title] of Object.entries(facets)) for (const value of state[key]) active(`${title}: ${label(key, value, items)}`, () => { state[key] = state[key].filter((item) => item !== value); });
    const container = $(view === "atlas" ? "atlas-results" : "work-results");
    const opened = new Set([...container.querySelectorAll(".collection[open]")].map((element) => element.dataset.collection));
    container.replaceChildren();
    const subjects = new Map();
    filtered.forEach((item) => {
      const key = `${item.domain}/${item.subdomain || ""}`;
      if (!subjects.has(key)) subjects.set(key, new Map());
      const groups = subjects.get(key);
      if (!groups.has(item.collection_path)) groups.set(item.collection_path, []);
      groups.get(item.collection_path).push(item);
    });
    const filteredView = Boolean(state.q || state.lab || state.opportunity || Object.keys(facets).some((key) => state[key].length));
    for (const [, groups] of [...subjects].sort(([a], [b]) => a.localeCompare(b, "en"))) {
      const section = node("section", undefined, "subject");
      section.append(node("h2", [...groups.values()][0][0].subject_title));
      [...groups].sort(([a], [b]) => a.localeCompare(b, "en")).forEach(([path, group], index) => {
        const collection = node("details", undefined, "collection");
        collection.dataset.collection = path;
        collection.open = filteredView || opened.has(path) || index === 0;
        const heading = node("summary");
        heading.append(node("span", group[0].collection_breadcrumb.join(" / ")), node("span", `${group.length} ${view === "work" ? "labs" : "opportunities"}`, "count"));
        const body = node("div", undefined, "entries");
        sorted(group).forEach((item) => body.append(entries[view].get(item.id).cloneNode(true)));
        collection.append(heading, body);
        section.append(collection);
      });
      container.append(section);
    }
    $("empty-state").hidden = filtered.length !== 0;
  }
  async function start() {
    try {
      const response = await fetch(document.body.dataset.catalog);
      if (!response.ok) throw new Error("Catalog response unavailable");
      data = await response.json();
      if (data.version !== 1 || data.labs.some((item) => !entries.work.has(item.id)) || data.opportunities.some((item) => !entries.atlas.has(item.id))) throw new Error("Catalog snapshot mismatch");
      state = readState();
      render();
      $("controls").addEventListener("submit", (event) => { event.preventDefault(); state.q = $("search").value.trim(); navigate(); });
      let searchTimer;
      $("search").addEventListener("input", () => { clearTimeout(searchTimer); searchTimer = setTimeout(() => { state.q = $("search").value.trim(); navigate(); }, 250); });
      $("sort").addEventListener("change", () => { state.sort = $("sort").value; navigate(); });
      $("reset").addEventListener("click", () => {
        clearTimeout(searchTimer);
        const view = state.view;
        state = {view, q: "", sort: "order", lab: null, opportunity: null};
        Object.keys(facets).forEach((key) => { state[key] = []; });
        $("load-warning").hidden = true;
        navigate();
      });
      document.querySelectorAll(".view-nav a").forEach((link) => link.addEventListener("click", (event) => {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        clearTimeout(searchTimer);
        state.view = link.dataset.view;
        state.lab = null; state.opportunity = null;
        ["status", "priority", "difficulty", "skill"].forEach((key) => { state[key] = []; });
        navigate();
      }));
      window.addEventListener("popstate", () => { clearTimeout(searchTimer); state = readState(); render(); });
    } catch (error) {
      $("load-warning").textContent = "Search and filters could not load. The full linked catalog and atlas remain available below. Reload to try again.";
      $("load-warning").hidden = false;
    }
  }
  start();
})();

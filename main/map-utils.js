// === drawNpop: Updates markers based on selected week usage ===
function drawNpop(week) {
  currentNpopLayer.clearLayers();
  rows.forEach(row => {
    const usage = parseFloat(row[`% Used: ${week}`]);
    const lat = parseFloat(row.Lat);
    const lon = parseFloat(row.Lon);
    if (!isNaN(lat) && !isNaN(lon)) {
      const marker = L.circleMarker([lat, lon], {
        radius: 8,
        color: usage >= 80 ? '#d73027' : usage >= 50 ? '#fc8d59' : '#91cf60',
        weight: 1,
        fillOpacity: 0.8,
        props: row
      });
      const popupContent = generatePopupHTML(row, week);
      marker.bindPopup(popupContent);
      currentNpopLayer.addLayer(marker);
    }
  });
}

// === filterMarkersByWeek: Optional opacity styling for device/address layers ===
function filterMarkersByWeek(weekKey) {
  if (!weekKey) return;

  // Device-level filtering
  currentDeviceLayer.eachLayer(marker => {
    const usage = parseFloat(marker.options.props?.[weekKey]);
    marker.setOpacity(!isNaN(usage) ? (usage > 80 ? 1 : 0.3) : 0);
  });

  // Address-level filtering
  addressLayer.eachLayer(marker => {
    const usage = parseFloat(marker.options.props?.[weekKey]);
    marker.setOpacity(!isNaN(usage) ? (usage > 80 ? 1 : 0.3) : 0);
  });
}

// === performSearch: Zooms and highlights marker by user input ===
function performSearch() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const query = searchInput.value.trim().toLowerCase();
  if (!query) return;

  let found = false;
  const match = rows.find(r => (r[mode] || '').toString().toLowerCase() === query);

  if (match && match.Lat && match.Lon) {
    const lat = parseFloat(match.Lat);
    const lon = parseFloat(match.Lon);
    if (!isNaN(lat) && !isNaN(lon)) {
      found = true;
      map.setView([lat, lon], 16, { animate: true });

      let targetMarker = null;
      currentNpopLayer.eachLayer(marker => {
        const val = (marker.options?.props?.[mode] || '').toString().toLowerCase();
        if (val === query) targetMarker = marker;
      });

      if (targetMarker) {
        targetMarker.openPopup();
        // Optionally add highlight ring
      }
    }
  }

  if (!found) {
    alert(`No match for "${searchInput.value}" in ${mode}`);
  }
}

// === DOMContentLoaded: Week selector + redraw logic ===
document.addEventListener("DOMContentLoaded", function () {
  const weekSelector = document.getElementById("weekSelector");
  if (!weekSelector || !rows || rows.length === 0) return;

  const weekKeys = Object.keys(rows[0]).filter(k => k.startsWith("% Used:"));
  weekKeys.forEach(week => {
    const opt = document.createElement("option");
    opt.value = week;
    opt.textContent = week.replace("% Used: ", "");
    weekSelector.appendChild(opt);
  });

  // Initial draw
  if (weekKeys.length > 0) {
    weekSelector.value = weekKeys[0];
    drawNpop(weekKeys[0].replace("% Used: ", ""));
  }

  // On change, redraw markers
  weekSelector.addEventListener("change", function () {
    const selectedWeek = weekSelector.value;
    drawNpop(selectedWeek.replace("% Used: ", ""));
    // filterMarkersByWeek(selectedWeek); // Optional if you're using address/device layers
  });
});


// === performSearch: Zooms and highlights marker by user input ===
function performSearch() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const query = searchInput.value.trim().toLowerCase();
  if (!query) return;

  let found = false;
  const match = rows.find(r => (r[mode] || '').toString().toLowerCase() === query);

  if (match && match.Lat && match.Lon) {
    const lat = parseFloat(match.Lat);
    const lon = parseFloat(match.Lon);
    if (!isNaN(lat) && !isNaN(lon)) {
      found = true;
      map.setView([lat, lon], 16, { animate: true });

      let targetMarker = null;
      currentNpopLayer.eachLayer(marker => {
        const val = (marker.options?.props?.[mode] || '').toString().toLowerCase();
        if (val === query) targetMarker = marker;
      });

      if (targetMarker) {
        targetMarker.openPopup();
        // Optional: Add highlight ring
      }
    }
  }

  if (!found) {
    alert(`No match for "${searchInput.value}" in ${mode}`);
  }
}

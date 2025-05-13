# 🗺️ Interactive Map

- Uses **Leaflet** with OpenStreetMap base layer + Satellite imagery option  
- Supports **zooming**, **panning**, and **layer toggling**

---

## 👤 Author

- **Name:** [Kristie Hu](https://www.kristiehu.com/) - [Github](https://github.com/Kristiehu)
- **Version:** 1.0.0
- **Date:** 2025-05-13
  
---


## 📊 Data Visualization

- **CSV Data Loading** via [PapaParse](https://www.papaparse.com/)
- **Marker Clustering** using `Leaflet.markercluster`
- **Heatmap Layer** using `Leaflet.heat`
  - Toggles visibility based on **zoom level**
  - Custom **gradient colors** for intensity
- **Shapefile Integration** using `shp.js`
  - Loads **FSA (Forward Sortation Area)** boundaries for Ontario & Quebec
  - Displays **metadata on hover**

---

## 🧩 UI Controls

### 📝 Title & Report Box
- Shows total count of **"npop"** points

### 🔍 Filtering System
- Text input with **autocomplete** (`<datalist>`)
- Clears filter with "×" button

### 🗂️ Layer Controls
- Toggle between **OSM/Satellite** base layers
- Toggle **FSA layers** and **building overlays**

---

## 🧭 Interactive Elements

- **Marker Popups** – Displays name/address on click  
- **FSA Hover Effects** – Highlights boundaries & shows metadata  
- **Building Click Events** – Shows details (name, ID, description)

---

## ⚙️ Dynamic Behaviors

- **Zoom-Based Layer Management**
  - Heatmap hides beyond zoom level **13**
  - FSA layers hide beyond zoom level **17**

- **Filtering Logic**
  - Updates **markers/heatmap in real time**
  - Resets **map view when cleared**

---

## 🎨 Styling & UX

- Custom-styled **report boxes** with hover effects  
- Responsive **full-screen layout**

---

## 📚 External Libraries Used

- [Leaflet](https://leafletjs.com/) – Core mapping  
- [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster) – Grouping markers  
- [Leaflet.heat](https://github.com/Leaflet/Leaflet.heat) – Heatmap visualization  
- [PapaParse](https://www.papaparse.com/) – CSV parsing  
- [shp.js](https://github.com/calvinmetcalf/shapefile-js) – Shapefile loading  
- [Leaflet-search](https://github.com/stefanocudini/leaflet-search) – Search functionality (not fully implemented)

---

> This creates a **geospatial dashboard** for visualizing **"npop"** data with filtering, clustering, heatmaps, and boundary overlays.


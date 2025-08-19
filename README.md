# 🗺️ Interactive Geospatial Dashboard

A **Leaflet-based web mapping tool** for exploring **NPOP data** with clustering, heatmaps, and dynamic filtering.  
Includes additional dashboards for device capacity reporting and device information tracking.  

---

## 🌍 Live Applications

- **[NPOP Map](https://kristiehu.github.io/Leaflet-Npop-Map/main/)**  
  Explore clustered markers, heatmaps, and FSA overlays.  
  [![NPOP Map Preview](https://raw.githubusercontent.com/kristiehu/Leaflet-Npop-Map/main/Npop_heatmap_preview.png)](https://kristiehu.github.io/Leaflet-Npop-Map/main)

- **[Device Capacity Reporting Dashboard](https://kristiehu.github.io/Leaflet-Npop-Map/main/capacityReport.html)**  
  Visualize port and capacity usage across devices.  
  [![Capacity Report Preview](https://raw.githubusercontent.com/kristiehu/Leaflet-Npop-Map/main/Port_capacity_preview.png)](https://kristiehu.github.io/Leaflet-Npop-Map/main/capacityReport.html)

- **[Device Info Tracker](https://kristiehu.github.io/Leaflet-Npop-Map/main/devices_only.html)**  
  Browse and search detailed device information.  
  [![Device Info Preview](https://raw.githubusercontent.com/kristiehu/Leaflet-Npop-Map/main/Npop_devices_preview.png)](https://kristiehu.github.io/Leaflet-Npop-Map/main/devices_only.html)

---

## 🧩 Key Features

### 📊 UI & Controls
- **Title & Report Box** showing total NPOP counts  
- **Text search with autocomplete** + clear filter option  
- **Layer controls** for toggling OSM/Satellite basemaps, FSAs, and building overlays  

### 🧭 Interactive Map Elements
- **Marker popups** with name & address  
- **FSA hover highlights** with metadata  
- **Building click events** showing details (name, ID, description)  

### ⚙️ Dynamic Behaviors
- **Zoom-based visibility**  
  - Heatmap hides beyond zoom **13**  
  - FSA layers hide beyond zoom **17**  
- **Real-time filtering** updates markers/heatmaps and resets view  

### 🎨 Styling & UX
- Custom-styled **report boxes with hover effects**  
- Responsive **full-screen map layout**  

---

## 📚 Technology Stack

- [Leaflet](https://leafletjs.com/) – Interactive maps  
- [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster) – Marker clustering  
- [Leaflet.heat](https://github.com/Leaflet/Leaflet.heat) – Heatmaps  
- [PapaParse](https://www.papaparse.com/) – CSV parsing  
- [shp.js](https://github.com/calvinmetcalf/shapefile-js) – Shapefile loading  
- [Leaflet-search](https://github.com/stefanocudini/leaflet-search) – Search functionality (beta)  

---

## 👤 Author

- **Kristie Hu**  
  🌐 [Website](https://www.kristiehu.com/) · 💻 [GitHub](https://github.com/Kristiehu)  
- **Version:** 1.0.0  
- **Date:** 2025-05-20  

---

> 🚀 This project provides a **geospatial dashboard** for exploring NPOP data, capacity usage, and device information through interactive, scalable, and user-friendly web maps.

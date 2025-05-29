
// === generatePopupHTML: Formats popup content for markers ===
function generatePopupHTML(row, week) {
  const usage = row[`% Used: ${week}`] || '—';
  const dev = row['Device Count'] || '0';
  const addr = row['Address'] || '—';
  const fsa = row['FSA'] || '—';
  const city = row['City'] || '—';
  const id = row['Entity ID'] || '—';

  return \`
    <div class="popup-group">
      <div class="device-entry">
        <h4>\${addr}</h4>
        <p><strong>City:</strong> \${city}<br/>
           <strong>FSA:</strong> \${fsa}<br/>
           <strong>Device Count:</strong> \${dev}<br/>
           <strong>Usage:</strong> \${usage}</p>
        <hr/>
        <p><strong>Entity ID:</strong> \${id}</p>
      </div>
    </div>
  \`;
}

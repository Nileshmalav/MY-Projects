var platform = new H.service.Platform({
  apikey: "YzIWnSOsn4xrV-DU3fLh_0ejruqmT0bOiIQvSnWaf2s"
});

function getDistance(lt1, lg1, lt2, lg2) {
  let a = new H.map.Marker({ lat: lt1, lng: lg1 })
  let b = new H.map.Marker({ lat: lt2, lng: lg2 })
  d = a.getGeometry().distance(b.getGeometry())
  d =  (d / 1609.33999997549).toFixed(2) + " miles "
  return d
}

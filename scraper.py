from dc_base_scrapers.arcgis_scraper import ArcGisScraper


stations_url = "https://maps.dover.gov.uk/arcgis/rest/services/Open_Data/Polling_Stations/MapServer/0/query?where=OID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&queryByDistance=&returnExtentsOnly=false&datumTransformation=&parameterValues=&rangeValues=&f=pjson"
districts_url = "https://maps.dover.gov.uk/arcgis/rest/services/Open_Data/Polling_Boundaries/MapServer/0/query?where=OID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&queryByDistance=&returnExtentsOnly=false&datumTransformation=&parameterValues=&rangeValues=&f=pjson"
council_id = "DOV"


stations_scraper = ArcGisScraper(
    stations_url, council_id, "utf-8", "stations", key="OID"
)
stations_scraper.scrape()
districts_scraper = ArcGisScraper(
    districts_url, council_id, "utf-8", "districts", key="OID"
)
districts_scraper.scrape()

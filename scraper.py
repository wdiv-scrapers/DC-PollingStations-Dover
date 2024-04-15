from dc_base_scrapers.arcgis_scraper import ArcGisScraper

root_url = "https://services-eu1.arcgis.com/xk4RA36G57mVH7Aw/ArcGIS/rest/services"
stations_url = ("{root_url}/Polling_Stations_points_Open_Data/FeatureServer/0/query?"
                 "where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope"
                 "&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true"
                 "&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false"
                 "&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false"
                 "&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount="
                 "&queryByDistance=&returnExtentsOnly=false&datumTransformation=&parameterValues=&rangeValues="
                 "&f=pjson").format(root_url=root_url)
districts_url = ("{root_url}/Polling_Boundaries_Open_Data/FeatureServer/0/query?"
                 "where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope"
                 "&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true"
                 "&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false"
                 "&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false"
                 "&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount="
                 "&queryByDistance=&returnExtentsOnly=false&datumTransformation=&parameterValues=&rangeValues="
                 "&f=pjson").format(root_url=root_url)
council_id = "DOV"


stations_scraper = ArcGisScraper(
    stations_url, council_id, "utf-8", "stations", key="OBJECTID"
)
stations_scraper.scrape()
districts_scraper = ArcGisScraper(
    districts_url, council_id, "utf-8", "districts", key="OBJECTID"
)
districts_scraper.scrape()

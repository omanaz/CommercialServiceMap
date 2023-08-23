import os
import json

def amalgamate_geojsons(list_of_strings, name, url,state_code):
    feature_collection = {
        "type": "FeatureCollection",
        "features": []
    }
    counties_list = []
    list_of_strings = list_of_strings.split(',')
    for file_name in os.listdir('./national_map/USA/'+state_code):
        if file_name.endswith('.geo.json') and file_name[:-9] in list_of_strings:
            with open('./national_map/USA/'+state_code+'/'+file_name) as f:
                counties_list.append(file_name[:-9])
                data = json.load(f)
                for feature in data['features']:
                    # Set the name for all features
                    feature['properties']['name'] = name
                    # Add hyperlink to URL
                    feature['properties']['url'] = url
                feature_collection["features"].extend(data["features"])
    if " " in name:
        name = name.replace(' ','')
    print('counties',counties_list)
    print(f'const {name} = {feature_collection};L.geoJSON({name},'+'{style:{fillOpacity: 0.6,stroke: false},onEachFeature: function(feature, layer) {layer.bindPopup(`<a href="${feature.properties.url}">${feature.properties.name}</a>`);}}).addTo(mymap);')

full_states = ['AL', 'AK', 'AR', 'CO', 'CT','HI','ID','IN','LA','ME','MD','MS','MT','NE','NH','ND','PR','RI','SD','UT','VT','WI' ]

counties = "Oakland,Saginaw,Cheboygan,Gogebic,Ontonagon,Otsego,Iron,Houghton,Keweenaw,Baraga,Marquette,Dickinson,Sanilac,Macomb,St. Clair,Lapeer,Tuscola,Oscoda,Ogemaw,Huron,Genesee,Bay,Midland,Gladwin,Arenac,Iosco,Alcona,Alpena,Presque Isle,Emmet,Montmorency,Shiawassee,Menominee,Delta,Alger,Schoolcraft,Luce,Mackinac,Chippewa"
out = "pontiac"
url = 'https://trade.gov/pontiac-contact-us'
out = out.capitalize()
state_code = 'MI'
amalgamate_geojsons(counties,out,url,state_code)


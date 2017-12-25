<template>
    <baidu-map style="height: 100%; width: 100%"
               :center="center"
               :zoom="zoom"
               @ready="handler"
               :scroll-wheel-zoom="true">

      <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
      <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
      <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" @locationSuccess="location_success" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
    </baidu-map>
</template>
<script>
  export default {
    data () {
      return {
        center: {lng: 0, lat: 0},
        zoom: 3,
        BMap: null,
        map: null,
      }
    },
    methods: {
      handler ({BMap, map}) {
        console.log(BMap, map)
        this.BMap = BMap
        this.map = map

        this.zoom = 15

        this.center.lng = 100.53063501
        this.center.lat = 29.54460611

        var point = new BMap.Point(106.53063501, 29.54460611);
        var marker = new BMap.Marker(point);
        map.addOverlay(marker)

      },
      location_success(point, AddressComponent, marker){
        console.log("location_success")
        var geolocation = new BMap.Geolocation();
        geolocation.getCurrentPosition(function(r){
          if(this.getStatus() == BMAP_STATUS_SUCCESS){
            var mk = new BMap.Marker(r.point);
            map.addOverlay(mk);
            map.panTo(r.point);
            alert('您的位置：'+r.point.lng+','+r.point.lat);
          }
          else {
            alert('failed'+this.getStatus());
          }
        });
      }
    }
  }
</script>

<style scoped="">
  .map{
    width: 100%;
    height: 100%;
  }
</style>

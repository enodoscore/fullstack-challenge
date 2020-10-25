<template>
<div>
<h2>Find and select multi-family properties</h2>
<div style="margin: 50px">
<el-row class="autocomplete">
  <el-col style="width: 100%">
    <el-autocomplete
      v-model="searchQuery"
      :fetch-suggestions="querySearch"
      placeholder="Search for class or addreess."
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>
</el-row>
</div>
</div>
</template>

<script>
import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
export default {
  data() {return {searchQuery: '', rows:{}}},
  methods: {
    querySearch(queryString, cb) {
       fetch("http://localhost:5000/api/get_autocomplete_values/" + queryString)
       .then(resp => {
                   if(resp.ok) {
                      return resp.json()
                   } else {
                      alert("Failed to get selected properties. Error: " + resp.status + " - " + resp.statusText) }})
       .then(resp => {
          //this.rows.value = resp.properties;
          this.rows = this.prepRows(resp.properties);
          cb(this.rows);
       });
    },
    prepRows(properties){
        let prepped = []
        properties.forEach(p => {
           prepped.push({'value': p[1] + " " + p[2]});
        })
        return prepped
    },
    handleSelect(item){
        fetch("http://localhost:5000/api/set_selected/" + item);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

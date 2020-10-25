<template>
<div>
<el-table
  :data="selectedProperties"
  stripe
  style="width: 100%"
>
  <el-table-column
    prop="index"
    label="Index">
  </el-table-column>
  <el-table-column
    prop="classDescription"
    label="Class Description">
  </el-table-column>
  <el-table-column
    prop="fullAddress"
    label="Full Address">
  </el-table-column>
  <td><button v-on:click="deleteSelected(prop.index)" type="button">Delete</button></td>
</el-table>
</div>
</template>

<script>
import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
export default {
  data () {return {selectedProperties: []}},
  methods: {
    getSelectedProperties() {
        fetch("http://localhost:5000/api/selected_properties")
        .then(resp => {
                   if(resp.ok) {
                      return resp.json()
                   } else {
                      alert("Failed to get selected properties. Error: " + resp.status + " - " + resp.statusText) }})
        .then(resp => {
                   resp.properties.forEach(p => {
                   const prop = {
                         index:p[0],
                         classDescription:p[1],
                         fullAddress:p[2]
                   };
                   this.selectedProperties.push(prop)})
        });
    },
    deleteSelected(item){
        fetch("http://localhost:5000/api/unset_selected/" + item, {mode:'no-cors'})
        .then(resp => {if(resp.ok) { return resp }})
        .then(() => {
                   this.selectedProperties = []
                   this.getSelectedProperties()
        })
    },
    handleSelect(){
        this.getSelectedProperties()
    }
  },
  mounted() {
    this.getSelectedProperties()
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

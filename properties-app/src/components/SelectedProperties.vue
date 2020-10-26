<template>
<div>
<el-table
  :data="selectedProperties"
  stripe
  style="width: 100%"
>
<div slot="empty"></div>
  <el-table-column
    prop="index"
    label="Index"
    width="100"
  >
  </el-table-column>
  <el-table-column
    prop="classDescription"
    label="Class Description"
    >
  </el-table-column>
  <el-table-column
    prop="fullAddress"
    label="Full Address">
  </el-table-column>
  <el-table-column width="100">
    label="Delete"
    <template slot-scope="scope">
      <el-button size="mini"
                 @click="deleteSelected(scope.row.index)">Delete</el-button>
    </template>
  </el-table-column>
</el-table>
</div>
</template>

<script>
import eventBus from '../event-bus.js'

export default {
  data () {return {selectedProperties: []}},
  methods: {
    getSelectedProperties() {
      this.selectedProperties = [];
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
    eventBus.$on('fireSelectedProperties', () => {
      this.getSelectedProperties()
    });
  },
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

<template>
<div>
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Class Description</th>
      <th scope="col">Full Address</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="prop in selectedProperties" v-bind:key="prop.index">
      <td>{{prop.index}}</td>
      <td>{{prop.classDescription}}</td>
      <td>{{prop.fullAddress}}</td>
      <td><button v-on:click="deleteSelected(prop.index)" type="button">Delete</button></td>
    </tr>
  </tbody>
</table>
</div>
</template>

<script>

export default {
  data () {return {index: '', classDescription: '', fullAddress: '', selectedProperties: []}},
  methods: {
    getSelectedProperties() {
        fetch("http://localhost:5000/data/selected_properties")
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
        fetch("http://localhost:5000/data/unset_selected/" + item, {mode:'no-cors'})
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

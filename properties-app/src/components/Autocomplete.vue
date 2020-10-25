<template>
<div>
<el-row class="autocomplete">
  <el-col :span="12">
    <div class="sub-title">Find multi-family properties.</div>
    <el-autocomplete
      class="inline-input"
      v-model="row"
      :fetch-suggestions="querySearch"
      placeholder="Please Input"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>
</el-row>
</div>
</template>

<script>

export default {
  data() {return {row:''}},
  methods: {
    querySearch(queryString) {
        fetch("http://localhost:5000/data/get_autocomplete_values/" + queryString).then(resp => {if(resp.ok){ return resp.json() } else { alert("Failed to get properties. Error: " + resp.status + " - " + resp.statusText) }});
    },
    handleSelect(item){
        fetch("http://localhost:5000/data/set_selected/" + item);
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

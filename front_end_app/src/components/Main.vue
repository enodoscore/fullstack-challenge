<template>
  <div>
    <el-row>
      <el-col :span="24">
        <div class="sub-title">Search for Properties by Address</div>
        <el-autocomplete
          size="large"
          v-model="input"
          :fetch-suggestions="querySearch"
          placeholder="Please Input"
          :trigger-on-focus="false"
          @select="handleSelect"
        ></el-autocomplete>
      </el-col>
    </el-row>
    <div v-if="selected.length >0">
      <div class="class">
        <SelectedTable :selected="selected" @resetSearch="resetSearch" />
      </div>
    </div>
  </div>
</template>

<script>
import SelectedTable from "./SelectedTable.vue";
import { apiGet } from "../apiBase/apiRequest";

export default {
  name: "Main",

  components: {
    SelectedTable: SelectedTable
  },

  data() {
    return {
      links: [],
      input: "",
      selected: [],
      results: []
    };
  },

  methods: {
    querySearch(queryString, callBack) {
      var results = this.fetchResultsFromApi(queryString)
      // call callback function to return suggestions
      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        callBack(results);
      }, 3000 * Math.random());
    },

    fetchResultsFromApi(queryString) {
      try {
        const data = apiGet(`search?search=${queryString}`, {});
        data.then(res => {
          this.results = res
        });
      } catch (err) {
        return null;
      }
      return this.updateResults()
    },

    updateResults() {
      return this.results.map((res) => Object.assign(res, { value: res.full_address }))
    },

    handleSelect(item) {

      if(this.selected.length > 0) { return }

      try {
        const data = apiGet(`${item.id}/update?info=${this.toogleSelected(item)}`, { method: "PATCH" });
        data.then(() => {
          this.selected.push(Object.assign(item, { selected: 1 }))
          this.handleNotification("You have selected this property!");
        });
      } catch (err) {
        return null;
      }
    },
  
    resetSearch(item) {
      this.handleUnselected(item)
    },

    handleUnselected(item) {
      try {
        const data = apiGet(`${item.id}/update?info=${this.toogleSelected(item)}`, { method: "PATCH" });
        data.then(() => {
          this.selected = [];
          this.results = [] 
          this.input = "" ;
          this.handleNotification("You have unselected this property!");
        });
      } catch (err) {
        console.log(err)
        return null;
      }
    },

    handleNotification(message) {
      this.$notify({
        title: "Success",
        message: `${message}`,
        type: "success",
        showClose: false,
        duration: 1500
      });
    },

    toogleSelected(item) {
      return item.selected === 1 ? 0 : 1
    }
  }
};
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

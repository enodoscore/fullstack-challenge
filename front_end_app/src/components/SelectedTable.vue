<template>
  <div class="data-table">
    <el-table :data="selected">
      <el-table-column prop="full_address" label="Address" width="300"></el-table-column>
      <el-table-column prop="zip" label="Zip" width="120"></el-table-column>
      <el-table-column prop="description" label="Description" width="500"></el-table-column>
      <el-table-column label="Operations" width="120">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="unselect(scope.$index, selected)"
            type="danger"
            size="medium"
          >Unselect</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "SelectedTable",
  
  methods: {
    unselect(index, rows) {
      let item = rows[index]
      rows.splice(index, 1);
      this.resetSearch(item)
    },

    resetSearch(item) {
      this.$emit("resetSearch", item)
    }
  },

  props: {
    selected: {
      Array,
      required: true
    }
  }
};
</script>

<style scoped>
.data-table {
  margin-left: 15%
}
</style>>
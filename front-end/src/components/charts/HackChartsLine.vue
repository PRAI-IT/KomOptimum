<template lang="pug">
LineChart.chartBlock(:chartData="$props.chartData" :options="options")
</template>

<script>
import { LineChart } from 'vue-chart-3';
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);
export default {
	components: { LineChart },
	props:{
		chartData:Object
	},
	data(){
		return{
			options:{
				plugins: {
					legend: {
						display: false
					}
				}
			}
		}
	}
}
</script>

<style scoped>
	.chartBlock{
		width: 100%;
		height: 200px;
	}
</style>
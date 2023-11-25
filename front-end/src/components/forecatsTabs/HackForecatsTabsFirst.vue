<template lang="pug">
.title Прогноз коммунальных платежей
.tabList
	.myTabSmall(:class="{'myTabActiveSmall':firstTabs === 0}" @click="firstTabs = 0") 2022
	.myTabSmall(:class="{'myTabActiveSmall':firstTabs === 1}" @click="firstTabs = 1") 2023
	.myTabSmall(:class="{'myTabActiveSmall':firstTabs === 2}" @click="firstTabs = 2") 2024
	.myTabSmall(:class="{'myTabActiveSmall':firstTabs === 3}" @click="firstTabs = 3") 3 года
.listCheckbox
	label.formCheck С учётом погоды
		input(type="checkbox" v-model="weather")
		.checkmark(style="--custom_color:#5570F1")
	label.formCheck С учётом ремонта
		input(type="checkbox" v-model="repair")
		.checkmark(style="--custom_color:#5570F1")
.scrolledBlock
	.blockTable
		.subTitle Прогноз цены по месяцам
		.rowForecatsMonth.blackRow
			div
			div(v-for="month in arrMonth") {{month}}
			div Общая сумма
		.rowForecatsMonth
			div Вода
			div 234
			div 312
			div 450
			div 400
			div 396
			div 415
			div 612
			div 250
			div 199
			div 376
			div 422
			div 322
			div 4 388
		.rowForecatsMonth
			div Свет
			div 1234
			div 1312
			div 1450
			div 1400
			div 1396
			div 1415
			div 1612
			div 1250
			div 1199
			div 1376
			div 1422
			div 1322
			div 16 388
		.rowForecatsMonth
			div Газ
			div 2234
			div 2312
			div 2450
			div 2400
			div 2396
			div 2415
			div 2612
			div 2250
			div 2199
			div 2376
			div 2422
			div 2322
			div 28 388
		.rowForecatsMonth
			div Тепло
			div 3234
			div 3312
			div 0
			div 0
			div 0
			div 0
			div 0
			div 0
			div 0
			div 0
			div 3422
			div 3322
			div 13 290
			div
.listCheckbox.additionMargin
	label.formCheck Вода
		input(type="checkbox" v-model="form.water")
		.checkmark(:style="`--custom_color:${arrColor[0]}`")
	label.formCheck Свет
		input(type="checkbox" v-model="form.light")
		.checkmark(:style="`--custom_color:${arrColor[1]}`")
	label.formCheck Газ
		input(type="checkbox" v-model="form.gas")
		.checkmark(:style="`--custom_color:${arrColor[2]}`")
	label.formCheck Тепло
		input(type="checkbox" v-model="form.teplo")
		.checkmark(:style="`--custom_color:${arrColor[3]}`")
HackChartsLine(:chartData="chartData")
</template>

<script>
import HackChartsLine from "@/components/charts/HackChartsLine.vue";

export default {
	components: {HackChartsLine},
	data(){
		return{
			arrMonth:['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Ноябрь','Декабрь'],

			firstTabs:0,
			weather:false,
			repair:false,

			form:{
				water:true,
				light:true,
				gas:false,
				teplo:false
			},

			arrColor:['#5570F1','#FFC357','#FE8084','#2DC8A8'],
			chartData:{
				labels: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Ноябрь','Декабрь'],
				datasets:  [
					{label: 'My First Dataset',
						data: [65, 59, 80, 81, 56, 55, 40, 65, 59, 80, 81, 56],
						fill: false,
						borderColor: '#5570F1',
						tension: 0.1},
					{label: 'My Second Dataset',
						data: [25, 39, 40, 51, 16, 85, 20, 25, 39, 40, 51, 16],
						fill: false,
						borderColor: '#FFC357',
						tension: 0.1}
				]
			}
		}
	}
}
</script>

<style scoped>
	.title{
		color: #2A2A2A;
		font-size: 16px;
		font-weight: 700;
		margin-bottom: 20px;
	}
	.rowForecatsMonth{
		display: flex;
		column-gap: 5px;
		justify-content: space-between;
		padding-bottom: 20px;
	}
	.rowForecatsMonth div{
		width: 65px;
		color: #7E92A2;
		font-size: 14px;
		text-align: center;
	}
	.rowForecatsMonth div:last-child{
		width: 97px;
	}
	.rowForecatsMonth div:first-child{
		text-align: left;
		color: #2A2A2A;
	}
	.rowForecatsMonth+ .rowForecatsMonth{
		padding: 20px;
		border-top: 1px solid #D6E1E6;
	}
	.subTitle{
		font-size: 16px;
		line-height: 20px;
		color: #6E7491;
		margin-bottom: 30px;
	}
	.blackRow div{
		color: #2A2A2A;
	}
	.additionMargin{
		margin-top: 40px;
	}
	.scrolledBlock{
		width: 100%;
		overflow-y: auto;
	}
	.blockTable{
		width: 1010px;
	}
	@media (max-width: 768px){
		.myTabSmall{
			width: calc(50% - 5px);
			text-align: center;
		}
		.tabList{
			flex-wrap: wrap;
			row-gap: 10px;
		}
		.listCheckbox{
			overflow-y: auto;
			padding-bottom: 15px;
			margin-bottom: -5px;
		}
	}
</style>
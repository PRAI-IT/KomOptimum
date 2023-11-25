<template lang="pug">
.shadow
	.title Прогноз коммунальных платежей
	.formGroup
		label Напишите какие виды работ планируете реализовать
		textarea(v-model="text")
	.blockSetYear
		span Год окончания ремонта
		input(type="number")
	.btn(@click="showEffect = true") Расчитать эфективность
	transition(name="animHeightBig" mode="out-in")
		.scrolledBlock(v-if="showEffect")
			.forecastPrice
				.additionalHeight
				.additionalHeight
				.titleForecatsPrice Прогноз цены за год
				.rowForecatsPrice
					div
					div.blackRow До ремонта
					div.blackRow После ремонта
				.rowForecatsPrice
					div Вода
					div 746
					div 2 132
						img(src="/img/arrow_top.svg")
				.rowForecatsPrice
					div Свет
					div 2 721
					div 1 821
						img(src="/img/arrow_down.svg")
				.rowForecatsPrice
					div Газ
					div 399
					div 402
						img(src="/img/arrow_top.svg")
				.rowForecatsPrice
					div Тепло
					div 4 321
					div 3 600
						img(src="/img/arrow_down.svg")
transition(name="animHeightBig" mode="out-in")
	div(v-if="showEffect")
		.bigTitle Добиться максимальной эффективности
		.shadow
			.titleCheckBox До ремонта
			.listCheckbox
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
			.titleCheckBox После ремонта
			.listCheckbox
				label.formCheck Вода
					input(type="checkbox" v-model="formSecond.water")
					.checkmark(:style="`--custom_color:${arrColor[4]}`")
				label.formCheck Свет
					input(type="checkbox" v-model="formSecond.light")
					.checkmark(:style="`--custom_color:${arrColor[5]}`")
				label.formCheck Газ
					input(type="checkbox" v-model="formSecond.gas")
					.checkmark(:style="`--custom_color:${arrColor[6]}`")
				label.formCheck Тепло
					input(type="checkbox" v-model="formSecond.teplo")
					.checkmark(:style="`--custom_color:${arrColor[7]}`")
			HackChartsLine(:chartData="chartData")
</template>

<script>
import HackChartsLine from "@/components/charts/HackChartsLine.vue";

export default {
	components: {HackChartsLine},
	data(){
		return{
			arrColor:['#5570F1','#FFC357','#FE8084','#2DC8A8','#D255F1','#9F9AB1','#80D1FE','#117409'],
			showEffect:false,
			text:'',
			form:{
				water:false,
				light:true,
				gas:false,
				teplo:false
			},
			formSecond:{
				water:false,
				light:true,
				gas:false,
				teplo:false
			},
			chartData:{
				labels: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Ноябрь','Декабрь'],
				datasets:  [
					{label: 'My First Dataset',
						data: [65, 59, 80, 81, 56, 55, 40, 65, 59, 80, 81, 56],
						fill: false,
							borderColor: '#FFC357',
						tension: 0.1},
					{label: 'My Second Dataset',
						data: [25, 39, 40, 51, 16, 85, 20, 25, 39, 40, 51, 16],
						fill: false,
						borderColor: '#9F9AB1',
						tension: 0.1}
				]
			}
		}
	}
}
</script>

<style scoped>
	.shadow{
		padding: 20px;
		box-shadow: 0 4px 32px 0 rgba(61, 70, 112, 0.08);
		border-radius: 8px;
	}
	.title{
		color: #2A2A2A;
		font-size: 16px;
		font-weight: 700;
		margin-bottom: 40px;
	}
	.formGroup label{
		font-size: 14px;
		color: #6E7491;
		margin-bottom: 10px;
		display: block;
	}
	textarea{
		padding: 12px 15px;
		border-radius: 8px;
		border: 1px solid #CFCFCF;
		resize: none;
		height: 124px;
		margin-bottom: 10px;
		display: block;
		width: 100%;
		box-shadow: none;
		outline: none;
	}
	.blockSetYear{
		display: flex;
		column-gap: 8px;
		margin-bottom: 20px;
		align-items: center;
	}
	.blockSetYear span{
		color: #53545C;
		font-size: 14px;
	}
	.blockSetYear input{
		height: 36px;
		border: 1px solid #E1E2E9;
		border-radius: 6px;
		padding: 0  8px;
		line-height: 36px;
		font-size: 14px;
		width: 80px;
		outline: none;
		box-shadow: none;
	}
	.additionalHeight{
		height: 15px;
	}
	.titleForecatsPrice{
		margin-bottom: 27px;
		color: #6E7491;
		font-size: 16px;
		font-weight: 500;
	}
	.rowForecatsPrice{
		display: flex;
		column-gap: 50px;
		padding: 20px 0;
		border-bottom: 1px solid #D6E1E6;
		width: fit-content;
	}
	.rowForecatsPrice:first-child{
		padding-top: 0;
	}
	.rowForecatsPrice div:first-child{
		color: #2A2A2A;
		text-align: left;
		justify-content: flex-start;
	}
	.rowForecatsPrice div{
		width: 105px;
		color: #7E92A2;
		font-size: 14px;
		text-align: center;
		align-items: center;
		justify-content: center;
		display: flex;
	}
	.rowForecatsPrice:last-child{
		border-bottom: none;
	}
	.rowForecatsPrice .blackRow{
		color: #2C2D33;
		text-align: left;
		justify-content: flex-start;
	}
	.bigTitle{
		text-align: center;
		font-weight: 700;
		line-height: 24px;
		font-size: 20px;
		margin: 30px 0;
	}
	.titleCheckBox{
		margin-bottom: 10px;
		font-size: 14px;
		line-height: 17px;
	}
	.scrolledBlock{
		width: 100%;
		overflow-y: auto;
	}
	.forecastPrice{
		width: fit-content;
	}
	@media (max-width: 768px){
		.listCheckbox{
			overflow-y: auto;
			padding-bottom: 15px;
			margin-bottom: -5px;
		}
	}
</style>
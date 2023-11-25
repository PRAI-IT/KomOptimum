<template lang="pug">
.title Прогноз коммунальных платежей
.titleCheckBox Средний показатель объекта
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
.titleCheckBox Средний по региону
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
.title.additionalMarginTitle Прогноз коммунальных платежей
.lineGoForecats(v-for="item of 3")
	.blockText Административное здание, 676014, Амурская область, р-н Сковородинский, г Сковородино, ул Победы, д 36, 04-01-07-00-00-005
	.btn(@click="$root.$_hack_selectAddress('')") Перейти к отчёту
</template>

<script>
import HackChartsLine from "@/components/charts/HackChartsLine.vue";

export default {
	components: {HackChartsLine},
	data(){
		return{
			arrColor:['#5570F1','#FFC357','#FE8084','#2DC8A8','#D255F1','#9F9AB1','#80D1FE','#117409'],
			form:{
				water:true,
				light:false,
				gas:false,
				teplo:false
			},
			formSecond:{
				water:true,
				light:false,
				gas:false,
				teplo:false
			},
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
						borderColor: '#D255F1',
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
		margin-bottom: 40px;
	}
	.titleCheckBox{
		margin-bottom: 10px;
		font-size: 14px;
		line-height: 17px;
	}
	.additionalMarginTitle{
		margin-top: 40px;
	}
	.lineGoForecats + .lineGoForecats{
		margin-top: 10px;
	}
	.lineGoForecats{
		display: flex;
	}
	.blockText{
		padding: 9px 20px 9px 8px;
		border: 1px solid #E1E2E9;
		border-radius: 12px;
		height: 50px;
		font-size: 13px;
		line-height: 15px;
		margin-right: -10px;
		overflow: hidden;
	}
	.lineGoForecats .btn{
		width: 149px;
		flex: none;
		height: 50px;
		line-height: 50px;
	}
	@media (max-width: 1110px) {
		.blockText{
			width: 100%;
		}
	}
	@media (max-width: 768px) {
		.blockText{
			-webkit-line-clamp: 2;
			line-height: 18px;
		}
		.listCheckbox{
			overflow-y: auto;
			padding-bottom: 15px;
			margin-bottom: -5px;
		}
	}
</style>
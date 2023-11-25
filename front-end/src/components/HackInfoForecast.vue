<template lang="pug">
.title Прогноз коммунальных расходов
.shadow
	.subTitle Данные об объекте
	.listSettings
		.settingBlock
			span Площадь объекта
			.inputBlock
				input(v-model="form.place")
				.inputWord м²
		.settingBlock
			span Исп. площадь
			.inputBlock
				input(v-model="form.use_place")
				.inputWord м²
		.settingBlock
			span Площадь в аренде
			.inputBlock
				input(v-model="form.arenda_place")
				.inputWord м²
		.settingBlock
			span Тех. состояние
			select(v-model="form.sostoyanie")
				option Хорошее
				option Удовлетворительное
				option Ветхое
				option Аварийное
	.listParams
		.paramsBlock
			span Год постройки*
			span 2008 год
		.paramsBlock
			span Тип помещения*
			span Гараж
.tabList.additionalMargin
	.myTab(:class="{'myTabActive':activeTab === 0}" @click="$_hack_info_forecats_selectMainTab(0)")
		.firstLineTab
			img(src="/img/tabs/1.svg")
			span Прогноз
		.secondLineTab Общий прогноз коммунальных услуг
	.myTab(:class="{'myTabActive':activeTab === 1}" @click="$_hack_info_forecats_selectMainTab(1)")
		.firstLineTab
			img(src="/img/tabs/2.svg")
			span Выбросы
		.secondLineTab Прогноз коммунальных услуг
	.myTab(:class="{'myTabActive':activeTab === 2}" @click="$_hack_info_forecats_selectMainTab(2)")
		.firstLineTab
			img(src="/img/tabs/3.svg")
			span Ремонт
		.secondLineTab Прогноз коммунальных услуг после ремонта
.shadow(v-if="activeTab === 0")
	HackForecatsTabsFirst
.shadow(v-if="activeTab === 1")
	HackForecatsTabsSecond
HackForecatsTabsThird(v-if="activeTab === 2")
.btn.centerBtn(@click="$_hack_info_forecats_changeCheckbox_next") {{activeTab===2?'Перейти на главную':'Перейти к следующему отчету'}}
</template>

<script>
import HackChartsLine from "@/components/charts/HackChartsLine.vue";
import {defineAsyncComponent} from "vue";
export default {
	emits:['back'],
	components: {
		HackChartsLine,
		HackForecatsTabsFirst: defineAsyncComponent(() =>import('@/components/forecatsTabs/HackForecatsTabsFirst.vue')),
		HackForecatsTabsSecond: defineAsyncComponent(() =>import('@/components/forecatsTabs/HackForecatsTabsSecond.vue')),
		HackForecatsTabsThird: defineAsyncComponent(() =>import('@/components/forecatsTabs/HackForecatsTabsThird.vue')),
	},
	data(){
		return{
			activeTab:0,
			form:{
				place:'122.5',
				use_place:'70.5',
				arenda_place:'52',
				sostoyanie:'Хорошее'
			},
		}
	},
	methods:{
		$_hack_info_forecats_changeCheckbox_next(){
			window.scroll({top: 0, behavior: "smooth"})
			if(this.activeTab === 2){
				this.$emit('back')
			}else this.activeTab ++
		},
		$_hack_info_forecats_selectMainTab(type){
			this.activeTab = type
		}
	}
}
</script>

<style scoped>
	.title{
		text-align: center;
		margin-bottom: 30px;
		font-size: 20px;
		line-height: 24px;
		font-weight: 700;
	}
	.shadow{
		padding: 20px;
		box-shadow: 0 4px 32px 0 rgba(61, 70, 112, 0.08);
		border-radius: 8px;
	}
	.subTitle{
		color: #2A2A2A;
		font-size: 16px;
		font-weight: 700;
		margin-bottom: 20px;
	}
	.listParams{
		display: flex;
		flex-wrap: wrap;
		row-gap: 20px;
		margin-top: 20px;
		column-gap: 20px;
	}
	.paramsBlock{
		padding-bottom: 20px;
		border-bottom: 1px solid #D6E1E6;
		width: 308px;
		display: flex;
		column-gap: 8px;;
	}
	.paramsBlock span{
		font-size: 14px;
		line-height: 17px;
		color: #7E92A2;
	}
	.paramsBlock span:first-child{
		color: #53545C !important;
	}
	.tabList{
		display: flex;
		column-gap: 10px;
	}
	.myTab{
		width: 280px;
		flex: none;
		border-radius: 8px;
		border: 1px solid #D6E1E6;
		background: #FFF;
		box-shadow: 0 4px 32px 0 rgba(61, 70, 112, 0.08);
		padding: 14px 10px 14px 20px;
		cursor: pointer;
		transition: .3s ease-in-out;
		outline: 1px solid white;
	}
	.firstLineTab{
		display: flex;
		align-items: center;
		margin-bottom: 9px;
	}
	.firstLineTab span{
		color: #2A2A2A;
		font-size: 14px;
		font-weight: 700;
	}
	.secondLineTab{
		font-size: 11px;
		line-height: 13px;
		color: #6E7491;
	}
	.myTabActive{
		border-color: #5570F1;
		outline: 1px solid #5570F1;
	}
	.myTab img{
		margin-right: 10px;
	}
	.inputBlock{
		position: relative;
		width: fit-content;
	}
	.inputBlock input,select{
		height: 36px;
		padding: 0 30px 0 8px;
		border: 1px solid #E1E2E9;
		border-radius: 6px;
		line-height: 36px;
		font-size: 14px;
		width: 80px;
		outline: none;
		box-shadow: none;
	}
	select{
		padding: 0 8px;
		width: unset;
	 }
	.inputWord{
		position: absolute;
		right: 8px;
		top: 0;
		bottom: 0;
		margin: auto;
		height: fit-content;
		font-size: 14px;
		color: #7E92A2;
	}
	.settingBlock{
		display: flex;
		align-items: center;
	}
	.settingBlock span{
		font-size: 14px;
		padding-right: 8px;
	}
	.additionalMargin{
		margin: 20px 0;
	}
	.listSettings{
		display: flex;
		column-gap: 20px;
		margin-bottom: 20px;
	}
	.centerBtn{
		margin: 40px auto 0 auto;
	}
	@media (max-width: 1100px) {
		.listSettings{
			flex-wrap: wrap;
			column-gap: 20px;
			row-gap: 20px;
		}
		.listSettings .settingBlock{
			width: calc(50% - 10px);
		}
		.listSettings .settingBlock span{
			white-space: nowrap;
		}
		.listSettings .settingBlock .inputBlock,.listSettings .settingBlock .inputBlock input,select{
			width: 100%;
		}
	}
	@media (max-width: 991px) {
		.myTab{
			width: 100% !important;
			flex: 1 !important;
		}
	}
	@media (max-width: 768px) {
		.listSettings .settingBlock{
			width: 100%;
		}
	}
	@media (max-width: 768px) {
		.myTab{
			padding: 10px;
		}
	}
	@media (max-width: 576px) {
		.tabList{
			flex-wrap: wrap;
			row-gap: 20px;
		}
		.myTab{
			width: 100% !important;
			flex: none !important;
		}
	}
</style>
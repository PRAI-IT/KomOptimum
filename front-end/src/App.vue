<template lang="pug">
.container
	.nameProject
		img(src="/img/nameProjectLogo.svg")
		| KomOptimum
	.shadowBlock
		.blockSearch
			.greyTitle Начните вводить город, регион или район
			.inputSearch
				img(src="/img/search.svg")
				VueSelect(:options="listPlaces" v-model="place" :clearable="false"
					@option:selected="$_hack_changeSearch()"
					placeholder="Начните вводить город, регион или район")
					template(#no-options="{ search }")
						span(v-if="search.length>=3") Ничего не найдено
						span(v-else) Начните искать
					template(#open-indicator)
						img.selectarrow(src="/img/selectarrow.svg")
	.shadowBlock.lastBlockShadow
		transition(name="fade" mode="out-in")
			HackFirstStep(v-if="step === 0")
			div(v-else)
				HackInfoForecast(@back="step = 0")

</template>
<script>
import HackFirstStep from "@/components/HackFirstStep.vue";
import HackInfoForecast from "@/components/HackInfoForecast.vue";
import axios from 'axios';
import VueSelect from "vue-select";
export default {
	components: {HackFirstStep,HackInfoForecast,VueSelect},
	data(){
		return{
			step:0,
			listPlaces:['Владивосток, Приморский край'],
			place:'',
			arr:{
				"Прошлый год":[
					"Расходы прошлого года, признанные после отчетной даты.Оплата водоснабжения, канализации",
					"Расходы прошлого года.Оплата потребления электроэнергии",
					"Расходы прошлого года.Оплата водоснабжения, канализации",
					"Расходы прошлого года, признанные после отчетной даты.Оплата потребления электроэнергии",
					"Расходы прошлого года, признанные после отчетной даты.Оплата потребления эл.энергии",
					"Расходы прошлого года. Оплата потребления электроэнергии",
					"Расходы прошлого года.Оплатата потребления электроэнергии",
					"Расходы прошлого года..Оплата потребления тепловой энергии",
					"Расходы прошлого года, признанные после отчетной даты.Оплата потребления тепловой энергии",
					"Расходы прошлого года.Оплата потребления тепловой энергии",
				],
				"Вода":[
					"Оплата водоснабжения",
					"Оплата канализации",
					"Оплата  канализации",
					"Оплата за холодное водоснабжение по тарифам",
					"Оплата за водоотведение по тарифам",
					"Оплата водоотведение",
					"Другие расходы.Холодное водоснабжение",
					"Другие расходы.Канализация",
					"Оплата водоотведения",
					"Оплата за холодное водоснабжение",
					"Оплата за водоотведение  по тарифам",
					"Оплата холодного водоснабжения",
					"Другие расходы.Оплата водоснабжения",
					"Другие расходы.Оплата водоотведения",
					"Другие расходы. Канализация",
					"Оплата за холодное водоснабжение  по тарифам",
					"Расходы по оплате услуг за холодное водоснабжение по тарифам",
					"Оплата водоотведения по тарифам",
					"Оплата за  водоотведение  по тарифам",
					"Другие расходы.Оплата водоотведение",
					"Другие расходы.Оплата канализации",
					"Другие расходы.Оплата холодного водоснабжения",
					"Холодное водоснабжение",
					"Канализация",
					"Затраты на холодное водоснабжение",
					"Затраты на канализацию",
					"Оплата холодное водоснабжения",
					"Расходы по оплате водоотведения",
					"Расходы по оплате холодного водоснабжения",
					"Оплата холодное водоснабжение",
					"Оплата за  водоотведение по тарифам",
				],
				"Свет":[
					"Оплата потребления электроэнергии",
					"Оплата за электроэнергию по тарифам",
					"Оплата за электроэнергию  по тарифам",
					"Другие расходы.Оплата потребления электроэнергии",
					"Плата за технологическое присоединение к электрическим сетям",
					"Расходы по оплате потребления электроэнергии",
				],
				"Газ":[
					"Оплата потребления газа по тарифам"
				],
				"Тепло":[
					"Оплата за горячее водоснабжение",
					"Оплата за горячее водоснабжение  по тарифам",
					"Горячее водоснабжение",
					"Оплата горячее водоснабжения",
					"Оплата за  горячее водоснабжение по тарифам",
					"Оплата за горячее  водоснабжение по тарифам",
					"Другие расходы.Оплата горячего водоснабжения",
					"Оплата горячего водоснабжения",
					"Оплата за горячее водоснабжение по тарифам",
					"Другие расходы.Горячее водоснабжения",
					"Оплата горячее водоснабжение",
					"Другие расходы.Горячее водоснабжение",
					"Оплата потребления тепловой энергии",
					"Оплата за тепловую энергию по тарифам",
					"Другие расходы.Оплата потребления тепловой энергии",
					"Оплата за дизельное топливо",
					"Оплата за потребление тепловой энергии",
					"Оплата потребления тепловой энергии",
					"Расходы по оплате отопления",
				]
			}
		}
	},
	methods:{
		$_hack_selectAddress(address){
			this.place = address
			this.$_hack_changeSearch(address)
		},
		$_hack_changeSearch(){
			this.step = 1
		},
		async requestFnc(method,url,formData){
			const res = await axios({method, url: 'http://185.103.111.98:65535/api/'+url, data:formData})
			if(res.status === 200){
				return res.data
			}else return false
		},
	}
}
</script>
<style>
	.nameProject{
		margin-bottom: 60px;
		display: flex;
		column-gap: 10px;
		font-size: 26px;
		line-height: 39px;
		color: white;
		font-weight: 600;
	}
	.greyTitle{
		margin-bottom: 7px;
		color: #7E92A2;
		font-size: 14px;
	}
	.blockSearch{
		max-width: 755px;
		width: 100%;
		margin: 0 auto;
	}
	.inputSearch{
		padding: 8px 16px;
		height: 45px;
		border-radius: 20px;
		border: 1px solid #D6E1E6;
		margin-bottom: 16px;
		display: flex;
		align-items: center;
		width: 100%;
		column-gap: 16px;
	}
	.lastBlockShadow{
		margin-top: 20px;
		min-height: 596px;
	}
	@media (max-width: 768px) {
		.lastBlockShadow{
			min-height: unset;
		}
		.shadowBlock{
			padding: 15px;
		}
	}
</style>

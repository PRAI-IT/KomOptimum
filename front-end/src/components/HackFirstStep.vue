<template lang="pug">
.containerStep
	img(src="/img/map.svg")
	.blockText
		.title Уважаемые пользователи!
		p Для начала работы вы можете вставить точные адрес объекта или начать вводить название в  адресную строку.
		p Для быстрого ознакомления с сервисом воспользуйтесь заготовленными ссылками ниже.
		.subTitle Рекомендации для просмотра
		.lineGoForecats(v-for="item of 3")
			.textLink Административное здание,  область, р-н Сковородинский, г Сковородино, ул Победы, д 36
			.btn(@click="$root.$_hack_selectAddress('')") Перейти к отчёту
</template>

<style scoped>
	.containerStep{
		padding: 40px 55px 40px 45px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		column-gap: 23px;
	}
	.blockText{
		flex: auto;
		margin-bottom: 40px;
	}
	.title{
		margin-bottom: 20px;
		font-weight: 700;
		font-size: 16px;
		line-height: 20px;
		color: #2A2A2A;
	}
	.blockText p {
		margin-bottom: 8px;
		font-size: 14px;
		line-height: 20px;
		color: #2A2A2A;
	}
	.subTitle{
		font-weight: 700;
		font-size: 16px;
		line-height: 24px;
		color: #2A2A2A;
		margin: 40px 0 20px 0;
	}
	.lineGoForecats{
		display: flex;
		width: 100%;
		margin-bottom: 10px;
	}
	.textLink{
		padding: 9px 20px 9px 8px;
		border: 1px solid #E1E2E9;
		border-radius: 12px;
		height: 50px;
		font-size: 12px;
		line-height: 11px;
		margin-right: -10px;
		color: #2A2A2A;

		-webkit-line-clamp: 3;
		word-break: break-word;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}
	.lineGoForecats .btn{
		width: 149px;
		flex: none;
		height: 50px;
		line-height: 50px;
	}
	@media (max-width: 1110px) {
		.containerStep img{
			display: none;
		}
		.textLink{
			width: 100%;
		}
	}
	@media (max-width: 768px) {
		.containerStep{
			padding: 0;
		}
		.textLink{
			-webkit-line-clamp: 2;
			line-height: 18px;
		}
	}
</style>
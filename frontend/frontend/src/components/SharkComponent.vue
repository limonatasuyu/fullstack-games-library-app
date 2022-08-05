<template>
	<button type="button" class='button'>{{message}}</button>
</template>
<script>
import axios from 'axios'

export default {
	name: 'SharkComponent',
	data() {
		return {
			message: ''
		}
	},
	methods: {
		getResponse() {
			const path = 'http://localhost:5000/shark'
			axios.get(path)
				.then((res) => {console.log(res.data);  this.message = res.data})
				.catch((err) => {console.log(err)})
		}
	},
	created() {
		this.getResponse();
	}
}
</script>

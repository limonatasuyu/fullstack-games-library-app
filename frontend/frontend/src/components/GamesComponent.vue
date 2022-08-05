<template>
	<div class='games-container'>
		<div class='header-container'>
			<p>Games Library</p>
			<hr />
		</div>
		<button type="button" class='button bg-green'>Add Game</button>
		<br/><br/>
		<table>
			<thead>
				<tr>
					<th v-for='i, x in ["Title", "Genre", "Played", "Actions"]' :key='x' scope='col'>{{i}}</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for='i, x in gamesData' :key='x'>
					<td>{{i.title}}</td><td>{{i.genre}}</td><td>{{i.played ? 'Yes' : 'No'}}</td>
					<td>
						<div class='flex' role='group'>
							<button type='button' class='button bg-blue'>Update</button>
							<button type='button' class='button bg-red'>Delete</button>
						</div>
					</td>
				</tr>
			</tbody>
		</table>
		<div class="form-container">
			<form>
				<div class="input-container flex">
					<label for="game-title-input">Game Title</label>
					<input v-model="addGameForm.title" id="game-title-input" type="text" required/>
				</div>
				<div class="input-container flex">
					<label for="game-genre-input">Game Genre</label>
					<input v-model="addGameForm.genre" id="game-genre-input" type="text" required/>
				</div>
				<div class="input-container flex">
					<label for="game-played-input">Played</label>
					<input v-model="addGameForm.played" id="game-played-input" type="checkbox" />
				</div>
				<button @click="onSubmit" class="button bg-blue">Submit</button>
			</form>
		</div>
	</div>
</template>
<style>
.header-container {
	background-color: #e5e3e3
}
</style>
<script>
import axios from 'axios'

export default {
	name: 'GamesComponent',
	data() {
		return {
			gamesData: null,
			addGameForm: {
				title: "",
				genre: "",
				played: [],
			}
		}
	},
	methods: {
		getGamesData() {
			const path = 'http://localhost:5000/games'
			axios.get(path)
				.then(res => this.gamesData = res.data.games)
				.catch(err => console.log(err))
		},
		addGamesData(payload) {
			const path = 'http://localhost:5000/games'
			axios.post(path, payload)
				.then(() => this.getGamesData())
				.catch((err) => {console.log(err); this.getGames()})
		},
		initForm() {
			this.addGameForm.title = "",
			this.addGameForm.genre = "",
			this.addGameForm.played = []
		},
		onSubmit(e) {
			e.preventDefault();
			let played = false;
			if (this.addGameForm.played[0]) played = true
			const payload = {
				title : this.addGameForm.title,
				genre : this.addGameForm.genre,
				played: played
			}
			this.addGamesData(payload);
			this.initForm();
		},
	},
	created() {this.getGamesData()}
}
</script>


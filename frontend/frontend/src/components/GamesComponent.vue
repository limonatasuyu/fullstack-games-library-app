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
							<button @click='toggleIsUpdating(i.id)' type='button' class='button bg-blue'>Update</button>
							<button @click='removeGame(i.id)' type='button' class='button bg-red'>Delete</button>
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
		<hr />
		<div v-if='isUpdating' class="form-container">
			<form>
				<div class="input-container flex">
					<label for="game-title-input">Game Title</label>
					<input v-model="editForm.title" id="game-title-input" type="text" required/>
				</div>
				<div class="input-container flex">
					<label for="game-genre-input">Game Genre</label>
					<input v-model="editForm.genre" id="game-genre-input" type="text" required/>
				</div>
				<div class="input-container flex">
					<label for="game-played-input">Played</label>
					<input v-model="editForm.played" id="game-played-input" type="checkbox" />
				</div>
				<button @click="onUpdateSubmit" class="button bg-green">Submit</button>
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
			},
			editForm: {
				id: "",
				title: "",
				genre: "",
				played: []
			},
			isUpdating: false,

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
				.catch((err) => {console.log(err); this.getGamesData()})
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
		toggleIsUpdating(id) {this.isUpdating = !this.isUpdating; this.editForm.id = id},
		updateGame(payload, gameID) {
			const path = `http://localhost:5000/games/${gameID}`
			axios.put(path, payload)
				.then(() => {this.getGamesData()})
				.catch(err => {console.log(err); this.getGamesData()})
		},
		onUpdateSubmit(e) {
			e.preventDefault()
			let played = false
			if (this.editForm.played[0]) played = true;
			const payload = {
				title: this.editForm.title,
				genre: this.editForm.genre,
				played,
			}
			this.updateGame(payload, this.editForm.id)
		},
		removeGame(gameId) {
			const path = `http://localhost:5000/games/${gameId}`
			axios.delete(path)
				.then(() => {this.getGamesData(); this.message = "Game removed"})
				.catch(err => {console.log(err); this.getGamesData()})
		}
	},
	created() {this.getGamesData()}
}
</script>


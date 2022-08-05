<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
html, body {margin: 0; padding: 0;}
.flex {display: flex}
.grid {display: grid}
.bg-green {background-color: green;}
.bg-blue {background-color: blue;}
.bg-red {background-color: red;}
.button {
	border: none; outline: none;
	border-radius: 2px;
	font-size: 1.5rem;
	color: white;
	padding: .5rem;
	cursor: pointer;
}

#app {margin-top: 60px;}

</style>

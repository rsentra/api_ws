<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Summary from "./routes/Summary.svelte"
  import { link } from 'svelte-spa-router'

  const routes = {
    '/': Home,
    '/api/summary': Summary
  }
</script>

<Router {routes}/>
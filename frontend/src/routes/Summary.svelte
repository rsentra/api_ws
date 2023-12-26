<script>
  import fastapi from "../lib/api"
  import { link } from 'svelte-spa-router'
  import { push } from 'svelte-spa-router'
  import Popup from '../lib/Popup.svelte'

  let params = {}
  let content = ""
  let message = []
  let mode = ""
  let create_date = ""
  
  function summary_get() {
    fetch("http://127.0.0.1:8000/api/summaryGet/SSSSS").then((response) => {
      response.json().then((json) => {
        message = json
      })
    })
  }

  // summary_get()

  function post_summary(event) {
        event.preventDefault()
        let url = "/api/summary"
        let params = {
            content: content,
            mode: mode
        }
        fastapi("post", url, params,
          (json) => {
          message = json.content
          create_date = json.create_date
      })
    }

    function post_create(event) {
        event.preventDefault()
        let url = "/api/create"
        let params = {
            content: content,
            summary: message,
            create_date: create_date
        }
        fastapi("post", url, params,
          (json) => {
            alert('저장완료')	
          },
          (json_error) => {
                error = json_error
            }
          )
    }
    
</script>
<div> <a use:link href="/">메인으로</a> </div>
<div style="float: left; width: 50%;">
  <p> <b>입력한 <i>상담내용</i>을 요약합니다</b> </p>
  <hr>
  <form method="post">
    <textarea rows="30" cols="100" bind:value={content}></textarea><p></p>
    <input type="submit" value="요약요청" on:click="{post_summary}">
      
    <input type='radio' bind:group={mode} value="test" />gpt연동X
    <input type='radio' bind:group={mode} value="gpt" />gtp연동
  </form>
</div>
<div style="float: left; width: 50%;">
  <h5>  결과 </h5> 
  <form method="post">
    <textarea rows="30" cols="100" bind:value={message}></textarea>
    <input type="hidden" bind:value={create_date}/><p></p>
    <!-- <button class="btn btn-dark" on:click="{post_create}">저장하기</button> -->
    <input type="submit" value="저장하기" on:click="{post_create}">
  </form>
  
</div>
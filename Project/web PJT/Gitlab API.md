# Gitlab API



### API resource

#### Project resources

- Commits

```
GET	/prljects/:id/repository/commits
```

Get a list of repository commits in a project.



- Members

```
GET	/projects/:id/members
```

Gets a list of project members viewable by the authenticated user.



사용 예시)

```
getMembers(the_id) {
		return Api(BASE_URL).get(`/projects/${the_id}/members`)
	}
```

the_id: group or project의 id





#### Standalone

- Projects

```
GET	/users/:user_id/projects
```

Get a list of visible projects owned by the given user.





## axios

HTTP 클라이언트 라이브러리로써 비동기 방힉으로 HTTP 데이터 요청을 실행



- get 사용법

```
// GET
axios.get('/api/todos')
  .then(res => {
    console.log(res.data)
  })
```

or

```
const result = await axios.get('/api/todos');
console.log(result.data)
```





### async and await







### mounted







------

##### 참고

- [Gitlab API](https://docs.gitlab.com/ee/api/)

- [axios 사용법+정의](https://zoomkoding.github.io/web%EA%B0%9C%EB%B0%9C/vue/histime/2019/01/30/axios.html)


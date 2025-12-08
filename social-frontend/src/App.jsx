import { useEffect, useState } from "react";
import { api } from "./api";

function App() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get("/posts/")
      .then((res) => {
        setPosts(res.data);
      })
      .catch((err) => {
        console.error("Error fetching posts:", err);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ maxWidth: "700px", margin: "0 auto" }}>
      <h1>Simple Social App</h1>

      {posts.length === 0 && <p>No posts yet.</p>}

      {posts.map((post) => (
        <div
          key={post.id}
          style={{
            marginBottom: "20px",
            padding: "10px",
            border: "1px solid #ccc",
          }}
        >
          <img
            src={post.image}
            alt="post"
            style={{ maxWidth: "100%", marginBottom: "8px" }}
          />
          <p>{post.caption}</p>
        </div>
      ))}
    </div>
  );
}

export default App;

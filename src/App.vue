
<script setup>

</script>


<template>
  <div class="blog-root">
    <header class="blog-header">
      <div class="header-layout">
        <div class="header-picture-col">
          <img src="/bass.png" alt="Bass logo" class="header-logo" />
        </div>
        <div class="header-content-col">
          <div class="header-title-row">
            <h1>Dum Bass Blog</h1>
          </div>
          <nav class="blog-menu">
            <router-link to="/" class="menu-btn">Home</router-link>
            <router-link to="/blogs/" class="menu-btn">Posts</router-link>
              <div class="header-icons">
                <a href="https://cv.kaese.space" target="_blank" rel="noopener" title="CV">
                  <img src="/cv.png" alt="CV" class="header-icon-img" />
                </a>
                <a href="https://github.com/kaese72" target="_blank" rel="noopener" title="Github">
                  <img src="/github.ico" alt="Github" class="header-icon-img" />
                </a>
                <a href="https://se.linkedin.com/in/calle-ryd%C3%A9n-975a11236" target="_blank" rel="noopener" title="Linkedin">
                  <img src="/linkedin.ico" alt="Linkedin" class="header-icon-img" />
                </a>
                <a href="/rss.xml" target="_blank" rel="noopener" title="RSS">
                  <img src="/rss.svg" alt="RSS" class="header-icon-img" />
                </a>
              </div>
          </nav>
        </div>
      </div>
    </header>
    <main class="blog-content">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.blog-root {
  min-height: 100vh;
  background: #f5f5f5;
  display: flex;
  flex-direction: column;
  align-items: center;
/* End blog-menu */

.blog-header {
  width: 21cm;
  background: #e0e0e0;
  color: #222;
  padding: 1rem 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  font-size: 1.2rem;
  letter-spacing: 0.1em;
  border-radius: 6px 6px 0 0;
  margin-top: 2rem;
  overflow: hidden;
  position: relative;
}

  .header-layout {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    width: 100%;
    height: 100%;
  }

  .header-picture-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-width: 7rem;
    max-width: 7rem;
    margin-right: 1.5rem;
    height: 100%;
    box-sizing: border-box;
  }

  .header-content-col {
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: flex-start;
  }

  .header-title-row {
    display: flex;
    align-items: center;
    min-height: 3.5rem;
  }
}

.header-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
}

.blog-menu {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  background: transparent;
    margin-top: 1.5rem;
    gap: 1rem;
}

.header-icons {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-left: auto; /* Aligns icons to the right */
}

.header-icon-img {
  width: 2rem;
  height: 2rem;
  object-fit: contain;
  display: inline-block;
  vertical-align: middle;
  transition: filter 0.2s;
}
.header-icon-img:hover {
  filter: brightness(0.7);
}

.menu-btn {
  background: #fff;
  border: 1px solid #bdbdbd;
  border-radius: 6px;
  padding: 0.5rem 1.2rem;
  font-size: 1rem;
  cursor: pointer;
  margin-top: -0.5rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  transition: background 0.2s;
}
.menu-btn:hover {
  background: #f0f0f0;
}

.header-logo {
  max-height: 100%;
  max-width: 100%;
  width: 6.5rem;
  height: 6.5rem;
  object-fit: contain;
  display: block;
  border: 3px solid #bdbdbd;
  border-radius: 1.5rem;
  background: #fff;
  box-sizing: border-box;
}

.blog-header h1 {
  margin: 0;
  flex: 1;
  text-align: left;
}

.blog-content {
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 0;
}

.a4-paper {
  background: #fff;
  width: 21cm;
  min-height: 29.7cm;
  box-shadow: 0 4px 24px rgba(0,0,0,0.12);
  border-radius: 6px;
  padding: 2.5cm 2cm;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
  font-family: 'Georgia', 'Times New Roman', Times, serif;
}

.a4-paper h2 {
  margin-top: 0;
}
</style>

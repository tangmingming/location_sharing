<template>
  <div style="display: flex; flex-direction: column; height: 100%">
    <router-view name="header"></router-view>
    <router-view style="flex: 1" name="body" ></router-view>
    <router-view name="footer"></router-view>
  </div>
</template>

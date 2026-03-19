# React Hooks 简介

## 什么是 Hooks？

Hooks 是 React 16.8 引入的新特性，它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。

### 为什么需要 Hooks？

在 Hooks 出现之前，如果你想在函数组件中使用状态，你必须把它改成 class 组件。这带来了几个问题：

1. **复杂组件难以理解**：class 组件中生命周期方法经常包含不相关的逻辑
2. **组件之间复用状态逻辑很难**：需要使用 render props 或高阶组件，导致"嵌套地狱"
3. **难以理解的 class**：this 的指向问题让很多开发者困惑

## useState Hook

useState 是最基本的 Hook，它让函数组件也能拥有状态。

### 基本用法

```jsx
import { useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

### 解构赋值说明

`const [count, setCount] = useState(0)` 这里使用了数组解构：
- `count` 是当前的状态值
- `setCount` 是更新状态的函数
- `0` 是初始状态

## useEffect Hook

useEffect 让你在函数组件中执行副作用操作。

### 什么是副作用？

在 React 中，副作用通常指：数据获取、订阅或者手动修改 DOM。

### 基本用法

```jsx
import { useState, useEffect } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

## Hook 使用规则

使用 Hooks 时需要遵循两条规则：

1. **只在最顶层使用 Hook**：不要在循环、条件或嵌套函数中调用 Hook
2. **只在 React 函数中调用 Hook**：在 React 函数组件或自定义 Hook 中调用

## 总结

Hooks 让你能够在不改变组件层次结构的情况下复用状态逻辑，让代码更加简洁易懂。

# React 组件

## 什么是组件？

组件是 React 应用的基本构建块。它们是可复用的 UI 片段。

## 函数组件

```jsx
function Welcome({ name }) {
  return <h1>Hello, {name}</h1>;
}
```

## useState Hook

用于在函数组件中添加状态：

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

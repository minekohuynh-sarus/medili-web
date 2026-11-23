// Hướng dẫn pha MeDili: mô hình 3D dựng hoàn toàn bằng code với three.js r160 (không dùng file mô hình ngoài).
// Một khung vẽ cố định phủ màn hình; mỗi mô hình bám theo ô .hd-stage[data-m] của nó khi cuộn trang.
// Màu theo bảng màu MeDili (kem, nâu cà phê, đồng, đỏ đất); không dùng xanh lá, đen hay xanh dương.
import * as THREE from 'three';

const SHOT = new URLSearchParams(location.search).get('shot');   // chế độ chụp ảnh dự phòng
const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
const DS = THREE.DoubleSide;

// ---------- vật liệu ----------
const M = {
  copper: () => new THREE.MeshPhysicalMaterial({color: '#C98A5E', metalness: 1, roughness: .24, clearcoat: .3, clearcoatRoughness: .2, side: DS}),
  copperD: () => new THREE.MeshPhysicalMaterial({color: '#9A5A34', metalness: 1, roughness: .32, side: DS}),
  alu: () => new THREE.MeshPhysicalMaterial({color: '#ECE9E4', metalness: .45, roughness: .3, clearcoat: .5, clearcoatRoughness: .18, side: DS}),
  wood: () => new THREE.MeshStandardMaterial({color: '#7B4B2A', roughness: .55, side: DS}),
  cream: () => new THREE.MeshPhysicalMaterial({color: '#F3EADC', roughness: .32, clearcoat: .6, clearcoatRoughness: .25, side: DS}),
  terra: () => new THREE.MeshPhysicalMaterial({color: '#A9432A', roughness: .3, clearcoat: .8, clearcoatRoughness: .18, side: DS}),
  paper: () => new THREE.MeshStandardMaterial({color: '#F4ECDD', roughness: .9, side: DS}),
  coffee: () => new THREE.MeshPhysicalMaterial({color: '#3B2013', roughness: .18, clearcoat: .7, side: DS}),
  milk: () => new THREE.MeshStandardMaterial({color: '#EFDDBD', roughness: .5, side: DS}),
  glass: (tint = '#FFFFFF', op = .2) => new THREE.MeshPhysicalMaterial({color: tint, roughness: .05, metalness: 0, transparent: true, opacity: op,
    clearcoat: 1, clearcoatRoughness: .04, side: DS, depthWrite: false, envMapIntensity: 1.5}),
};

// ---------- hình học ----------
const lathe = (pts, seg = 96) => new THREE.LatheGeometry(pts.map(([r, y]) => new THREE.Vector2(Math.max(r, 0), y)), seg);
const mesh = (geo, mat, x = 0, y = 0, z = 0) => { const m = new THREE.Mesh(geo, mat); m.position.set(x, y, z); return m; };

function canvasTex(w, h, draw, srgb = true) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); if (srgb) t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t;
}

let SHADOW_TEX;
function shadow(w, d, op = .5) {
  SHADOW_TEX ||= canvasTex(128, 128, (g) => {
    const r = g.createRadialGradient(64, 64, 0, 64, 64, 64);
    r.addColorStop(0, 'rgba(46,26,14,1)'); r.addColorStop(.5, 'rgba(46,26,14,.42)'); r.addColorStop(1, 'rgba(46,26,14,0)');
    g.fillStyle = r; g.fillRect(0, 0, 128, 128);
  });
  const m = new THREE.Mesh(new THREE.PlaneGeometry(w, d), new THREE.MeshBasicMaterial({map: SHADOW_TEX, transparent: true, opacity: op, depthWrite: false}));
  m.rotation.x = -Math.PI / 2; m.position.y = .003; m.renderOrder = -1; return m;
}

// gộp các đỉnh trùng vị trí (đường nối của khối cầu) để bóng đổ mượt
function weld(geo) {
  const p = geo.attributes.position, c = geo.attributes.color, idx = geo.index.array;
  const map = new Map(), pos = [], cols = [], remap = new Uint32Array(p.count);
  for (let i = 0; i < p.count; i++) {
    const k = Math.round(p.getX(i) * 1e4) + ',' + Math.round(p.getY(i) * 1e4) + ',' + Math.round(p.getZ(i) * 1e4);
    let j = map.get(k);
    if (j === undefined) { j = pos.length / 3; map.set(k, j); pos.push(p.getX(i), p.getY(i), p.getZ(i)); if (c) cols.push(c.getX(i), c.getY(i), c.getZ(i)); }
    remap[i] = j;
  }
  const ni = [];
  for (let i = 0; i < idx.length; i += 3) { const a = remap[idx[i]], b = remap[idx[i + 1]], d = remap[idx[i + 2]]; if (a !== b && b !== d && a !== d) ni.push(a, b, d); }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  if (c) g.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
  g.setIndex(ni); g.computeVertexNormals(); return g;
}

// hạt cà phê: khối dẹt, một mặt phẳng có rãnh chữ S, màu rang mộc loang nhẹ
function beanGeo(ws, hs) {
  const g = new THREE.SphereGeometry(1, ws, hs), p = g.attributes.position, n = p.count, col = new Float32Array(n * 3);
  const cA = new THREE.Color('#85502E'), cB = new THREE.Color('#5E331B'), cC = new THREE.Color('#2C150A'), tmp = new THREE.Color();
  for (let i = 0; i < n; i++) {
    let x = p.getX(i), y = p.getY(i), z = p.getZ(i);
    const front = Math.max(z, 0);
    if (z > 0) z *= .56;
    const sx = .085 * Math.sin(y * 2.5);
    const band = Math.exp(-((x - sx) ** 2) / (2 * .075 ** 2));
    const groove = band * front * Math.max(0, 1 - y ** 6);
    z -= groove * .21;
    x *= 1 + .045 * Math.sin(y * 3.2);
    p.setXYZ(i, x * .7, y, z * .56);
    const nse = .5 + .5 * Math.sin(x * 17 + y * 9) * Math.cos(z * 13 - y * 7);
    tmp.copy(cA).lerp(cB, .2 + .35 * nse).lerp(cC, Math.min(1, groove * 2.4));
    col[i * 3] = tmp.r; col[i * 3 + 1] = tmp.g; col[i * 3 + 2] = tmp.b;
  }
  g.setAttribute('color', new THREE.BufferAttribute(col, 3));
  return weld(g);
}

function groundsTex() {
  return canvasTex(256, 256, (g) => {
    g.fillStyle = '#4A2817'; g.fillRect(0, 0, 256, 256);
    for (let i = 0; i < 2600; i++) {
      const v = Math.random(); g.fillStyle = v < .5 ? 'rgba(30,14,6,.7)' : v < .85 ? 'rgba(110,64,36,.65)' : 'rgba(150,96,58,.55)';
      g.beginPath(); g.arc(Math.random() * 256, Math.random() * 256, .6 + Math.random() * 1.8, 0, 7); g.fill();
    }
  });
}

// ---------- mô hình ----------
function mBean() {
  const g = new THREE.Group();
  const mat = new THREE.MeshPhysicalMaterial({color: '#FFFFFF', vertexColors: true, roughness: .34, clearcoat: .6, clearcoatRoughness: .28,
    sheen: .35, sheenColor: new THREE.Color('#9A6A46'), sheenRoughness: .5});
  const big = new THREE.Mesh(beanGeo(196, 132), mat); big.scale.setScalar(.47);
  const pivot = new THREE.Group(); pivot.add(big); pivot.rotation.z = .2; pivot.position.y = .53; g.add(pivot);
  const sgeo = beanGeo(80, 60), smalls = [];
  for (const [r, y, ph, sc] of [[.5, .84, .4, .11], [.54, .3, 2.5, .095], [.56, .62, 4.4, .08]]) {
    const b = new THREE.Mesh(sgeo, mat); b.scale.setScalar(sc); g.add(b); smalls.push({b, r, y, ph});
  }
  g.add(shadow(.95, .55, .38));
  return {g, h: 1.06, sz: 1.12, update(t, p) {
    big.rotation.y = -.35 + Math.sin(t * .45) * 1.15 + p * 1.2; pivot.position.y = .53 + Math.sin(t * 1.2) * .018;
    for (const s of smalls) {
      const a = s.ph + t * .32;
      s.b.position.set(Math.cos(a) * s.r, s.y + Math.sin(t * .9 + s.ph) * .03, Math.sin(a) * s.r * .55);
      s.b.rotation.set(t * .5 + s.ph, t * .7, s.ph);
    }
  }};
}

function mGrinder() {
  const g = new THREE.Group(), cu = M.copper(), cuD = M.copperD(), wd = M.wood();
  g.add(mesh(lathe([[.045, 0], [.06, 0], [.066, .02], [.075, .055], [.2, .125], [.27, .152], [.282, .162]]), cuD));       // phễu ra bột
  g.add(mesh(lathe([[.282, .162], [.292, .17], [.292, .25], [.282, .258]]), wd));                                          // đai gỗ
  g.add(mesh(lathe([[.282, .258], [.276, .262], [.276, .7], [.286, .706], [.292, .722], [.292, .758], [.272, .774], [.222, .8],
    [.12, .83], [.05, .842], [0, .844]]), cu));                                                                              // thân đồng
  for (const y of [.262, .7]) { const r = mesh(new THREE.TorusGeometry(.279, .007, 12, 120), cuD, 0, y); r.rotation.x = Math.PI / 2; g.add(r); }
  g.add(mesh(new THREE.CylinderGeometry(.022, .026, .13, 24), cuD, 0, .9));
  const crank = new THREE.Group(); crank.position.y = .955; g.add(crank);
  crank.add(mesh(new THREE.CylinderGeometry(.05, .05, .03, 32), cuD));
  const arm = mesh(new THREE.BoxGeometry(.46, .026, .06), cu, .22, 0); crank.add(arm);
  crank.add(mesh(new THREE.CylinderGeometry(.042, .05, .13, 32), wd, .43, .075));
  crank.add(mesh(new THREE.SphereGeometry(.043, 24, 12, 0, Math.PI * 2, 0, Math.PI / 2), wd, .43, .14));
  return {g, h: 1.06, sz: 1.1, nozzle: new THREE.Vector3(0, -.01, 0), update(t) { crank.rotation.y = -t * 2.2; }};
}

function mPhin() {
  const g = new THREE.Group();
  // ly thủy tinh: thành ngoài lên, vành, thành trong xuống
  g.add(mesh(lathe([[0, 0], [.27, 0], [.29, .015], [.3, .05], [.335, .62], [.34, .64], [.33, .642], [.322, .62], [.29, .085], [0, .075]]), M.glass('#FFFFFF', .24)));
  g.add(mesh(new THREE.CylinderGeometry(.291, .287, .085, 72), M.milk(), 0, .118));
  const cof = mesh(new THREE.CylinderGeometry(.302, .29, 1, 72), M.coffee(), 0, 0); g.add(cof);
  const lvl = .2; cof.scale.y = lvl; cof.position.y = .16 + lvl / 2;
  // đĩa phin, buồng phin để mở, bột cà phê bên trong
  const al = M.alu();
  g.add(mesh(lathe([[0, .645], [.4, .645], [.43, .652], [.442, .668], [.436, .674], [.41, .664], [.25, .66], [0, .66]]), al));
  g.add(mesh(lathe([[.2, .66], [.236, .662], [.252, 1.04], [.262, 1.06], [.252, 1.062], [.24, 1.04], [.226, .676], [0, .674]]), al));
  const gr = mesh(new THREE.CircleGeometry(.238, 64), new THREE.MeshStandardMaterial({map: groundsTex(), roughness: .95}), 0, .95);
  gr.rotation.x = -Math.PI / 2; g.add(gr);
  // giọt cà phê
  const dm = M.coffee(), drops = [0, 1, 2].map(() => { const d = mesh(new THREE.SphereGeometry(.017, 16, 12), dm); d.scale.y = 1.5; g.add(d); return d; });
  g.add(shadow(1.1, .9, .42));
  const top = .66 - .02, bot = .16 + lvl;
  return {g, h: 1.07, sz: 1.12, mouth: new THREE.Vector3(0, .95, 0), update(t) {
    drops.forEach((d, i) => { const f = ((t * .9 + i / 3) % 1); d.position.set(0, top - (top - bot) * f * f, 0); d.visible = f < .97; });
  }};
}

function mPour() {
  const g = new THREE.Group(), set = new THREE.Group(); g.add(set); set.position.x = .3;
  // bình thủy tinh và cà phê bên trong
  set.add(mesh(lathe([[0, 0], [.29, 0], [.32, .02], [.355, .14], [.36, .26], [.33, .4], [.27, .5], [.272, .54], [.262, .545], [.258, .5],
    [.318, .4], [.345, .26], [.34, .14], [.305, .035], [0, .03]]), M.glass('#FFFFFF', .22)));
  set.add(mesh(lathe([[0, .035], [.3, .035], [.334, .14], [.343, .2], [0, .2]]), M.coffee()));
  // phễu gốm đỏ đất, đế và quai
  const tr = M.terra(), base = new THREE.Group(); base.position.y = .54; set.add(base);
  base.add(mesh(lathe([[0, 0], [.3, 0], [.315, .012], [.312, .03], [.14, .035], [.12, .06], [.1, .06], [0, .06]]), tr));
  base.add(mesh(lathe([[.1, .06], [.13, .06], [.44, .5], [.47, .52], [.472, .54], [.45, .545], [.43, .525], [.115, .095], [0, .09]]), tr));
  const h = mesh(new THREE.TorusGeometry(.09, .026, 14, 40, Math.PI * 1.25), tr, .46, .3); h.rotation.z = -Math.PI * .62; base.add(h);
  base.add(mesh(lathe([[.012, .105], [.11, .11], [.415, .5], [.43, .6], [.425, .605], [.405, .51], [.1, .12], [0, .118]], 96), M.paper()));   // giấy lọc
  const bed = mesh(new THREE.CircleGeometry(.235, 64), new THREE.MeshStandardMaterial({map: groundsTex(), roughness: .9}), 0, .33);
  bed.rotation.x = -Math.PI / 2; base.add(bed);
  // ấm cổ ngỗng bằng đồng: dựng sao cho đầu vòi nằm ở gốc tọa độ
  const kettle = new THREE.Group(), body = new THREE.Group(), cu = M.copper(), wd = M.wood();
  body.add(mesh(lathe([[0, 0], [.3, 0], [.33, .018], [.36, .11], [.37, .28], [.34, .43], [.25, .54], [.18, .57], [.178, .59]]), cu));
  body.add(mesh(lathe([[.185, .585], [.17, .6], [.12, .63], [.05, .645], [0, .648]]), cu));
  body.add(mesh(new THREE.SphereGeometry(.045, 20, 14), wd, 0, .67));
  const spout = new THREE.CatmullRomCurve3([[.32, .09], [.47, .14], [.57, .35], [.63, .55], [.72, .65], [.83, .64], [.88, .6]].map(([x, y]) => new THREE.Vector3(x, y, 0)));
  body.add(mesh(new THREE.TubeGeometry(spout, 80, .024, 16), cu));
  const hdl = new THREE.CatmullRomCurve3([[-.3, .1], [-.5, .17], [-.57, .38], [-.47, .58], [-.24, .55]].map(([x, y]) => new THREE.Vector3(x, y, 0)));
  body.add(mesh(new THREE.TubeGeometry(hdl, 60, .034, 14), wd));
  body.position.set(-.88, -.6, 0); kettle.add(body);
  const tipY = 1.36; kettle.scale.setScalar(.62); kettle.position.set(0, tipY, 0); kettle.rotation.z = -.45; set.add(kettle);
  // dòng nước rót
  const surf = .54 + .33, stream = mesh(new THREE.CylinderGeometry(.01, .013, 1, 12), M.glass('#FFFFFF', .55)); set.add(stream);
  set.add(shadow(1.2, .9, .4)); g.position.x = -.08;
  return {g, h: 1.66, sz: 1.72, update(t) {
    const a = t * 2.2, ox = Math.cos(a) * .055, oz = Math.sin(a) * .055;
    kettle.position.set(ox, tipY, oz);
    const len = tipY - surf; stream.scale.y = len; stream.position.set(ox, surf + len / 2, oz);
  }};
}

function steamTex() {
  return canvasTex(64, 128, (g) => {
    const r = g.createRadialGradient(32, 70, 2, 32, 70, 30);
    r.addColorStop(0, 'rgba(255,255,255,.9)'); r.addColorStop(1, 'rgba(255,255,255,0)');
    g.fillStyle = r; g.beginPath(); g.ellipse(32, 64, 18, 56, 0, 0, 7); g.fill();
  });
}

function cremaTex() {
  return canvasTex(256, 256, (g) => {
    const r = g.createRadialGradient(128, 128, 10, 128, 128, 128);
    r.addColorStop(0, '#D49A5E'); r.addColorStop(.55, '#B97640'); r.addColorStop(.86, '#7A4220'); r.addColorStop(1, '#4E2913');
    g.fillStyle = r; g.fillRect(0, 0, 256, 256);
    for (let i = 0; i < 260; i++) { g.fillStyle = `rgba(${Math.random() < .5 ? '235,190,135' : '120,64,30'},.25)`; g.beginPath();
      const a = Math.random() * 7, d = Math.random() * 110; g.arc(128 + Math.cos(a) * d, 128 + Math.sin(a) * d, 1 + Math.random() * 4, 0, 7); g.fill(); }
  });
}

function mEspresso() {
  const g = new THREE.Group(), cr = M.cream(), tr = M.terra();
  g.add(mesh(lathe([[0, 0], [.24, 0], [.27, .01], [.3, .014], [.5, .046], [.55, .07], [.556, .082], [.54, .086], [.49, .066], [.31, .036], [.25, .03], [0, .03]], 120), cr));
  const cup = new THREE.Group(); cup.position.y = .03; g.add(cup);
  cup.add(mesh(lathe([[0, 0], [.15, 0], [.165, .01], [.2, .05], [.265, .17], [.3, .3], [.31, .38], [.312, .395]], 110), tr));
  cup.add(mesh(lathe([[.312, .395], [.3, .4], [.292, .38], [.282, .3], [.25, .18], [.19, .08], [.08, .06], [0, .058]], 110), cr));
  const crema = mesh(new THREE.CircleGeometry(.284, 72), new THREE.MeshPhysicalMaterial({map: cremaTex(), roughness: .45, clearcoat: .3}), 0, .345);
  crema.rotation.x = -Math.PI / 2; cup.add(crema);
  const hd = mesh(new THREE.TorusGeometry(.085, .024, 16, 48, Math.PI * 1.3), tr, .335, .22); hd.rotation.z = -Math.PI * .65; cup.add(hd);
  const st = steamTex(), puffs = [0, 1, 2].map(i => { const s = new THREE.Sprite(new THREE.SpriteMaterial({map: st, transparent: true, depthWrite: false, opacity: 0}));
    cup.add(s); return s; });
  g.add(shadow(1.25, 1.25, .35));
  return {g, h: .62, sz: 1.12, update(t) {
    puffs.forEach((s, i) => { const f = (t * .22 + i / 3) % 1; s.position.set(Math.sin(t * .8 + i * 2) * .06 + (i - 1) * .07, .42 + f * .5, 0);
      s.scale.set(.16 + f * .2, .32 + f * .3, 1); s.material.opacity = Math.sin(f * Math.PI) * .32; });
  }};
}

function labelTex() {
  return canvasTex(1024, 360, (g, w, h) => {
    g.fillStyle = '#F3E6CF'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#9E3B26'; g.fillRect(0, h - 44, w, 44);
    g.textAlign = 'center'; g.fillStyle = '#9E3B26';
    g.font = 'italic 600 96px "Playfair Display", Georgia, serif'; g.fillText('MeDili', w / 2, 112);
    g.fillStyle = '#4A2C1A'; g.font = '800 118px "Big Shoulders Display", "Arial Narrow", sans-serif'; g.fillText('COLD BREW', w / 2, 232);
    g.font = '600 34px "Be Vietnam Pro", system-ui, sans-serif'; g.fillStyle = '#6B4A35'; g.fillText('Robusta Di Linh · ủ lạnh 18–24 giờ', w / 2, 284);
    g.fillStyle = '#F3E6CF'; g.font = '700 26px "Be Vietnam Pro", system-ui, sans-serif'; g.fillText('MÊ VỊ DI LINH', w / 2, h - 13);
  });
}

function mCold() {
  const g = new THREE.Group(), b = new THREE.Group(); b.position.x = -.17; g.add(b);
  b.add(mesh(lathe([[0, 0], [.22, 0], [.245, .015], [.252, .05], [.252, .62], [.242, .68], [.18, .76], [.104, .82], [.088, .86], [.088, .975],
    [.098, .985], [.098, 1.0], [.08, 1.0], [.078, .86], [.094, .82], [.17, .75], [.236, .675], [.24, .05], [.21, .022], [0, .02]]), M.glass('#8A4A22', .3)));
  b.add(mesh(lathe([[0, .025], [.232, .025], [.236, .06], [.236, .6], [.226, .66], [.16, .73], [0, .73]]), new THREE.MeshPhysicalMaterial({color: '#24120A', roughness: .2, clearcoat: .8, side: DS})));
  b.add(mesh(new THREE.CylinderGeometry(.103, .103, .085, 40), new THREE.MeshStandardMaterial({color: '#C08A57', roughness: .8}), 0, 1.04));
  const L = 2.5, lab = mesh(new THREE.CylinderGeometry(.256, .256, .34, 96, 1, true, -L / 2, L), new THREE.MeshStandardMaterial({map: labelTex(), roughness: .75}), 0, .33);
  b.add(lab);
  // ly cà phê có đá
  const c = new THREE.Group(); c.position.set(.33, 0, .2); g.add(c);
  c.add(mesh(lathe([[0, 0], [.16, 0], [.175, .012], [.19, .44], [.195, .45], [.185, .452], [.18, .44], [.165, .028], [0, .025]]), M.glass('#FFFFFF', .22)));
  c.add(mesh(new THREE.CylinderGeometry(.174, .161, .29, 64), M.coffee(), 0, .19));
  const ice = new THREE.MeshPhysicalMaterial({color: '#FFFFFF', roughness: .08, transparent: true, opacity: .45, clearcoat: 1, depthWrite: false});
  const cubes = [[-.05, .33, .02, .4], [.06, .34, -.03, 1.1], [0, .4, .06, 2.2]].map(([x, y, z, r]) => {
    const k = mesh(new THREE.BoxGeometry(.11, .1, .11), ice, x, y, z); k.rotation.set(r, r * .7, r * .3); c.add(k); return k; });
  g.add(shadow(1.35, 1, .4));
  return {g, h: 1.13, sz: 1.2, update(t) { cubes.forEach((k, i) => { k.position.y = .33 + i * .03 + Math.sin(t * 1.3 + i * 2) * .008; }); }};
}

const MAKE = {bean: mBean, grinder: mGrinder, phin: mPhin, 'pour-over': mPour, espresso: mEspresso, 'cold-brew': mCold};
const FIT = {bean: .9, grinder: .74, phin: .84, 'pour-over': .9, espresso: .8, 'cold-brew': .84};
const TILT = {bean: .1, grinder: .2, phin: .36, 'pour-over': .22, espresso: .5, 'cold-brew': .2};
const YAW = {bean: 0, grinder: -.55, phin: -.4, 'pour-over': .2, espresso: -.7, 'cold-brew': -.25};

// ---------- ánh sáng và môi trường ----------
function studio(renderer, scene) {
  const tex = canvasTex(512, 256, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h);
    gr.addColorStop(0, '#FFF8EE'); gr.addColorStop(.42, '#F0E2CD'); gr.addColorStop(.5, '#C4AC90'); gr.addColorStop(.62, '#7A5A42'); gr.addColorStop(1, '#3B271B');
    g.fillStyle = gr; g.fillRect(0, 0, w, h);
    g.fillStyle = '#FFFFFF'; g.fillRect(60, 30, 34, 120); g.fillRect(300, 40, 22, 110); g.fillRect(150, 20, 110, 30);
    g.fillStyle = 'rgba(255,244,228,.9)'; g.fillRect(400, 60, 60, 70);
    g.fillStyle = 'rgba(70,44,28,.85)'; g.fillRect(200, 60, 40, 80); g.fillRect(470, 40, 30, 90);
  });
  tex.mapping = THREE.EquirectangularReflectionMapping;
  const pm = new THREE.PMREMGenerator(renderer);
  scene.environment = pm.fromEquirectangular(tex).texture; pm.dispose(); tex.dispose();
  const key = new THREE.DirectionalLight('#FFF1E0', 1.35); key.position.set(-1, 2.2, 1.6); scene.add(key);
  const rim = new THREE.DirectionalLight('#FFE2C4', .7); rim.position.set(1.6, 1.2, -1.4); scene.add(rim);
  scene.add(new THREE.HemisphereLight('#FFF4E6', '#6E4A33', .45));
}

function makeRenderer(cv, opts = {}) {
  const r = new THREE.WebGLRenderer({canvas: cv, antialias: true, alpha: true, powerPreference: 'high-performance', ...opts});
  r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.08;
  r.setClearColor(0x000000, 0); return r;
}

function holderFor(m) {
  const model = MAKE[m](), holder = new THREE.Group(), tilt = new THREE.Group(), spin = new THREE.Group();
  holder.add(tilt); tilt.add(spin); spin.add(model.g); model.g.position.y = -model.h / 2; tilt.rotation.x = TILT[m]; spin.rotation.y = YAW[m];
  return {m, model, holder, tilt, spin, yaw: 0, vel: 0};
}

async function fontsReady() {
  try { await Promise.race([Promise.all(['italic 600 40px "Playfair Display"', '800 40px "Big Shoulders Display"', '600 20px "Be Vietnam Pro"'].map(f => document.fonts.load(f))),
    new Promise(r => setTimeout(r, 2500))]); } catch (e) { /* dùng phông dự phòng */ }
}

// ---------- chế độ chụp ảnh dự phòng: ?shot=phin ----------
async function shot(m) {
  await fontsReady();
  const S = 720, cv = document.createElement('canvas'); cv.width = cv.height = S;
  const renderer = makeRenderer(cv, {preserveDrawingBuffer: true}); renderer.setPixelRatio(1); renderer.setSize(S, S, false);
  const scene = new THREE.Scene(); studio(renderer, scene);
  const fov = 24, cam = new THREE.PerspectiveCamera(fov, 1, 10, 20000); cam.position.z = (S / 2) / Math.tan(fov * Math.PI / 360);
  const it = holderFor(m); scene.add(it.holder); it.holder.scale.setScalar(S * FIT[m] / it.model.sz); it.model.update(1.3, 0);
  if (m === 'grinder') {
    const n = 160, pos = new Float32Array(n * 3);
    it.holder.updateMatrixWorld(true); const a = it.model.g.localToWorld(it.model.nozzle.clone());
    for (let i = 0; i < n; i++) { const f = i / n; pos.set([a.x + (Math.random() - .5) * (3 + 8 * f), a.y - f * (a.y + S / 2), 0], i * 3); }
    scene.add(grounds(pos));
  }
  renderer.render(scene, cam);
  window.__shot = cv.toDataURL('image/webp', .9);
}

let DOT;
function grounds(pos) {
  DOT ||= canvasTex(32, 32, (g) => { const r = g.createRadialGradient(16, 16, 0, 16, 16, 16); r.addColorStop(0, 'rgba(255,255,255,1)');
    r.addColorStop(.6, 'rgba(255,255,255,.9)'); r.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = r; g.fillRect(0, 0, 32, 32); });
  const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const pts = new THREE.Points(geo, new THREE.PointsMaterial({color: '#4E2A15', size: 3.6, sizeAttenuation: false, map: DOT, transparent: true, depthWrite: false}));
  pts.frustumCulled = false; return pts;
}

// ---------- trang ----------
async function main() {
  const canvas = document.getElementById('hd3d'), stages = [...document.querySelectorAll('.hd-stage[data-m]')];
  if (!canvas || !stages.length) return;
  // máy không có WebGL2 thì giữ ảnh dự phòng, không báo lỗi
  let renderer, gl = null;
  try { gl = canvas.getContext('webgl2', {antialias: true, alpha: true, powerPreference: 'high-performance'}); } catch (e) { /* bỏ qua */ }
  if (!gl) return;
  try { renderer = makeRenderer(canvas, {context: gl}); } catch (e) { return; }
  await fontsReady();
  const scene = new THREE.Scene(); studio(renderer, scene);
  const fov = 24, cam = new THREE.PerspectiveCamera(fov, 1, 10, 40000);
  const items = stages.map(el => { const it = holderFor(el.dataset.m); it.el = el; scene.add(it.holder); return it; });
  const byM = Object.fromEntries(items.map(it => [it.m, it]));

  // dòng bột rơi từ cối xay xuống phin
  const N = 720, sp = new Float32Array(N * 3), ph = new Float32Array(N), jit = new Float32Array(N), spd = new Float32Array(N);
  for (let i = 0; i < N; i++) { ph[i] = Math.random(); jit[i] = Math.random() * 2 - 1; spd[i] = .8 + Math.random() * .4; }
  const stream = grounds(sp); scene.add(stream);
  // nền tối: hạt bột sáng màu hơn để vẫn thấy dòng bột rơi
  const mq = matchMedia('(prefers-color-scheme: dark)');
  const tone = () => { const c = getComputedStyle(document.body).backgroundColor.match(/\d+/g) || [255, 255, 255];
    const dark = (+c[0] * .3 + +c[1] * .59 + +c[2] * .11) < 110; stream.material.color.set(dark ? '#B07A50' : '#4E2A15'); kick(); };
  mq.addEventListener?.('change', tone); new MutationObserver(tone).observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme', 'class']});
  const A = new THREE.Vector3(), B = new THREE.Vector3();

  // kéo để xoay
  for (const it of items) {
    let px = null, last = 0;
    it.el.addEventListener('pointerdown', e => { px = e.clientX; last = performance.now(); it.el.setPointerCapture?.(e.pointerId); kick(); });
    it.el.addEventListener('pointermove', e => { if (px === null) return; const dx = e.clientX - px; px = e.clientX; it.yaw += dx * .012;
      const now = performance.now(); it.vel = dx * .012 / Math.max(8, now - last) * 16; last = now; kick(); });
    const up = () => { px = null; };
    it.el.addEventListener('pointerup', up); it.el.addEventListener('pointercancel', up);
  }

  // Khung vẽ nằm trong lớp .hd-3d phủ cả nội dung trang, mỗi khung hình dịch xuống đúng vị trí đang xem.
  // Giữa hai khung hình, khung vẽ cuộn cùng nội dung nên mô hình không bị trễ so với ô của nó khi cuộn nhanh.
  const box = canvas.parentElement;
  let W = 0, H = 0, running = false, t0 = performance.now(), ready = false, drawn = false, lost = false;
  function size(w, h) {
    if (w === W && h === H) return;
    W = w; H = h; canvas.style.height = h + 'px';
    renderer.setPixelRatio(Math.min(devicePixelRatio || 1, w < 700 ? 1.6 : 2)); renderer.setSize(w, h, false);
    cam.aspect = w / h; cam.position.set(0, 0, (h / 2) / Math.tan(fov * Math.PI / 360)); cam.far = cam.position.z * 6; cam.updateProjectionMatrix();
  }
  canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); lost = true; document.documentElement.classList.remove('r3d'); });

  function frame(now) {
    if (lost) { running = false; return; }
    const b = box.getBoundingClientRect(), vh = innerHeight;
    if (b.width < 1 || b.height < 1) { running = false; return; }
    const h = Math.round(Math.min(vh, b.height)), ty = Math.round(Math.max(0, Math.min(b.height - h, -b.top)));
    const top = b.top + ty, left = b.left;
    const t = REDUCE ? 1.3 : (now - t0) / 1000;
    let any = false;
    const rects = items.map(it => it.el.getBoundingClientRect());
    size(Math.round(b.width), h);
    canvas.style.transform = `translate3d(0,${ty}px,0)`;
    items.forEach((it, i) => {
      const r = rects[i], cy = r.top + r.height / 2 - top, cx = r.left + r.width / 2 - left;
      const vis = r.width > 0 && r.bottom > -vh * .3 && r.top < vh * 1.3;
      it.holder.visible = vis;
      it.holder.position.set(cx - W / 2, H / 2 - cy, 0);
      it.holder.scale.setScalar(Math.max(1, r.height) * FIT[it.m] / it.model.sz);
      if (!vis) return; any = true;
      const p = Math.max(-1.2, Math.min(1.2, (r.top + r.height / 2 - vh / 2) / vh));
      if (!REDUCE) { it.yaw += it.vel; it.vel *= .92; }
      it.spin.rotation.y = YAW[it.m] + it.yaw + p * .5;
      it.model.update(t, p);
    });
    const gr = byM.grinder, phn = byM.phin;
    stream.visible = !!gr && (gr.holder.visible || (phn && phn.holder.visible));
    if (stream.visible) {
      gr.holder.updateMatrixWorld(true); gr.model.g.localToWorld(A.copy(gr.model.nozzle));
      if (phn) { phn.holder.updateMatrixWorld(true); phn.model.g.localToWorld(B.copy(phn.model.mouth)); } else B.set(A.x, A.y - H, A.z);
      const tt = REDUCE ? 0 : t * .55;
      for (let i = 0; i < N; i++) {
        const f = (ph[i] + tt * spd[i]) % 1, sprd = 2.5 + 9 * f * f;
        sp[i * 3] = A.x + (B.x - A.x) * f + jit[i] * sprd; sp[i * 3 + 1] = A.y + (B.y - A.y) * f; sp[i * 3 + 2] = A.z + (B.z - A.z) * f + jit[(i * 7) % N] * sprd * .5;
      }
      stream.geometry.attributes.position.needsUpdate = true;
    }
    if (any || drawn) {
      renderer.render(scene, cam); drawn = any;
      if (any && !ready) { ready = true; document.documentElement.classList.add('r3d'); }
    }
    if (any && !REDUCE) requestAnimationFrame(frame); else running = false;
  }
  function kick() { if (!running) { running = true; requestAnimationFrame(frame); } }
  addEventListener('scroll', kick, {passive: true}); addEventListener('resize', kick);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) kick(); });
  tone();
}

if (SHOT) shot(SHOT); else main();

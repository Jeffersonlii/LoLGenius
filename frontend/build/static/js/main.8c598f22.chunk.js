(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{114:function(e,t,r){"use strict";r.r(t);var n=r(0),c=r.n(n),a=r(30),i=r.n(a),s=(r(76),r(77),r(68)),o=r(14),l=r(128),j=r(115),d=r(22),h=r(21),u=(r(78),r(130)),b=r(3),O=r(131),f=r(126),x=r(127),p=r(64),g=r.n(p),m=r(63),v=r.n(m),w=r(132),y=r(129),k=r(4),L=r(66),S=r.n(L),C=(r(97),r(1));var F=function(){return Object(C.jsxs)("div",{id:"mi-host",children:[Object(C.jsxs)("div",{id:"data-features",children:[Object(C.jsx)("h1",{children:"Data Features"}),Object(C.jsx)("p",{children:"Data is collected via the Riot Games API, currently 20 features are used to train the model"}),Object(C.jsxs)("ul",{children:[Object(C.jsx)("li",{children:"10 features for each player's MMR (collected via whatismymmr API)"}),Object(C.jsx)("li",{children:"10 features for each player's Tilt Score"}),Object(C.jsx)("ul",{children:Object(C.jsx)("li",{children:"Calculated as the weighted sum of the player's performance in their last 5 games"})})]}),Object(C.jsxs)("p",{children:[" ","These features were selected on the fundemental fact that the team with the better players win on average"]}),Object(C.jsxs)("p",{children:[" ","Data was collected in 16 hours and resulting in 850 total data points"]})]}),Object(C.jsxs)("div",{id:"model",children:[Object(C.jsx)("h1",{children:"Model"}),Object(C.jsx)("p",{children:"The machine learning model used is a neural network with 3 hidden layes of size 8, with relu activation"}),Object(C.jsx)("h2",{children:"Summaries"}),Object(C.jsx)("h3",{children:"Training Set Accuracy"})," ",Object(C.jsx)("code",{children:Object(C.jsx)("pre",{children:"\n              precision    recall  f1-score   support\n\n       False       0.81      0.74      0.77       294\n        True       0.76      0.83      0.79       299\n\n    accuracy                           0.78       593\n   macro avg       0.79      0.78      0.78       593\nweighted avg       0.79      0.78      0.78       593\n                                \n                        "})}),Object(C.jsx)("h3",{children:"Validation Set Accuracy"}),Object(C.jsx)("code",{children:Object(C.jsx)("pre",{children:"\n              precision    recall  f1-score   support\n\n       False       0.78      0.71      0.74       131\n        True       0.72      0.79      0.75       124\n\n    accuracy                           0.75       255\n   macro avg       0.75      0.75      0.75       255\nweighted avg       0.75      0.75      0.75       255\n                                \n                        "})})]})]})};var P=function(){var e=n.useState(""),t=Object(h.a)(e,2),r=t[0],c=t[1],a=n.useState(!1),i=Object(h.a)(a,2),s=i[0],o=i[1],l=n.useState(void 0),j=Object(h.a)(l,2),p=j[0],m=j[1],L=n.useState(!1),P=Object(h.a)(L,2),T=P[0],A=P[1],I=n.useState(!0),D=Object(h.a)(I,2),M=D[0],_=D[1];return Object(C.jsxs)("div",{id:"host",children:[Object(C.jsx)("section",{id:"title-section",children:"LoL Genius"}),Object(C.jsxs)("section",{id:"input-area",children:[Object(C.jsx)(u.a,{value:r,onChange:function(e){return c(e.target.value)},size:b.d.large,placeholder:"Summoner Name",clearOnEscape:!0,place:!0}),Object(C.jsx)(O.a,{disabled:s,onClick:function(){o(!0),m(void 0),v.a.get("/api/winprob-by-summoner/".concat(""===r?"%20":r.replace(/\s/g,"%20"))).then((function(e){m(Object(d.a)(Object(d.a)({},e.data),{},{error:!1})),o(!1)})).catch((function(e){m(Object(d.a)(Object(d.a)({},e.response.data),{},{error:!0})),o(!1)}))},children:"Predict"})]}),Object(C.jsxs)("section",{id:"result-area",children:[s&&Object(C.jsx)(w.a,{}),p&&(p.error?Object(C.jsx)(u.a,{value:p.msg,error:!0}):p.win?Object(C.jsx)(u.a,{value:"Win! \ud83d\ude42",positive:!0}):Object(C.jsx)(u.a,{value:"Loss \ud83d\ude43",error:!0}))]}),Object(C.jsxs)("section",{id:"desc-area",children:["Enter your League of Legends summoner name and LoLGenius predict the outcome of your current game! (NA Only)",[Object(C.jsxs)(C.Fragment,{children:["Powered by"," ",Object(C.jsx)("a",{href:"blah doesnt matter",onClick:function(e){e.preventDefault(),A(!0)},children:"machine learning"}),"!"]}),"73% accurate!"].map((function(e){return Object(C.jsx)(f.a,{artwork:function(e){return Object(C.jsx)(g.a,Object(d.a)({},e))},children:Object(C.jsx)(x.a,{children:e})})}))]}),Object(C.jsxs)("footer",{children:[Object(C.jsxs)("div",{id:"socials",children:[Object(C.jsx)("a",{href:"https://jeffersonli.dev/",target:"_blank",rel:"noreferrer",children:"More"}),Object(C.jsx)("a",{href:"https://www.linkedin.com/in/jeffersonlii/",target:"_blank",rel:"noreferrer",children:"LinkedIn"}),Object(C.jsx)("a",{href:"https://github.com/Jeffersonlii",target:"_blank",rel:"noreferrer",children:"GitHub"}),Object(C.jsx)("a",{href:"https://github.com/Jeffersonlii/LoLGenius",target:"_blank",rel:"noreferrer",children:"Source Code"})]}),"\xa9",(new Date).getFullYear()," Jefferson Li. All rights reserved."]}),Object(C.jsx)(y.a,{isOpen:T,autoFocus:!0,onClose:function(){return A(!1)},anchor:k.a.bottom,showBackdrop:!1,size:"auto",children:Object(C.jsx)(F,{})}),M&&Object(C.jsxs)("div",{id:"message",children:[Object(C.jsxs)("p",{children:["Currently not working, waiting for Riot to approve a production API key \xa0\xa0",Object(C.jsx)("a",{href:"https://developer.riotgames.com/docs/portal#product-registration_application-process",target:"_blank",rel:"noreferrer",s:!0,children:"More Info"})]}),Object(C.jsx)("div",{class:"del-icon",onClick:function(){_(!1)},children:Object(C.jsx)(S.a,{size:32})})]})]})},T=new s.a;var A=function(){return Object(C.jsx)(o.Provider,{value:T,children:Object(C.jsx)(l.a,{theme:j.a,children:Object(C.jsx)(P,{})})})},I=function(e){e&&e instanceof Function&&r.e(3).then(r.bind(null,133)).then((function(t){var r=t.getCLS,n=t.getFID,c=t.getFCP,a=t.getLCP,i=t.getTTFB;r(e),n(e),c(e),a(e),i(e)}))};i.a.render(Object(C.jsx)(c.a.StrictMode,{children:Object(C.jsx)(A,{})}),document.getElementById("root")),I()},76:function(e,t,r){},77:function(e,t,r){},78:function(e,t,r){},97:function(e,t,r){}},[[114,1,2]]]);
//# sourceMappingURL=main.8c598f22.chunk.js.map
# GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding

## sec:preamble preamble
_Pages 1-1_

GeoAnchor: Collaborative Reasoning via Latent
Decomposition for 3D Spatial Understanding
Hao Li1,2, Han Fang2, Zixin Pan2,4, Xin Wei2, Hongbo Sun2, Jinglin Xu3, Zhiyu Lin2, Ye Yuan2, Zhongjiang He2,
Yu Yu1,∗, Hao Sun2,∗
1Shanghai Jiao Tong University, 2Xingchen AGI Lab, China Telecom Artificial Intelligence Technology
(Beijing) Co., Ltd, 3University of Science and Technology Beijing, 4The Hong Kong University of Science
and Technology (Guangzhou)
Although multimodal large language models (MLLMs) have achieved remarkable progress, understanding
3D spatial relationships from 2D images remains a critical challenge. Existing methods primarily rely on
symbolic text tokens, which inherently lack the fidelity to represent continuous geometric information. While
recent methods use latent representations to enhance reasoning, relying on a single latent type cannot adapt
to the diversity of spatial tasks, leading to misalignment in complex geometric scenarios. To address these
limitations, we propose GeoAnchor, an interleaved text-latent reasoning framework. GeoAnchor decomposes
3D spatial information into three complementary components: position latents for object grounding, direction
latents for relational orientation, and geometry latents for scene structure. These components are recombined
in a structured space to construct local evidence while capturing global context, enabling dynamic and
interpretable reasoning. Furthermore, we introduce a collaborative training strategy that guides the model
from local spatial perception to comprehensive 3D understanding. Extensive experiments on diverse and
complex 3D reasoning tasks demonstrate that GeoAnchor outperforms the state of the art, validating its
effectiveness and generalization capabilities.
Links: https://github.com/JerryPW/GeoAnchor
Date: July 14, 2026

## sec:introduction Introduction
_Pages 1-3_

Multimodal large language models (MLLMs) have demonstrated remarkable performance across a wide range
of 2D vision-language tasks (Yang et al., 2025a; Liu et al., 2024; Google DeepMind, 2025). However, a
critical capability remains underdeveloped: 3D spatial reasoning. Humans naturally infer depth, relative
positions, and occlusions from visual scenes, yet existing MLLMs still struggle with complex spatial reasoning
tasks (Cheng et al., 2024; Zhang et al., 2025c). This deficiency in such 3D understanding impedes their
deployment in geometry-sensitive downstream applications, including robotics (Kim et al., 2024; Pertsch
et al., 2025), autonomous driving (Zhou et al., 2025; Hwang et al., 2024; Ye et al., 2025), and VR/AR
systems (Afzal et al., 2025). Existing efforts to enhance spatial reasoning capabilities generally follow two
paradigms. The first paradigm leverages large-scale datasets, enabling models to implicitly learn 3D relational
patterns through statistical regularities in the data (Cheng et al., 2024; Chen et al., 2024; Li et al., 2025c;
Yang et al., 2025b; Cai et al., 2025). The second paradigm augments 2D visual inputs with explicit 3D or
2.5D signals (e.g., point clouds, depth maps, or cognitive maps), thereby providing richer global geometric
structure for the model (Mao et al., 2025; Zheng et al., 2025; Huang et al., 2025; Wu et al., 2025a; Fan et al.,
2025). Despite their contributions, both methods are constrained by reasoning within a discrete text space:
geometric evidence is verbalized into discrete tokens, inevitably leading to the loss of fine-grained spatial cues
and biasing reasoning toward linguistic priors. Furthermore, the discrete nature of text tokens fails to capture
the continuous characteristics of the physical world, rendering autoregressive generation unreliable for precise
numerical tasks like distance estimation and object localization (Wen et al., 2025).
Recent studies have explored latent reasoning to address the inherent limitations of text-based reasoning. By
conducting intermediate reasoning within non-linguistic latent representations, rather than verbalizing every
step in natural language, these methods preserve continuous semantic information, facilitating more coherent
∗Corresponding Authors
arXiv:2607.13454v2 [cs.CV] 28 Jul 2026
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
(a) Text-Only Reasoning
(b) Single Latent Reasoning
Which is closer to the viewer
MLLM
“ The plant is…
Wait, … maybe
the sofa?”
“They look close…”
Single
Latent
Which is closer to the viewer
(c) Decomposed Latent Reasoning (Ours)
Which is closer to the viewer
Local objects analysis
Global geometry context
MLLM
Factorized interpretable cues
“ The plant is closer, followed by the sofa, then the bookshelf.”
Lost continuous geometry
Lack interpretable cues
Position Latent
(Local)
Direction Latent
(Local)
Geometry Latent
(Global)
MLLM
Figure 1 Existing methods suffer from information loss due to verbalization or limited interpretability from entangled
latents.
In contrast, GeoAnchor decomposes reasoning into position, direction, and geometry factors to enable
structured, interpretable local-plus-global reasoning.
multimodal reasoning (Qin et al., 2025; Yang et al., 2025d; Li et al., 2025a; Wang et al., 2025b). When applied
to spatial reasoning, researchers typically design geometrically-aware latent tokens supervised by geometric
priors (e.g., depth maps) (Bigverdi et al., 2025; Liu et al., 2025a). Nevertheless, directly adopting such latent
tokens for 3D spatial reasoning introduces two key limitations. First, existing methods rely on a single type of
latent representation, which struggles to accommodate the diverse demands of spatial reasoning. For example,
while latents decoded into depth maps effectively capture near-far object relationships, they are limited in
representing complex spatial information beyond depth. Second, these latent representations primarily focus
on global geometric context, offering limited insight into local object interactions. Consequently, when tasked
with precise tasks such as estimating the absolute distance between two points, global latents fail to provide
sufficient local evidence.
In this work, we propose GeoAnchor, a text–latent interleaved framework that avoids compressing geometric
information into a single entangled latent representation or verbalizing it into discrete text tokens. Instead,
GeoAnchor decomposes 3D spatial information into three complementary basic latent components: a position
token for precise object grounding, a direction token for modeling relational orientation, and a geometry token
for capturing global scene structure. The position and direction tokens provide explicit and traceable local
evidence for target objects, while the geometry latent encodes global scene context. This design enables
dynamic recombination of these latents within a structured space, eliminating the need for a uniform latent
token design across all types of questions. Consequently, GeoAnchor achieves an interpretable latent reasoning
process that adaptively accommodates the diverse demands of spatial reasoning tasks.
To enable such structured reasoning, we introduce a four-stage collaborative training strategy. First, we
align the model with local 3D perception using large-scale object-grounding data, thereby establishing robust
object-level spatial cues. Second, we jointly optimize local and global latent components, facilitating the
evolution of reasoning from local perception to holistic spatial understanding. Third, we refine the latent
representations via text-only supervision, encouraging the model to internalize spatial reasoning logic without
relying on intermediate guidance. Finally, we incorporate reinforcement learning (Shao et al., 2024) with
pattern-specific rewards to enable adaptive selection of latent tokens, allowing the model to dynamically switch
between local-only and local-plus-global reasoning patterns. Built on Qwen3-VL-2B (Yang et al., 2025a),
GeoAnchor achieves state-of-the-art performance: 68.4% and 69.7% accuracy on the SPAR-Bench (Zhang
et al., 2025b) and SPBench (Li et al., 2025c), respectively. It surpasses the base model by a significant 21.2%
margin, and outperforms GPT-4o (Hurst et al., 2024) and Gemini-2.5-Flash (Comanici et al., 2025) by 18.0%
and 13.6%, respectively. Moreover, a 10.7% performance gain on the out-of-domain ViewSpatial Bench (Li
et al., 2025b) confirms GeoAnchor’s robust generalization capability.
The main contributions of this paper are summarized as follows:
• We propose GeoAnchor, a new 3D spatial reasoning framework that decomposes geometric reasoning into
three complementary and physically meaningful latent components: position, direction, and geometry.
Such a design enables dynamic latent recombination toward interpretable and query-adaptive spatial
understanding.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
• We introduce a collaborative four-stage training strategy that enables the model to perform structured
local-plus-global spatial reasoning and adaptively select latent tokens.
• Extensive experiments on challenging 3D reasoning benchmarks, including SPAR-Bench, SPBench and
ViewSpatial, demonstrate that GeoAnchor surpasses the base model by 21.2% and outperforms GPT-4o
and Gemini-2.5-Flash, showing competitive performance in 3D reasoning tasks.
Related Works
2.1
Text-Based Visual Spatial Reasoning
With rapid progress in embodied intelligence, spatial understanding in MLLMs has drawn increasing attention.
Recent efforts to improve spatial reasoning in MLLMs can be broadly grouped into two categories. The first
leverages curated datasets and multi-stage training to learn spatial relations from large-scale examples (Chen
et al., 2024; Li et al., 2025c; Yang et al., 2025b; Cai et al., 2025; Elmaaroufi et al., 2025; Liu et al., 2025b; Zhan
et al., 2025; Batra et al., 2025; Ouyang et al., 2025). For example, SpatialLadder (Li et al., 2025c) constructs
SpatialLadder-26k and adopts a progressive curriculum from perception to reasoning. SpaceR (Ouyang et al.,
2025) further improves spatial reasoning by introducing spatially tailored reward signals in reinforcement
learning. However, direct training often promotes memorization over reasoning, limiting generalization.
Recognizing the limitations of purely 2D priors, the second category augments the input with 2.5D or 3D
information to strengthen global spatial understanding (Mao et al., 2025; Zheng et al., 2025; Huang et al., 2025;
Wu et al., 2025a; Zhang et al., 2025a; Gholami et al., 2025). For example, SpatialMind (Zhang et al., 2025a)
encodes object locations on a 2D grid to form a cognitive map that is provided as additional input. Spatial-
MLLM (Wu et al., 2025a) incorporates a frozen geometry encoder (e.g. VGGT) to provide complementary
3D representations. Nevertheless, methods that primarily generate text still struggle to faithfully express
continuous spatial relations in discrete language. This mismatch causes substantial information loss when
continuous geometry is mapped to textual descriptions, ultimately limiting spatial understanding.
2.2
Latent Reasoning
To overcome the limitations of a text-only output modality, one straightforward solution is to “think with
images” (Yang et al., 2025c; Wu et al., 2024, 2025b; Gao et al., 2024). For example, ViLaSR (Wu et al., 2025b)
facilitates spatial localization by rendering auxiliary guide lines, while MindJourney (Yang et al., 2025c)
leverages a diffusion model to synthesize alternative viewpoints and feeds the generated images back into the
model. However, these methods rely heavily on external tools, reducing flexibility and limiting generalization.
Inspired by latent reasoning in LLMs (Butt et al., 2025; Wei et al., 2025; Shen et al., 2025), which replaces
discrete text tokens with self-generated continuous embeddings, several studies have extended latent reasoning
to MLLMs (Ray et al., 2025; Qin et al., 2025; Yang et al., 2025d; Li et al., 2025a; Wang et al., 2025b) and
further to spatial reasoning (Bigverdi et al., 2025; Liu et al., 2025a; Hu et al., 2025; Chen et al., 2025) to
improve reasoning flexibility. LVR (Li et al., 2025a) and Mirage (Yang et al., 2025d) use image supervision
to guide latent tokens, encouraging the model to develop an interleaved visual–textual reasoning process in
latent space. For spatial reasoning, Aurora (Bigverdi et al., 2025) and SSR (Liu et al., 2025a) incorporate
depth maps into latent tokens to strengthen geometric reconstruction. Nevertheless, the complexity of spatial
reasoning is unlikely to be fully captured by a single global latent token. Such a bottleneck often lacks
sufficient capacity and structure for diverse spatial problems, while also reducing interpretability when the
model must resolve heterogeneous geometric relations.

## sec:method Method
_Pages 3-6_

In this section, we present GeoAnchor, a framework designed to tackle complex spatial reasoning tasks via an
interleaved text-latent paradigm. Section 3.1 presents the overall architecture, while Section 3.2 details the
design of decomposed spatial tokens. Section 3.3 then describes the collaborative training strategy, which
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
From the photo frame facing the yellow tower, where is the yellow deer sculpture located?
Sure, to answer this, I
first need to locate the
yellow deer sculpture…
I need to determine the
direction from the
photo to the tower…
Based on these cues, I
can build a rough spatial
layout of the scene…
the
right.
Token
Sequence
Vision
System/
Instruction
Text
Local Atomic
3D Cues
Local Atomic
3D Cues
Global Geometry
Context
Text
Text
Decoder
position
direction
Decoder
3D Foundation Model
(e.g., VGGT)
Full VGGT Feature
Global
Token 𝑖
Similarity
weights
max similarity
Each global token aligns only
with its most similar feature
Global
Tokens
Decoded
Global Tokens
Global Geometry Context
Local Atomic 3D Cues
Depth Map
Back-projection
Downsampling
Soft Coverage
Figure 2 Overview of GeoAnchor. We organize spatial reasoning into two components: (i) obtaining local atomic 3D
cues and (ii) building global geometric context. We replace discrete text-based representations with continuous latent
tokens to encode abstract 3D information. Specifically, local tokens capture object locations and inter-object direction,
whereas the global token encodes the overall scene structure.
facilitates a structured evolution from local perception to holistic spatial understanding. Finally, Section 3.4
summarizes the construction of the grounding and reasoning datasets employed across training stages.
3.1
Text-Latent Interleaved Framework
GeoAnchor employs a text-latent interleaved reasoning framework to address the loss of continuous 3D
information inherent in relying solely on discrete textual representations. Specifically, the model utilizes
discrete text tokens for semantic planning and logical reasoning, while leveraging latent representations to
encode and capture over continuous, multi-grained 3D spatial cues. The overall structure is illustrated in
Figure 2. Given an image I and query Q, GeoAnchor outputs the reasoning trajectory O, which consists of
an interleaved sequence of text and latent tokens:
O = t1 ⊕z1 ⊕· · · ⊕zk−1 ⊕tk,
(1)
where t = {t1, . . . , tk} denotes the sequence of text tokens, and z = {z1, . . . , zk−1} represents the sequence of
latent tokens.
Unlike text tokens retrieved via embedding lookups, each latent token zi is defined as a fixed-length sequence
of M continuous hidden states, i.e., zi = {hi,1, hi,2, . . . , hi,M}, where each hi,j ∈Rd resides in the model’s
hidden space. Specifically, at the j-th internal step of generating zi, the MLLM fθ(·) produces the hidden
state hi,j conditioned on the preceding context:
hi,j = f hidden
(Q, I, O<zi, hi,1:j−1),
(2)
where O<zi denotes the entire reasoning trajectory generated before zi, and hi,1:j−1 denotes the internal
hidden states generated up to step j −1. However, the output hidden-state space and the input embedding
space typically lie on different manifolds. Directly feeding hi,j back into the input trajectory without alignment
can lead to severe latent drift and autoregressive instability (Yue et al., 2025). To bridge this gap, we introduce
a latent projector P(·) that maps the output hidden state into the input embedding space. Specifically, the
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
projected continuous embedding ei,j ∈Rd is computed as:
ei,j = P(hi,j) = LayerNorm
hi,j + MLP
 LayerNorm(hi,j)
(3)
The projected embedding ei,j is then fed back as the input representation for the subsequent generation step,
ensuring a consistent and stable reasoning trajectory.
3.2
Decomposed Spatial Tokens
To address the limitation that a single latent type struggles to handle diverse spatial reasoning tasks, we
decompose the spatial reasoning process into two distinct stages: obtaining local atomic 3D cues and building
global geometric context. Accordingly, we introduce three complementary latent tokens: the position token
zpos, the direction token zdir, and the geometry token zgeo. The first two serve as local tokens by encoding
atomic 3D cues for target objects, including object grounding and relational orientation, whereas the geometry
token is a global token to capture the overall scene structure. By disentangling the uniform latent representation
into structured 3D evidence with distinct functions, the model can flexibly compose diverse spatial evidence
within the latent space, thereby enabling more interpretable spatial reasoning.
Explicit Supervision of Local 3D Cues. In conventional text-based reasoning, local spatial information, such
as positional coordinates and directional vectors, is typically represented as discrete numerical text tokens.
To preserve the continuity of 3D spatial information, we encode these cues into latent tokens and employ
decoders to map them into numerical coordinates for alignment. We map latent tokens to the target 3D space
using lightweight linear heads, similar to the text prediction module. Given that each latent token comprises
a sequence of hidden states (Section 3.1), zpos and zdir are defined as:
zpos = {hpos
, . . . , hpos
lpos},
zdir = {hdir
1 , . . . , hdir
ldir},
(4)
where hpos
and hdir
∈RD are the hidden states at the j-th internal step, and lpos and ldir denote the numbers
of hidden states for each latent token. The hidden states within each latent token are first averaged along the
sequence dimension and then mapped to 3D outputs through two separate linear heads:
ˆp = Wpos
lpos
lpos
j=1
hpos
ˆd = Wdir
ldir
ldir
j=1
hdir
j ,
(5)
where Wpos, Wdir ∈R3×D are projection heads, while ˆp ∈R3 and ˆd ∈R3 denote the predicted position and
direction, respectively. To explicitly supervise these two tokens, we apply the Smooth L1 loss (Girshick, 2015)
for position prediction and the cosine similarity loss for direction prediction:
Lpos =
2(ˆp −p)2,
if |ˆp −p| < 1.0
|ˆp −p| −1
otherwise
, Ldir = 1 −
ˆd · d
∥ˆd∥2∥d∥2
(6)
where p and d denote the ground-truth 3D position coordinates and direction vectors, respectively.
Coverage-Based Supervision of Global Geometry. We supervise the global token zgeo using geometry features
from the last layer of the VGGT model (Wang et al., 2025a), since these features can be decoded into 3D point
clouds and inherently capture global geometric structure. However, VGGT generates a high-resolution feature
grid, whereas the global token is a compact representation composed of a few hidden states. Consequently,
enforcing strict token-wise alignment would impose overly fine-grained constraints on the global token,
potentially undermining its role as a compact representation of scene-level geometry. Therefore, a coarse
soft-coverage alignment strategy is adopted instead of strict dense alignment.
We first transform the dense VGGT feature map into a supervision feature by multi-scale average pooling.
Specifically, for the final VGGT feature map of size H × W × D, average pooling is applied at multiple spatial
resolutions {r1, . . . , rL}. Each pooled feature grid is flattened into r2
l feature vectors, and the vectors from all
scales are concatenated to form the coarse-grained VGGT feature map V ∈Rlvggt×D, where lvggt = PL
l=1 r2
l .
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Text
Position
Direction
VLM
Where is the fridge in
3D, and which way is
the door from it?
Grounding Task
VLM
Stage 2: Spatial Latent Reasoning
Stage 1: Local Perception Warm-up
Position
Direction
Text
Geometry
Spatial Relation
Value Estimation
View Change
Stage 3: Latent Relaxation
VLM
Text Supervision ONLY
Latent Supervision Disabled:
Spatial Reasoning Tasks:
Stage 4: Adaptive Latent Reinforcement Learning
Policy

## sec:model Model
_Pages 6-8_

Reference Model
Spatial Tasks
Update Policy
…<pos>…<dir>…
<answer>C</answer>
A: Local Reasoning
B: Local & Global Reasoning
…<pos>…<dir>…<geo>…
<answer>A</answer>
Calculate the accuracy for pattern A and B
𝐴𝑐𝑐$ = 𝑛$
%&''(%$ + 𝜅𝐴𝑐𝑐$
)*+$
𝑛$ + 𝜅
, 𝑡∈{𝐴, 𝐵}
𝑟= 𝑟,&'-.$ + 𝑟.%% + 𝑟/.$$('0 ⋅𝟏[𝑡= 𝑡∗]
𝑡∗= 𝑎𝑟𝑔max
$∈{4,6} 𝐴𝑐𝑐$
Promote patterns with higher accuracy
Figure 3 Overview of the collaborative training framework of GeoAnchor. The model is trained in a coarse-to-fine manner,
evolving from local perception to holistic spatial understanding, then to latent relaxation without explicit latent
supervision, and finally to an adaptive latent reinforcement learning stage that encourages dynamic reasoning patterns.
In parallel, the global token zgeo is projected into geometry tokens G ∈Rlgeo×D via a linear layer, where lgeo
denotes the number of geometry tokens. We then compute token similarities as:
Ai,j = ⟨vi, gj⟩
uj =
lvggt
lvggt
i=1
exp(Ai,j)
Plgeo
j′=1 exp(Ai,j′)
(7)
where vi ∈RD is the i-th coarse-grained VGGT feature and gj ∈RD is the j-th geometry token, τ represents
the temperature parameter, and uj denotes the average soft assignment received by the j-th geometry token.
The alignment loss is defined as:
Lgeo = −
lvggt
lvggt
i=1
log
lgeo
j=1
exp(Ai,j) + λbal
lgeo
j=1
log uj −log
lgeo
(8)
The first term encourages that every VGGT feature aligns with at least one geometry token, thereby achieving
coarse coverage without dense alignment. The second term enforces balanced token utilization to prevent
representation collapse, controlled by the coefficient λbal. Collectively, these objectives guide the geometry
tokens to capture complementary global evidence that integrates seamlessly with local evidence for downstream
reasoning.
3.3
Collaborative Training Strategy
To effectively train the model for spatial reasoning with latent tokens, we design a collaborative training
framework that systematically builds up spatial intelligence, as illustrated in Figure 3.
Stage 1: Local Perception Warm-up. We first warm up the base model by training its 3D grounding capability.
Specifically, we construct a large-scale 3D grounding dataset and train the model with two complementary
abilities: predicting the 3D position of a target object and predicting the relative direction between two
objects. By learning these two signals jointly, the model is encouraged to collaboratively organize the local
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
tokens into coherent local spatial evidence. The local tokens are optimized with Lpos and Ldir, while the text
tokens are trained with the next-token prediction loss LNTP. Formally, the training objective for Stage 1 is:
Lstage1 = λtLNTP + λl (Lpos + Ldir) ,
(9)
where λt and λl are the corresponding balance coefficients.
Stage 2: Spatial Latent Reasoning. In the second stage, the model is further trained on a spatial reasoning
dataset covering diverse spatial tasks. During this stage, it learns to conduct an interpretable spatial reasoning
process in the latent space by collaboratively integrating local 3D cues with global geometric context. It also
learns to dynamically utilize the position and the direction tokens according to the input question, thereby
developing a basic ability for adaptive latent token selection. The position, direction, and geometry tokens
are supervised by their corresponding losses. Denoting λg as the coefficient for Lgeo, the total loss for Stage 2
is defined as follows:
Lstage2 = λtLNTP + λl(Lpos + Ldir) + λgLgeo.
(10)
Stage 3: Latent Relaxation. Although the explicit supervision in Stage 2 effectively aligns the latent tokens
with 3D information, overly strong alignment may shift them away from the original language manifold and
hinder subsequent reasoning. Inspired by (Yang et al., 2025d; Ray et al., 2025), we therefore introduce a
latent relaxation stage that removes explicit latent supervision and retains only text supervision. λl and λg
are set to 0, and the latent tokens are thus updated only through the text supervision, which helps the learned
spatial representations better fit the language distribution while preserving the spatial information acquired
in earlier stages.
Stage 4: Adaptive Latent Reinforcement Learning. Although the preceding stages enable reasoning with latent
tokens, they still rely on a fixed usage pattern where both local and global tokens are invoked for every
query. However, different spatial reasoning tasks require different levels of spatial information, making such
fixed invocation suboptimal. To address this issue, we introduce an adaptive latent reinforcement learning
stage based on Group Relative Policy Optimization (GRPO) (Shao et al., 2024). We consider two reasoning
patterns: local-only and local-plus-global. Then in addition to format and accuracy rewards, we introduce
a pattern-specific reward to evaluate the effectiveness of each reasoning pattern. Within each group, the
model samples N responses, each generated by randomly selecting one of the two patterns. For pattern
t ∈{local, local+global}, its effectiveness is estimated as:
Acct = ncorrect
+ κAcchist
nt + κ
, Acchist
←(1 −µ) Acchist
+ µncorrect
(11)
where nt and ncorrect
denote the numbers of sampled and correct responses under pattern t, respectively,
Acchist
is the EMA-based historical accuracy (Kingma and Ba, 2014), κ is the smoothing coefficient, and µ
is the update rate. The pattern with the higher smoothed accuracy receives an additional pattern reward
rpattern. This encourages the model to use global token only when local reasoning is insufficient, leading to
more efficient and more interpretable reasoning.
3.4
Dataset Construction
We construct two training sets for GeoAnchor: a large-scale 3D grounding dataset for Stage 1 and a spatial
reasoning dataset for the subsequent supervised and reinforcement learning stages. The former provides
explicit supervision for local spatial perception, while the latter supports joint local-global spatial reasoning.
For the grounding dataset, we build on top of ScanNet (Dai et al., 2017) by sampling 10k scenes from its 2.5
million views over 1,500+ scans. For each image, we use Qwen3-VL-32B (Yang et al., 2025a) to identify up to
five objects, along with their descriptions and 2D bounding boxes. We then employ Depth Anything v3 (Lin
et al., 2025) to estimate depth maps and camera poses, and recover the 3D coordinates of the extracted
objects through back-projection. Ground-truth directions are derived from coordinate differences. We further
diversify the queries using point-coordinate, bounding-box, and natural-language formulations, with each
sample involving one to three objects. This process yields 550k 3D grounding samples in total.
For the spatial reasoning dataset, we use SPAR (Zhang et al., 2025b) as the primary data source, since it is
built on ScanNet (Dai et al., 2017), ScanNet++ (Yeshwanth et al., 2023), and Structured3D (Zheng et al.,
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 1 Evaluation Results on Spatial Reasoning Benchmarks. For each metric, bold numbers indicate the best
performance, while underlined numbers represent the second-best performance.
SPAR-Bench
SPBench
ViewSpatial

## sec:model-2 Model
_Pages 8-8_

Param
Avg.
Dep.
Dis.
Prox.
Rel.
View
Avg.
Rel.
Abs.
Avg.
Cam.
Per.
Proprietary Models
GPT-4o (Hurst et al., 2024)
40.1
34.3
43.4
57.1
45.9
31.0
53.4
49.4
56.0
37.5
33.5
43.6
Gemini-2.5-Flash (Comanici et al., 2025)
48.7
37.4
45.2
80.1
63.2
41.0
51.5
44.7
56.0
44.0
43.0
45.5
General Models
MiniCPM-V-4.5 (Yu et al., 2025)
37.7
32.4
32.6
62.1
50.6
29.8
40.9
47.4
36.7
39.0
43.0
32.9
LLaVA-OneVision-1.5 (An et al., 2025)
34.5
29.3
32.6
58.5
40.7
26.7
40.8
45.1
38.0
38.7
40.6
35.3
Qwen3-VL (Yang et al., 2025a)
41.1
32.5
34.6
71.2
62.1
31.5
55.1
47.6
60.0
44.0
44.6
43.1
Molmo2 (Clark et al., 2026)
24.6
16.7
3.2
62.4
48.4
25.1
29.7
47.6
18.1
45.5
46.0
45.1
GLM-4.1V (Hong et al., 2025)
48.0
42.4
53.2
65.6
57.7
34.3
49.1
43.6
52.6
40.4
37.6
44.7
Qwen3.5 (Qwen Team, 2026)
48.6
39.0
53.0
73.8
63.5
33.4
48.8
48.6
48.8
45.6
47.2
43.2
Kimi-VL (Team et al., 2025)
16B-A3B
33.9
28.6
26.7
60.6
44.5
28.3
42.1
40.8
43.0
38.1
36.5
40.4
Internvl3.5 (Wang et al., 2025c)
38B
38.0
31.5
35.5
60.9
58.0
25.5
53.1
49.4
55.5
41.4
43.3
38.6
Specialized Models
G2VLM (Hu et al., 2025) [CVPR’26]
41.7
41.8
66.3
37.7
26.4
24.2
14.3
25.2
7.2
18.3
16.0
21.7
3DThinker (Chen et al., 2025) [CVPR’26]
23.8
15.8
18.6
49.7
24.2
25.1
13.8
32.2
1.7
29.2
27.7
31.5
SpatialLadder (Li et al., 2025c) [ICLR’26]
32.4
22.1
29.8
53.8
43.7
29.5
69.6
81.6
65.0
43.3
41.8
45.4
SpatialMLLM-v1.1 (Wu et al., 2025a) [NeurIPS’25]
33.7
25.3
34.2
53.8
36.5
31.2
54.2
55.7
53.3
39.7
39.8
39.6
ViLaSR (Wu et al., 2025b) [NeurIPS’25]
38.6
28.9
43.1
61.8
46.4
28.2
52.2
54.4
50.8
34.3
33.8
34.9
Aurora (Bigverdi et al., 2025) [CVPR’25]
13B
29.6
26.9
29.0
52.7
21.7
25.7
32.1
36.8
29.0
25.6
26.2
24.7
Qwen3-VL (Yang et al., 2025a) (Baseline Model)
32.4
21.9
24.0
60.6
49.2
28.3
52.9
51.4
54.8
36.3
39.5
37.2
GeoAnchor
68.4
55.5
67.4
80.3
84.6
68.8
69.7
86.7
58.7
47.0
47.5
46.0
Improvement
+36.0
+33.6
+43.4
+19.7
+35.4
+40.5
+16.8
+35.3
+3.9
+10.7
+8.0
+8.8
2020), and provides 7M samples covering diverse spatial tasks. We sample 100k questions from SPAR and use
the bounding boxes provided in the dataset to obtain the ground-truth positions and directions of the target
objects, following the same back-projection procedure as in the grounding dataset. In addition, we extract
global geometric features for each image using VGGT (Wang et al., 2025a). To better cover centimeter-based
answer formats, we further incorporate 5k samples from SpatialLadder-26k (Li et al., 2025c). In total, the
resulting spatial reasoning dataset contains 105k samples.

## sec:experiment Experiment
_Pages 8-9_

4.1
Experimental Setup
Implementation Details. GeoAnchor is built on Qwen3-VL-2B (Yang et al., 2025a), with local token length
lpos = ldir = 2 and global token length lgeo = 8. Stage 1 is trained on the grounding dataset for one epoch
using a batch size of 64 and a learning rate of 1 × 10−4. Stages 2 and 3 are each trained for one epoch on the
spatial reasoning dataset with a batch size of 32 and a learning rate of 2 × 10−5. The loss weights are set to
λt = λl = 1 and λg = 0.1. For global geometry supervision, the VGGT feature map is pooled at L = 3, with
{r1, r2, r3} = {1, 2, 4}. In the RL stage, 8 rollouts are performed per question with a sampling temperature of
1.0, a pattern reward rpattern of 0.5, a KL-divergence coefficient β of 0.01, and a learning rate of 5 × 10−7.
Additional details are provided in the supplementary material.
EvaluationBenchmarksandMetrics. We evaluate GeoAnchor on SPAR-Bench (Zhang et al., 2025b), SPBench (Li
et al., 2025c), and ViewSpatial (Li et al., 2025b), where the first two serve as in-domain benchmarks and the
last assesses out-of-domain generalization. For multiple-choice questions, we directly judge correctness and
report the mean accuracy. For numerical questions, the mean accuracy is computed as the average accuracy
across confidence thresholds from 0.5 to 0.9 with a step size of 0.05.
4.2
Main Results
Table 1 compares GeoAnchor with state-of-the-art models across three benchmarks. Despite its compact
2B parameter size, GeoAnchor outperforms proprietary, open-source, and specialized MLLMs, including
those with up to 38B parameters. On in-domain benchmarks, it achieves state-of-the-art mean accuracy
on both SPAR-Bench (68.4%) and SPBench (69.7%), surpassing the base Qwen3-VL-2B by 36.0% and
16.8%, respectively. While SpatialLadder slightly outperforms GeoAnchor on the SPBench Abs. metric,
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 2 Ablation study on the effectiveness of latent reasoning.
Vanilla SFT trains the model directly on question-answer pairs,
and text CoT follows a “localize-then-reason” paradigm and is
trained entirely in the text modality.

## sec:model-3 Model
_Pages 9-11_

SPAR SPBench ViewSpatial
Avg.
Qwen3-VL-2B (Yang et al., 2025a)
32.4
52.9
36.3
40.5
+ vanilla SFT
56.4
58.1
40.9
51.8
+ text CoT SFT
60.1
52.9
42.2
51.7
Latent Reasoning (Bigverdi et al., 2025)
62.4
57.8
40.5
53.6
local tokens
65.8
66.9
44.4
59.0
global token
63.8
64.3
46.0
58.0
local + global token
67.5
68.8
46.3
60.9
Table 3 Ablation results on the collaborative training
strategy. S1, S2, and S3 represent the three-stage SFT,
and S4 represents the RL stage.
S1 S2 S3
SPAR SPBench ViewSpatial Avg.
w/o rpattern w/ rpattern
63.1
61.9
42.7
55.9
56.5
48.4
33.9
46.3
52.8
41.0
19.8
37.9
67.5
68.8
46.3
60.9
67.8
69.2
46.2
61.1
68.4
69.7
47.0
61.7
Table 4 Ablation of local token interpretability
across position, direction, and mixed questions.
Problem Setting
Position
Direction
Mixed
Position token only
65.2
36.5
55.8
Direction token only
62.9
38.7
53.5
Full local tokens
66.4
39.4
57.0
Table 5 Ablation of VGGT alignment strategies for supervising the
global geometry token.
Alignment
Sampling
SPAR
SPBench
ViewSpatial
Avg.
Dense
Mean Pooling
59.9
66.8
45.5
57.4
Adaptive Pooling
66.9
66.5
44.4
59.3
Linear Interpolation
53.7
60.2
37.3
37.8
Soft Coverage
Multi-Scale Pooling
68.4
69.7
47.0
61.7
its inconsistent performance across other benchmarks suggests a limitation in generalization. Notably, on
the out-of-domain ViewSpatial benchmark, GeoAnchor attains 47.0% mean accuracy, ranking first in both
sub-tasks. The substantial 10.7% gain over the base model demonstrates our method’s robust generalization
capability beyond the training distribution.
4.3
Ablation Experiments
Effects of Different Reasoning Paradigms. Table 2 compares the performance of different reasoning paradigms
on spatial tasks. Compared with vanilla SFT, text CoT SFT does not yield consistent gains across benchmarks,
suggesting that spatial information is difficult to incorporate effectively through textual reasoning. Therefore,
the reasoning process is more easily influenced by language patterns than by geometric evidence. In contrast,
by encoding continuous 3D information into latent tokens, GeoAnchor outperforms both vanilla SFT and
text CoT SFT, indicating that latent reasoning provides a more effective way to leverage spatial information.
Furthermore, GeoAnchor also surpasses the single-latent reasoning baseline. Performance drops when the
model is restricted to one type of analysis, showing that the decomposed token design plays a more important
role than latent reasoning. Our design reduces the semantic burden of a single latent and enables more
task-adaptive use of spatial cues, leading to more interpretable and robust reasoning than a single-latent
design.
Effects of Collaborative Training Stages. Table 3 illustrates the effectiveness of each training stage. Stages 1,
2, and 3 improve the performance by 5.0%, 14.6%, and 23.0%, respectively, validating the effectiveness of
our multi-stage design. Figure 4 shows that Stage 3 yields significantly higher gains than merely extending
Stage 2, confirming its value lies in integrating latent tokens into reasoning rather than additional training
iterations. Moreover, while applying GRPO directly as stage 4 improves in-domain performance, it degrades
out-of-domain results on ViewSpatial. After adding the pattern reward, the model achieves consistent gains
across all three benchmarks. This suggests that applying a fixed reasoning pattern introduces redundant
information and thereby interferes with answer prediction. In contrast, the pattern reward encourages a more
concise and efficient reasoning process, enabling the model to make more accurate use of spatial evidence.
Effects of Local Position and Direction Tokens. Table 4 groups the three benchmarks into three categories:
Position, which focuses on relative object locations; Direction, which focuses on object orientation; and Mixed,
which requires both types of local evidence. The results show that using both position and direction tokens
yields the best overall performance. When only the position token is used during reasoning, the model performs
well on position-related questions but shows clear degradation on direction-related and mixed categories.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
SPAR
SPBench
ViewSpatial
Accuracy (%)
52.8
41.0
19.8
67.5
68.8
46.3
56.9
53.3
36.8
63.5
61.2
40.2
Stage 1 + 2
Stage 1 + 2 + 3
Stage 1 + 2 + Extra Stage 2 (
t =
l = 1,
g = 0.1)
Stage 1 + 2 + Extra Stage 2 (
t =
l = 0.1,
g = 0.01)
Figure 4 Ablation study on the effectiveness of Stage 3.
Attention Weight (%)
answer
meters
difference
and
6.25%
6.08%
5.15%
3.78%
1.92%
1.04%
0.98%
0.91%
0.90%
0.87%
(a) Text CoT
Attention Weight (%)
answer
difference
meters
6.05%
6.01%
4.42%
2.55%
1.19%
1.18%
1.14%
0.93%
0.86%
0.78%
(b) GeoAnchor w/o Stage 1
10%
15%
Attention Weight (%)
<latent>
<latent>
<latent>
answer
meters
15.23%
14.16%
13.87%
5.00%
4.59%
4.35%
2.56%
1.54%
1.23%
1.17%
(c) GeoAnchor
Figure 5 Comparison of the top text attention weights assigned by the final answer under different reasoning paradigms.
Using only the direction token leads to the opposite trend. These observations indicate that the local tokens
indeed encode their corresponding spatial information and provide strong evidence for final answer generation.
Effects of Alignment Strategies in Global Tokens. Table 5 compares different VGGT alignment strategies. The
proposed soft coverage alignment is evaluated against three dense alignment baselines. Specifically, Mean
Pooling averages the VGGT features and the global token along the sequence dimension. Adaptive Pooling
and Linear Interpolation resample the VGGT features to match the length of the global token using average
pooling and interpolation, respectively. The results show that soft coverage alignment achieves the best
performance across all three benchmarks, suggesting that coverage-based supervision provides a more suitable
strategy for learning a compact representation of scene-level geometry while preserving sufficient information
for downstream reasoning.
4.4
In-Depth Analysis
Latent reasoning improves aggregation of answer-relevant information, with Stage 1 playing a key role. As shown in
Figure 5, GeoAnchor assigns stronger attention to latent tokens when generating the final answer. In contrast,
although Text CoT also produces numerical coordinates, its answer token attends less to spatially meaningful
cues and more to semantically weak symbols. This suggests that discretized textual reasoning weakens
spatial semantics, whereas GeoAnchor allows the answer to directly leverage compact latent representations.
The attention analysis further highlights that Stage 1 is important for developing a strong dependence on
latent tokens, indicating that this stage establishes robust grounded latent evidence that supports subsequent
reasoning.
Final-answer attention is more accurately grounded in task-relevant visual regions. As shown in the upper part of
Figure 6, GeoAnchor focuses more precisely on the visual regions relevant to the queried spatial target when
generating the final answer. By comparison, the baseline exhibits more diffuse attention, while Text CoT
spreads attention more broadly without clearly isolating the most relevant object or location. This suggests
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Qwen3-VL-2B
Text CoT
GeoAnchor
red point latent
blue point latent
green point latent
Attention on Final Answer
Attention on Local Latent
Figure 6 Visual attention comparison on the final answer
and local token. The red, blue, and green points represent
the target objects mentioned in the questions.
Text
Image
Latent
VGGT
SPAR-Bench
SPBench
Figure 7 Visualization of text, image, VGGT, and global
token embeddings using t-SNE.
that GeoAnchor not only aggregates reasoning information more effectively, but also grounds its predictions
more faithfully in visual evidence.
Local tokens show clear spatial specialization. The lower part of Figure 6 shows that GeoAnchor produces
distinct visual attention patterns when generating latent tokens for different positions. Each local token
consistently attends to the region associated with its corresponding spatial target, indicating that these tokens
encode disentangled spatial semantics rather than entangled global patterns. This behavior suggests that the
latent space is organized in a semantically meaningful way, making the intermediate reasoning variables both
interpretable and useful for final answer prediction.
The global token indeed encodes VGGT information. Following Yang et al. (2025d), we use t-SNE (Van der
Maaten and Hinton, 2008) to visualize the relationships among text, image, VGGT features, and the global
token. As shown in Figure 7, on both SPAR-Bench and SPBench, the global token lies between the VGGT and
text tokens. This suggests that it remains close to the geometry manifold while preserving textual semantics,
consistent with the role of Stage 3 discussed in Section 3.3.

## sec:conclusion Conclusion
_Pages 11-12_

This paper presents GeoAnchor, a text-latent interleaved framework for spatial reasoning. By decomposing
spatial reasoning into position, direction, and geometry latents, GeoAnchor enables decomposed local-
plus-global reasoning beyond text-only representations. A collaborative multi-stage training strategy further
improves the learning of grounded spatial evidence. Experiments on multiple benchmarks show that GeoAnchor
consistently outperforms the base model and generalizes well across diverse 3D reasoning tasks.
Acknowledgement
This work is supported by the National Natural Science Foundation of China (Grant Nos. 92270201 and
62125204), and National Natural Science Foundation of China (62522102, 62432001), Beijing Natural Science
Foundation (L247006).
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding

## sec:references References
_Pages 12-22_

Muhamamd Zeshan Afzal, SK Aziz Ali, Didier Stricker, Peter Eisert, Anna Hilsmann, Daniel Perez-Marcos, Marco
Bianchi, Sonia Crottaz-Herbette, Roberto De Ioris, Eleni Mangina, et al. Next generation xr systems-large language
models meet augmented and virtual reality. IEEE computer graphics and applications, 2025.
Xiang An, Yin Xie, Kaicheng Yang, Wenkang Zhang, Xiuwei Zhao, Zheng Cheng, Yirui Wang, Songcen Xu, Changrui
Chen, Didi Zhu, et al. Llava-onevision-1.5: Fully open framework for democratized multimodal training. arXiv
preprint arXiv:2509.23661, 2025.
Hunar Batra, Haoqin Tu, Hardy Chen, Yuanze Lin, Cihang Xie, and Ronald Clark. Spatialthinker: Reinforcing 3d
reasoning in multimodal llms via spatial rewards. arXiv preprint arXiv:2511.07403, 2025.
Mahtab Bigverdi, Zelun Luo, Cheng-Yu Hsieh, Ethan Shen, Dongping Chen, Linda G Shapiro, and Ranjay Krishna.
Perception tokens enhance visual reasoning in multimodal language models. In Proceedings of the Computer Vision
and Pattern Recognition Conference, pages 3836–3845, 2025.
Natasha Butt, Ariel Kwiatkowski, Ismail Labiad, Julia Kempe, and Yann Ollivier. Soft tokens, hard truths. arXiv
preprint arXiv:2509.19170, 2025.
Zhongang Cai, Ruisi Wang, Chenyang Gu, Fanyi Pu, Junxiang Xu, Yubo Wang, Wanqi Yin, Zhitao Yang, Chen Wei,
Qingping Sun, et al. Scaling spatial intelligence with multimodal foundation models. arXiv preprint arXiv:2511.13719,
2025.
Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. Spatialvlm:
Endowing vision-language models with spatial reasoning capabilities. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 14455–14465, 2024.
Zhangquan Chen, Manyuan Zhang, Xinlei Yu, Xufang Luo, Mingze Sun, Zihao Pan, Yan Feng, Peng Pei, Xunliang
Cai, and Ruqi Huang. Think with 3d: Geometric imagination grounded spatial reasoning from limited views. arXiv
preprint arXiv:2510.18632, 2025.
An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu.
Spatialrgpt: Grounded spatial reasoning in vision-language models. Advances in Neural Information Processing
Systems, 37:135062–135093, 2024.
Christopher Clark, Jieyu Zhang, Zixian Ma, Jae Sung Park, Mohammadreza Salehi, Rohun Tripathi, Sangho Lee,
Zhongzheng Ren, Chris Dongjoo Kim, Yinuo Yang, et al. Molmo2: Open weights and data for vision-language
models with video understanding and grounding. arXiv preprint arXiv:2601.10611, 2026.
Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein,
Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality,
long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.
Angela Dai, Angel X Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser, and Matthias Niessner. Scannet:
Richly-annotated 3d reconstructions of indoor scenes. In Proceedings of the IEEE conference on computer vision
and pattern recognition, pages 5828–5839, 2017.
Karim Elmaaroufi, Liheng Lai, Justin Svegliato, Yutong Bai, Sanjit A Seshia, and Matei Zaharia. Graid: Enhancing
spatial reasoning of vlms through high-fidelity data generation. arXiv preprint arXiv:2510.22118, 2025.
Zhiwen Fan, Jian Zhang, Renjie Li, Junge Zhang, Runjin Chen, Hezhen Hu, Kevin Wang, Huaizhi Qu, Dilin Wang,
Zhicheng Yan, et al. Vlm-3r: Vision-language models augmented with instruction-aligned 3d reconstruction. arXiv
preprint arXiv:2505.20279, 2025.
Timin Gao, Peixian Chen, Mengdan Zhang, Chaoyou Fu, Yunhang Shen, Yan Zhang, Shengchuan Zhang, Xiawu
Zheng, Xing Sun, Liujuan Cao, et al. Cantor: Inspiring multimodal chain-of-thought of mllm. In Proceedings of the
32nd ACM International Conference on Multimedia, pages 9096–9105, 2024.
Mohsen Gholami, Ahmad Rezaei, Zhou Weimin, Sitong Mao, Shunbo Zhou, Yong Zhang, and Mohammad Akbari.
Spatial reasoning with vision-language models in ego-centric multi-view scenes. arXiv preprint arXiv:2509.06266,
2025.
Ross Girshick. Fast r-cnn. In Proceedings of the IEEE international conference on computer vision, pages 1440–1448,
2015.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Google DeepMind.
Gemini 3 pro model card, 2025.
URL https://storage.googleapis.com/deepmind-media/
Model-Cards/Gemini-3-Pro-Model-Card.pdf.
Wenyi Hong, Wenmeng Yu, Xiaotao Gu, Guo Wang, Guobing Gan, Haomiao Tang, Jiale Cheng, Ji Qi, Junhui
Ji, Lihang Pan, et al. Glm-4.5 v and glm-4.1 v-thinking: Towards versatile multimodal reasoning with scalable
reinforcement learning. arXiv preprint arXiv:2507.01006, 2025.
Wenbo Hu, Jingli Lin, Yilin Long, Yunlong Ran, Lihan Jiang, Yifan Wang, Chenming Zhu, Runsen Xu, Tai Wang,
and Jiangmiao Pang. G2vlm: Geometry grounded vision language model with unified 3d reconstruction and spatial
reasoning. arXiv preprint arXiv:2511.21688, 2025.
Xiaohu Huang, Jingjing Wu, Qunyi Xie, and Kai Han. Mllms need 3d-aware representation supervision for scene
understanding. arXiv e-prints, pages arXiv–2506, 2025.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila
Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. arXiv preprint arXiv:2410.21276, 2024.
Jyh-Jing Hwang, Runsheng Xu, Hubert Lin, Wei-Chih Hung, Jingwei Ji, Kristy Choi, Di Huang, Tong He, Paul
Covington, Benjamin Sapp, et al. Emma: End-to-end multimodal model for autonomous driving. arXiv preprint
arXiv:2410.23262, 2024.
Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan
Foster, Grace Lam, Pannag Sanketi, et al. Openvla: An open-source vision-language-action model. arXiv preprint
arXiv:2406.09246, 2024.
Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980,
2014.
Bangzheng Li, Ximeng Sun, Jiang Liu, Ze Wang, Jialian Wu, Xiaodong Yu, Hao Chen, Emad Barsoum, Muhao Chen,
and Zicheng Liu. Latent visual reasoning. arXiv preprint arXiv:2509.24251, 2025a.
Dingming Li, Hongxing Li, Zixuan Wang, Yuchen Yan, Hang Zhang, Siqi Chen, Guiyang Hou, Shengpei Jiang, Wenqi
Zhang, Yongliang Shen, et al. Viewspatial-bench: Evaluating multi-perspective spatial localization in vision-language
models. arXiv preprint arXiv:2505.21500, 2025b.
Hongxing Li, Dingming Li, Zixuan Wang, Yuchen Yan, Hang Wu, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun
Xiao, and Yueting Zhuang. Spatialladder: Progressive training for spatial reasoning in vision-language models. arXiv
preprint arXiv:2510.08531, 2025c.
Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. Depth
anything 3: Recovering the visual space from any views. arXiv preprint arXiv:2511.10647, 2025.
Haotian Liu, Chunyuan Li, Yuheng Li, Bo Li, Yuanhan Zhang, Sheng Shen, and Yong Jae Lee. Llavanext: Improved
reasoning, ocr, and world knowledge, 2024.
Yang Liu, Ming Ma, Xiaomin Yu, Pengxiang Ding, Han Zhao, Mingyang Sun, Siteng Huang, and Donglin Wang.
Ssr: Enhancing depth perception in vision-language models via rationale-guided spatial reasoning. arXiv preprint
arXiv:2505.12448, 2025a.
Yuhong Liu, Beichen Zhang, Yuhang Zang, Yuhang Cao, Long Xing, Xiaoyi Dong, Haodong Duan, Dahua Lin, and
Jiaqi Wang. Spatial-ssrl: Enhancing spatial understanding via self-supervised reinforcement learning. arXiv preprint
arXiv:2510.27606, 2025b.
Yongsen Mao, Junhao Zhong, Chuan Fang, Jia Zheng, Rui Tang, Hao Zhu, Ping Tan, and Zihan Zhou. Spatiallm:
Training large language models for structured indoor modeling. arXiv preprint arXiv:2506.07491, 2025.
Kun Ouyang, Yuanxin Liu, Haoning Wu, Yi Liu, Hao Zhou, Jie Zhou, Fandong Meng, and Xu Sun. Spacer: Reinforcing
mllms in video spatial reasoning. arXiv preprint arXiv:2504.01805, 2025.
Karl Pertsch, Kyle Stachowicz, Brian Ichter, Danny Driess, Suraj Nair, Quan Vuong, Oier Mees, Chelsea Finn, and
Sergey Levine. Fast: Efficient action tokenization for vision-language-action models. arXiv preprint arXiv:2501.09747,
2025.
Yiming Qin, Bomin Wei, Jiaxin Ge, Konstantinos Kallidromitis, Stephanie Fu, Trevor Darrell, and XuDong Wang.
Chain-of-visual-thought: Teaching vlms to see and think better with continuous visual tokens. arXiv preprint
arXiv:2511.19418, 2025.
Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. URL https://qwen.ai/blog?id=qwen3.5.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Arijit Ray, Ahmed Abdelkader, Chengzhi Mao, Bryan A Plummer, Kate Saenko, Ranjay Krishna, Leonidas Guibas,
and Wen-Sheng Chu. Mull-tokens: Modality-agnostic latent thinking. arXiv preprint arXiv:2512.10941, 2025.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li,
Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv
preprint arXiv:2402.03300, 2024.
Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. Codi: Compressing chain-of-thought
into continuous space via self-distillation. In Proceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pages 677–693, 2025.
Kimi Team, Angang Du, Bohong Yin, Bowei Xing, Bowen Qu, Bowen Wang, Cheng Chen, Chenlin Zhang, Chenzhuang
Du, Chu Wei, et al. Kimi-vl technical report. arXiv preprint arXiv:2504.07491, 2025.
Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. Journal of machine learning research, 9
(11), 2008.
Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. Vggt:
Visual geometry grounded transformer. In Proceedings of the Computer Vision and Pattern Recognition Conference,
pages 5294–5306, 2025a.
Qixun Wang, Yang Shi, Yifei Wang, Yuanxing Zhang, Pengfei Wan, Kun Gai, Xianghua Ying, and Yisen Wang. Monet:
Reasoning in latent visual space beyond images and language. arXiv preprint arXiv:2511.21395, 2025b.
Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong
Ye, Jie Shao, et al. Internvl3. 5: Advancing open-source multimodal models in versatility, reasoning, and efficiency.
arXiv preprint arXiv:2508.18265, 2025c.
Xilin Wei, Xiaoran Liu, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Jiaqi Wang, Xipeng Qiu, and Dahua Lin. Sim-cot:
Supervised implicit chain-of-thought. arXiv preprint arXiv:2509.20317, 2025.
Junjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Jinming Li, Zhongyi Zhou, Xiaoyu Liu, Chaomin Shen, Yaxin
Peng, and Feifei Feng. Diffusionvla: Scaling robot foundation models via unified diffusion and autoregression. In
Forty-second International Conference on Machine Learning, 2025.
Diankun Wu, Fangfu Liu, Yi-Hsin Hung, and Yueqi Duan. Spatial-mllm: Boosting mllm capabilities in visual-based
spatial intelligence. arXiv preprint arXiv:2505.23747, 2025a.
Junfei Wu, Jian Guan, Kaituo Feng, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, and Tieniu Tan. Reinforcing spatial
reasoning in vision-language models with interwoven thinking and visual drawing. arXiv preprint arXiv:2506.09965,
2025b.
Wenshan Wu, Shaoguang Mao, Yadong Zhang, Yan Xia, Li Dong, Lei Cui, and Furu Wei. Mind’s eye of llms:
visualization-of-thought elicits spatial reasoning in large language models. Advances in Neural Information Processing
Systems, 37:90277–90317, 2024.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang,
Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025a.
Rui Yang, Ziyu Zhu, Yanwei Li, Jingjia Huang, Shen Yan, Siyuan Zhou, Zhe Liu, Xiangtai Li, Shuangye Li, Wenqian
Wang, et al. Visual spatial tuning. arXiv preprint arXiv:2511.05491, 2025b.
Yuncong Yang, Jiageng Liu, Zheyuan Zhang, Siyuan Zhou, Reuben Tan, Jianwei Yang, Yilun Du, and Chuang Gan.
Mindjourney: Test-time scaling with world models for spatial reasoning. arXiv preprint arXiv:2507.12508, 2025c.
Zeyuan Yang, Xueyang Yu, Delin Chen, Maohao Shen, and Chuang Gan. Machine mental imagery: Empower
multimodal reasoning with latent visual tokens. arXiv preprint arXiv:2506.17218, 2025d.
Bowen Ye, Bin Zhang, and Hang Zhao. Dap: A discrete-token autoregressive planner for autonomous driving. arXiv
preprint arXiv:2511.13306, 2025.
Chandan Yeshwanth, Yueh-Cheng Liu, Matthias Niessner, and Angela Dai. Scannet++: A high-fidelity dataset of 3d
indoor scenes. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 12–22, 2023.
Tianyu Yu, Zefan Wang, Chongyi Wang, Fuwei Huang, Wenshuo Ma, Zhihui He, Tianchi Cai, Weize Chen, Yuxiang
Huang, Yuanqian Zhao, et al. Minicpm-v 4.5: Cooking efficient mllms via architecture, data, and training recipe.
arXiv preprint arXiv:2509.18154, 2025.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Zhenrui Yue, Bowen Jin, Huimin Zeng, Honglei Zhuang, Zhen Qin, Jinsung Yoon, Lanyu Shang, Jiawei Han, and Dong
Wang. Hybrid latent reasoning via reinforcement learning. arXiv preprint arXiv:2505.18454, 2025.
Xiaoyu Zhan, Wenxuan Huang, Hao Sun, Xinyu Fu, Changfeng Ma, Shaosheng Cao, Bohan Jia, Shaohui Lin, Zhenfei
Yin, Lei Bai, et al. Actial: Activate spatial reasoning ability of multimodal large language models. arXiv preprint
arXiv:2511.01618, 2025.
Haoyu Zhang, Meng Liu, Zaijing Li, Haokun Wen, Weili Guan, Yaowei Wang, and Liqiang Nie. Spatial understanding
from videos: Structured prompts meet simulation data. arXiv preprint arXiv:2506.03642, 2025a.
Jiahui Zhang, Yurui Chen, Yanpeng Zhou, Yueming Xu, Ze Huang, Jilin Mei, Junhui Chen, Yu-Jie Yuan, Xinyue Cai,
Guowei Huang, et al. From flatland to space: Teaching vision-language models to perceive and reason in 3d. arXiv
preprint arXiv:2503.22976, 2025b.
Weichen Zhang, Zile Zhou, Xin Zeng, Liu Xuchen, Jianjie Fang, Chen Gao, Jinqiang Cui, Yong Li, Xinlei Chen,
and Xiao-Ping Zhang. Open3d-vqa: A benchmark for embodied spatial concept reasoning with multimodal large
language model in open space. In Proceedings of the 33rd ACM International Conference on Multimedia, pages
12784–12791, 2025c.
Duo Zheng, Shijia Huang, and Liwei Wang. Video-3d llm: Learning position-aware video representation for 3d scene
understanding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
8995–9006, 2025.
Jia Zheng, Junfei Zhang, Jing Li, Rui Tang, Shenghua Gao, and Zihan Zhou. Structured3d: A large photo-realistic
dataset for structured 3d modeling. In European Conference on Computer Vision, pages 519–535. Springer, 2020.
Xingcheng Zhou, Xuyuan Han, Feng Yang, Yunpu Ma, Volker Tresp, and Alois Knoll. Opendrivevla: Towards
end-to-end autonomous driving with large vision language action model. arXiv preprint arXiv:2503.23463, 2025.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Datasets and Evaluation Benchmarks
Our training data mainly come from SPAR-7M and SpatialLadder-26K. In the experiments, we use SPAR-
Bench, SPBench, and ViewSpatial-Bench as the main benchmarks to evaluate our method. In this section, we
first introduce the datasets and benchmarks used in our study, and then summarize the task definitions and
sample counts of the evaluated benchmark subsets in the corresponding tables.
A.1
SPAR-7M and SPAR-Bench
SPAR-7M is a large-scale dataset designed for spatial understanding, constructed from more than 4,000 indoor
3D scenes collected from public scene datasets with 3D ground truth, including ScanNet, ScanNet++, and
Structured3D. Through a 3D-driven data generation pipeline, the authors derive image sequences, camera
parameters, and depth information from these scenes, and further generate diverse spatial question-answer
pairs from the associated 3D scene metadata. As a result, SPAR-7M covers 33 task types and contains over 7
million QA pairs, spanning a broad range of abilities from low-level spatial perception to high-level spatial
reasoning, and supporting single-view, multi-view, and video settings.
Importantly, the dataset is accompanied by its own benchmark, namely SPAR-Bench, which is explicitly
introduced for evaluation rather than training alone. SPAR-Bench is constructed from the SPAR-7M split by
selecting representative spatial tasks and manually verifying the resulting samples for quality control. In our
experiments, we use the single-image subset of SPAR-Bench, which contains 2,866 samples in total. Detailed
task definitions and per-task sample counts are summarized in Table 1.
Table 1 Task definitions and sample counts of the SPAR-Bench subset used in our experiments.
Task Name
Description
#Samples
depth_prediction_oc
Given the depth of a reference point, estimate the depth of another queried
point.
depth_prediction_oo
Given the depth of a reference point, estimate the depth difference between
two other queried points.
distance_prediction_oc
Estimate the distance between a queried point and the camera.
distance_prediction_oo
Estimate the distance between two queried points.
distance_infer_center_oo
Determine which of two queried points is farther away from a given
reference point.
obj_spatial_relation
Under the camera view, determine the relative position of one queried point
with respect to another.
spatial_imagination_oc
First determine the position of a queried point under the camera view, then
re-judge its position after a viewpoint transformation.
spatial_imagination_oo
First determine the relative position between two queried points under the
camera view, then re-judge their relation after a viewpoint transformation.
Total
A.2
SpatialLadder-26K and SPBench
SpatialLadder-26K is a multimodal spatial reasoning dataset designed to support progressive learning from
perceptual grounding to more advanced reasoning. It contains 26,610 samples across four complementary
task categories, including object localization, single-image spatial reasoning, multi-view spatial reasoning, and
video spatial reasoning. In terms of task coverage, the dataset spans seven spatial dimensions, namely relative
direction, relative distance, absolute distance, object size, counting, room size, and appearance order, thereby
covering a broad range of spatial understanding skills across image, multi-view, and video modalities. In
terms of data sources, the object localization, single-image, and multi-view portions are constructed from
ScanNet 3D scene reconstructions, while the video subset is sampled from SR-91k.
The paper further introduces two dedicated benchmarks built using the same pipeline on the ScanNet validation
set, namely SPBench-SI and SPBench-MV. In our experiments, we use only the single-image benchmark,
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
namely SPBench-SI, which contains 1,009 samples in total. Detailed task definitions and per-task sample
counts are summarized in Table 2.
Table 2 Task definitions and sample counts of the SPBench-SI subset used in our experiments.
Task Name
Description
#Samples
object_rel_direction
Under the camera view, determine the relative position between two objects.
object_rel_distance
Determine which object is farther away from a given reference object.
object_abs_distance
Under the camera view, estimate the distance between two objects.
object_size_estimation
Estimate the size of an object along a given dimension in centimeters.
Total
A.3
ViewSpatial-Bench
ViewSpatial-Bench is a dedicated benchmark for evaluating multi-perspective spatial localization in vision-
language models. It contains over 5,700 multiple-choice question-answer pairs spanning more than 1,000
unique 3D scenes, with source images drawn from the validation sets of ScanNet and MS-COCO. In terms
of task coverage, the benchmark comprises multiple task types under complementary perspective settings,
targeting both camera-perspective and person-perspective spatial reasoning. This design makes it a challenging
benchmark for evaluating cross-viewpoint spatial understanding.
Although the paper also describes a larger multi-perspective spatial training dataset generated by the same
automated 3D annotation pipeline, the associated training set is not publicly released. Accordingly, in our
experiments, we use only the single-image evaluation subset of ViewSpatial-Bench, which contains 4,607
samples in total. Detailed task definitions and per-task sample counts are summarized in Table 3.
A.4
Definition of Grouped Metrics
Main results in the paper using grouped abbreviations instead of listing every original task separately. Table 4
summarizes the mapping from each grouped metric to its corresponding original tasks. In all cases, each
grouped metric is computed as the average over the corresponding original tasks.
Training Dataset Construction
B.1
Overview
We construct two training datasets for GeoAnchor. The first is a 3D grounding dataset used in Stage 1 to
initialize local spatial perception. The second is a spatial reasoning training dataset used in Stages 2 and 3 as
well as the subsequent RL stage. In this section, we describe the construction pipeline, annotation procedure,
and summary statistics of these datasets.
B.2
3D Grounding Dataset
B.2.1
Object Extraction
Our 3D grounding dataset is constructed based on ScanNet. We sample 10k scenes from more than 2.5
million views spanning over 1,500 scans. For each image, we first employ Qwen3-VL-32B to identify up to five
salient objects, together with their textual descriptions and 2D bounding boxes. The prompt used for object
extraction is shown in Figure. 1.
To ensure the consistency between the generated referring expressions and the localized regions, we perform an
additional verification step after object extraction. Concretely, for each object, we take the generated referring
expression and use it as a grounding query on the same image to obtain a second predicted bounding box.
We then measure the overlap between the original box and the re-grounded box using intersection-over-union
(IoU). An annotation is retained only if the IoU exceeds 0.5; otherwise, it is discarded. This self-consistency
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 3 Task definitions and sample counts of the ViewSpatial-Bench subset used in our experiments.
Task Name
Description
#Samples
Camera perspective –
Relative Direction
Under the camera view, determine the relative position of one queried point
with respect to another.
Camera perspective –
Object View Orientation
Given an image, determine the facing orientation of the object.
Person perspective –
Object View Orientation
Determine the facing orientation of the person appearing in the image.
Person perspective –
Relative Direction
Given a specified person-centered perspective, determine the relative position of
an object.
Total
Table 4 Mapping from grouped metric abbreviations to the original tasks.
Benchmark
Abbr.
Original Task
SPAR-Bench
Dep.
depth_prediction_oc, depth_prediction_oo
Dis.
distance_prediction_oc, distance_prediction_oo
Prox.
distance_infer_center_oo
Rel.
obj_spatial_relation
View.
spatial_imagination_oc, spatial_imagination_oo
SPBench
Rel.
object_rel_direction, object_rel_distance
Abs.
object_abs_distance, object_size_estimation
ViewSpatial
Cam.
Camera perspective – Relative Direction
Camera perspective – Object View Orientation
Per.
Person perspective – Object View Orientation
Person perspective – Relative Direction
check effectively filters out noisy cases in which the generated textual description does not faithfully correspond
to the extracted object region. The prompt used for verification is shown in Figure. 2.
Table 5 reports the verification results. Across 10,000 images, 47,663 object annotations are automatically
extracted, and 44,998 pass the self-consistency check, giving an object-level retention rate of 94.41%. The
mean and median IoU between the original and re-grounded boxes are 0.787 and 0.856, showing that most
generated referring expression–bounding box pairs are well aligned.
B.2.2
3D Position Acquisition
We estimate depth maps and camera poses using Depth Anything v3, and recover object 3D coordinates
through depth-guided back-projection.
These recovered coordinates are further converted into object-
level position annotations and pairwise direction annotations for supervising local latent learning. For an
object with bounding box bi = [x(1)
i , y(1)
, x(2)
i , y(2)
], we define its 2D reference point as the box center, i.e.,
ui = (x(1)
+ x(2)
i )/2 and vi = (y(1)
+ y(2)
)/2. Let Ωi denote the set of pixels covered by the box. The object
depth is estimated by averaging the predicted depth values inside the box:
zi =
|Ωi|
(u,v)∈Ωi
D(u, v).
(1)
Given the camera intrinsic matrix K and pose (R, t), where R ∈R3×3 and t ∈R3, the object position in the
camera and world coordinates is computed as:
i = ziK−1 ui, vi, 1T ,
i = Rpc
i + t.
(2)
We use pw
as the object-level position annotation.
For an object pair (i, j), the relative displacement
∆ij = pw
j −pw
i is used to derive pairwise direction annotations.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
You are a vision-language model performing object grounding.
Task: In this image, detect up to 5 salient objects.
For each object, write ONE referring expression (REC)
that uniquely identifies the object in the scene, and its bounding box.
Output format:
[{"rec": "...", "bbox": [x1, y1, x2, y2]}, ...]
Requirements:
- Return ONLY a valid JSON list, nothing else.
- 0 to 5 items in the list.
- bbox is [x1, y1, x2, y2] normalized to [0, 1000].
Figure 1 Prompt used for object extraction and referring-
expression generation in the construction pipeline of the
3D grounding dataset.
You are a vision-language model performing object grounding.
Given an image and a referring expression, localize the referred
object and return ONLY one valid JSON object in the format:
{"bbox": [x1, y1, x2, y2]}
Requirements:
- Return ONLY the JSON object, nothing else.
- bbox must be [x1, y1, x2, y2].
- Coordinates must be normalized to [0, 1000].
Figure 2 Prompt used for the self-consistency verification
of automatically generated referring expression–bounding
box pairs.
Table 5 Statistics of the self-consistency verification step
for object extraction.
Total anns.
Verified anns.
Retention rate
Mean IoU
Median IoU
47,663
44,998
94.41%
0.787
0.856
Table 6 Comparison between 3D object coordinates recov-
ered from pseudo depth and ground-truth depth.
Mean Err.
Median Err.
x Err.
y Err.
z Err.
Acc@0.5m
Acc@0.2m
0.09
0.04
0.02
0.01
0.08
98.0
92.9
Table 6 shows that 3D coordinates recovered from pseudo depth closely match those from ground-truth depth.
The mean and median Euclidean errors are only 0.09,m and 0.04,m, with most deviation concentrated on the
depth axis. Meanwhile, 98.0% and 92.9% of recovered points fall within 0.5,m and 0.2,m, respectively. This
confirms that pseudo depth introduces only limited noise and serves as reliable 3D supervision for subsequent
local latent learning.
B.2.3
Dataset Statistics
To increase the diversity of supervision, we construct training queries in three forms: point-coordinate
queries, bounding-box-based queries, and natural-language queries. Each sample involves one to three objects
depending on the task type. After filtering invalid detections and geometrically unreliable samples, the final
pipeline yields 550k 3D grounding samples. Table 7 summarizes the statistics for grounding dataset.
B.3
Spatial Reasoning Training Dataset
The spatial reasoning training dataset is mainly built from SPAR and SpatialLadder-26K. We sample 100k
questions from SPAR and 5k from SpatialLadder-26K. Basic dataset statistics are summarized in Table 8 and
Table 9.
Experiment Details
C.1
Implementation Details
The complete implementation details are summarized in Table 10. The table covers the key experimental
settings for our 4-stage collaborative training.
C.2
Experiment Settings
C.2.1
Task Definition of Position, Direction, and Mixed Questions.
As described in Section 4.3, the tasks from the three benchmarks are regrouped into three categories: Position,
Direction, and Mixed, according to the type of local spatial evidence they require. Table 11 further provides
an explicit mapping from these three categories to the original task types in each benchmark.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 7 Statistics of 3D Grounding Dataset used in Stage 1.
Question Type
Count
Single Position Question
224,990
Multiple Position Question
159,530
Direction Question
164,920
Total
549,440
Table 8 Statistics for Spatial Reasoning datasets from SPAR.
Source Dataset
Type
Question Type
Count
ScanNet
depth_prediction_oc
numeric
depth_prediction_oo
numeric
distance_infer_center_oo
multiple choice
distance_prediction_oc
numeric
distance_prediction_oo
numeric
obj_spatial_relation_oo
multiple choice
spatial_imagination_oc
multiple choice
spatial_imagination_oo
multiple choice
ScanNet++
depth_prediction_oc
numeric
depth_prediction_oo
numeric
distance_infer_center_oo
multiple choice
distance_prediction_oc
numeric
distance_prediction_oo
numeric
obj_spatial_relation_oo
multiple choice
spatial_imagination_oc
multiple choice
spatial_imagination_oo
multiple choice
Structured3D
depth_prediction_oc
numeric
depth_prediction_oo
numeric
distance_prediction_oc
numeric
distance_prediction_oo
numeric
spatial_imagination_oc
numeric
spatial_imagination_oo
numeric
Total
C.2.2
Dense Alignment Baselines for Global Geometry Supervision
This subsection describes the three dense alignment baselines presented in ablation study of VGGT alignment
strategy. All three methods use the same projected geometry tokens as in Section 3.2, and differ only in
how the dense VGGT feature sequence is compressed to match the length of the global token. Following
Section 3.2, let the final VGGT feature map be of size H × W × D. After flattening the spatial dimensions in
raster order, the VGGT feature sequence is denoted as:
F = {f1, . . . , flf } ∈Rlf ×D,
lf = H × W,
(3)
and the global latent zgeo is projected into geometry tokens:
G = {g1, . . . , glgeo} ∈Rlgeo×D,
(4)
where lgeo is the number of geometry tokens.
Mean Pooling. This baseline performs the strongest compression. It averages the dense VGGT sequence and
the geometry-token sequence along the sequence dimension, producing one global vector for each side, and
then directly aligns the two pooled vectors with Smooth L1 loss. In other words, the entire feature sequence
is reduced to a single scene-level representation before alignment.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 9 Statistics for Spatial Reasoning datasets from SpatialLadder-26K.
Question Category
Question Type
Count
Relative Direction
multiple choice
Absolute Distance
numeric
Object Size
numeric
Relative Distance
multiple choice
Total
Table 10 Implementation details of GeoAnchor.
Category
Item
Setting
General
Base MLLM
Qwen3-VL-2B
Hardware
8 × NVIDIA A800
SFT
Local token length
lpos = ldir = 2
Global token length
lgeo = 8
S1 training epochs
S1 batch size
S1 learning rate
1 × 10−4
S2/3 training epochs
S2/3 batch size
S2/3 learning rate
2 × 10−5
Text loss weight
λt = 1
Local loss weight
λl = 1
Global loss weight
λg = 0.1
VGGT pooling levels
L = 3
VGGT pooling resolutions
{r1, r2, r3} = {1, 2, 4}
Geometry balance coefficient
λbal = 0.05
Rollouts per question
N = 8
Sampling temperature
1.0
Pattern reward
rpattern = 0.5
KL-divergence coefficient
β = 0.01
Learning rate
5 × 10−7
EMA smoothing coefficient
κ = 8
EMA update rate
µ = 0.2
Adaptive Pooling. This baseline first resamples the VGGT sequence from length lf to length lgeo by adaptive
average pooling. Concretely, the sequence is partitioned into lgeo contiguous bins of nearly equal size, and the
features inside each bin are averaged to obtain a resampled VGGT target sequence. This produces one target
vector for each geometry token, enabling token-wise dense supervision after length matching.
Linear Interpolation. This baseline also converts the VGGT sequence to length lgeo, but uses 2D linear
interpolation instead of average pooling. Compared with adaptive pooling, it preserves the sequence order
through continuous interpolation between neighboring VGGT features, and then aligns the interpolated
sequence with the geometry tokens in a token-wise manner.
For the latter two baselines, let ˜F = { ˜f1, . . . , ˜flgeo} ∈Rlgeo×D denote the resampled VGGT sequence obtained
by either adaptive pooling or linear interpolation. Their alignment loss is defined uniformly as:
Ldense =
lgeo
lgeo
j=1
SmoothL1(gj, ˜fj).
(5)
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 11 Task regrouping into Position, Direction, and Mixed categories for ablation study of local token interpretability.
Category
Task
Benchmark
Position
depth_prediction_oc
SPAR-Bench
depth_prediction_oo
SPAR-Bench
distance_prediction_oc
SPAR-Bench
distance_prediction_oo
SPAR-Bench
distance_infer_center_oo
SPAR-Bench
obj_spatial_relation
SPBench
object_rel_direction
SPBench
obj_abs_distance
SPBench
object_size_estimation
SPBench
object_rel_distance
SPBench
Camera - Relative Direction
ViewSpatial
Direction
Camera - Object View Orientation
ViewSpatial
Person - Object View Orientation
ViewSpatial
Mixed
spatial_imagination_oc
SPAR-Bench
spatial_imagination_oo
SPAR-Bench
Person - Relative Direction
ViewSpatial
Table 12 Ablation study on different base models. GeoAnchor is instantiated on Qwen2.5-VL-3B, with comparisons
against the base model, vanilla SFT, and text CoT SFT. The results show that GeoAnchor consistently achieves the
best performance across all three benchmarks, demonstrating that the proposed latent reasoning framework can be
effectively integrated into different base models and yields substantial gains in spatial reasoning.
SPAR-Bench
SPBench
ViewSpatial

## sec:model-4 Model
_Pages 22-23_

Avg.
Dep.
Dis.
Prox.
Rel.
View
Avg.
Rel.
Abs.
Avg.
Cam.
Per.
Qwen2.5-VL-3B
28.7
25.5
25.7
55.6
29.4
21.7
32.9
42.8
26.5
37.3
39.7
33.6
+ vanilla SFT
59.8
42.5
56.8
76.8
75.2
65.1
59.2
68.0
53.5
41.9
36.1
46.8
+ text CoT SFT
60.7
45.2
60.6
74.2
76.1
62.5
52.5
56.2
50.1
39.3
36.8
43.1
GeoAnchor
66.0
49.7
62.9
81.5
81.0
71.4
66.1
76.6
59.3
47.0
46.8
47.4
Improvement
+37.3
+24.2
+37.2
+25.9
+51.6
+49.7
+33.2
+33.8
+32.8
+9.7
+7.1
+13.8
Additional Experiments
D.1
Ablation Study for Different Base Model
We implement our latent reasoning framework on Qwen2.5-VL-3B, and Table 12 shows the corresponding
results. GeoAnchor consistently outperforms conventional SFT methods such as vanilla SFT and text CoT
SFT, exhibiting the same improvement trend as on the Qwen3-VL-2B illustratede in the main paper. These
results demonstrate the effectiveness and generalizability of our method, as it can be seamlessly integrated
into different model backbones and consistently improve their spatial reasoning capabilities.
D.2
Ablation Study for Different Latent Length
We carefully tune the lengths of the local and global tokens to ensure that the latent space remains both
expressive and compact. Table 13 shows that the best overall performance is achieved when the local token
length is 2 and the global token length is 8. This indicates that effective spatial reasoning depends on
a latent space that remains compact while preserving sufficient spatial information. Overly short latents
impose an excessive information bottleneck, while overly long latents weaken the compactness and functional
specialization of the latent space. The balanced setting therefore provides the most effective trade-off between
preserving spatial information and supporting downstream reasoning.
GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
Table 13 Ablation study on the latent length. We demon-
strate that the overall model achieves the best performance
when the local token length is 2 and the global token length
is 8.
Local
Global
SPAR
SPBench
ViewSpatial
Avg.
64.5
67.3
38.7
56.8
65.5
64.1
35.2
54.9
66.1
66.2
41.8
58.0
66.7
67.7
45.6
60.0
65.3
66.5
43.2
58.3
65.7
66.4
41.6
57.9
67.5
68.8
46.3
60.9
Table 14 Ablation study of pooling resolution for VGGT
alignment. The multi-scale setting {1, 2, 4} performs best
among all multi-scale variants, and further surpasses the
single-scale 5 × 5 setting even with a comparable token
count.
Pooling Resolution
SPAR
SPBench
ViewSpatial
Avg.
{1, 2}
65.2
67.1
41.6
57.9
{1, 2, 4, 8}
64.3
66.8
44.3
58.5
{5}
67.2
66.9
45.9
60.0
{1, 2, 4}
67.5
68.8
46.3
60.9
D.3
Ablation Study for Different Pooling Resolution in Global Token Alignment
Table 14 shows that the multi-scale setting {1, 2, 4} achieves the best overall performance, obtaining the best
results on all three benchmarks. This indicates that combining coarse-to-fine spatial resolutions provides
more effective geometry supervision than either a smaller or an overly fine scale set. Moreover, although the
single-scale 5 × 5 setting uses a comparable number of tokens, it still underperforms {1, 2, 4}. This suggests
that the advantage of multi-scale pooling lies in its ability to capture complementary geometric cues at
different spatial resolutions, jointly preserving global scene layout and finer local structure, which leads to
more effective geometry alignment.

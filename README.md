# GenAI-Hub
A collection of Jupyter notebooks showcasing the use of Generative AI models, including Large Language Models (LLMs), Vision-Language Models (VLMs), and Diffusion Models



## Models

<!-- AUTO-GENERATED:MODEL-INDEX:START -->

### Quick Start

Install uv, then use the root project for repository tooling:

```bash
uv sync
uv run python tools/validate_metadata.py
uv run python tools/update_readme.py
```

For notebook execution, use the environment shown in the matrix below. Shared environments live under `envs/`; models marked `model-specific` need the setup notes in their model folder metadata.

Register a shared environment as a Jupyter kernel:

```bash
cd envs/hf-transformers
uv sync
uv run python -m ipykernel install --user --name genai-hf-transformers
```

### Index (by model)

* [AEMatter](AEMatter/aematter_inference.ipynb) — segmentation-matting; matting, segmentation
* [Alfie](Alfie/alfie_inference.ipynb) — generation; image-generation, rgba-generation
* [AnimateDiff](AnimateDiff/animatediff_huggingface_inference.ipynb) — generation; video-generation, diffusion
* [AnomalyCLIP](AnomalyCLIP/anomalyclip_inference.ipynb) — anomaly; anomaly-detection, zero-shot
* [AuraSR](AuraSR/aurasr_inference.ipynb) — generation; super-resolution, image-generation
* [BART](BART/bart_huggingface_inference.ipynb) — llm; text-generation, seq2seq
* [BEN2](BEN2/ben2_huggingface_inference.ipynb) — segmentation-matting; segmentation, HR-seg, DIS
* [BERT-deepset](BERT-deepset/bert-deepset_haystack_inference.ipynb) — llm; question-answering
* [BiRefNet](BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb) — segmentation-matting; matting, segmentation, DIS
* [BLIP](BLIP/blip_huggingface_inference.ipynb) — vlm; VLM, captioning, VQA, image-text-retrieval
* [CAT-Seg](CAT-Seg/catseg_inference.ipynb) — segmentation-matting; segmentation, open-vocabulary-segmentation
* [CLIP](CLIP/clip_huggingface_inference.ipynb) — retrieval-embedding; contrastive, image-features, text-features, retrieval
* [CLIPseg](CLIPseg/clipseg_huggingface_inference.ipynb) — segmentation-matting; segmentation, text-prompted-segmentation
* [CogVLM](CogVLM/cogvlm_inference.ipynb) — vlm; VLM, VQA
* [ControlNet](ControlNet/controlnet_inference.ipynb) — generation; image-generation, conditioned-generation, diffusion
* [DepthAnything](DepthAnything/depthanything_huggingface_inference.ipynb) — depth-3d; depth-estimation
* [DepthPro](DepthPro/depthpro_inference.ipynb) — depth-3d; depth-estimation, metric-depth
* [DETR](DETR/detr_huggingface_inference.ipynb) — detection; detection
* [DiffDIS](DiffDIS/diffdis_inference.ipynb) — segmentation-matting; segmentation, HR-seg, DIS
* [DINOv3](DINOv3/dinov3_inference.ipynb) — classification-representation; image-features, representation-learning
* [DPT](DPT/dpt_huggingface_inference.ipynb) — depth-3d; depth-estimation
* [EoMT](EoMT/eomt_huggingface_inference.ipynb) — classification-representation; segmentation, image-features
* [EssentialAI](EssentialAI/essentialai_huggingface_inference.ipynb) — llm; text-generation
* [EVA](EVA/eva_timm_inference.ipynb) — classification-representation; image-classification, image-features
* [FaceParsing](FaceParsing/faceparsing_huggingface_inference.ipynb) — segmentation-matting; segmentation, face-parsing
* [Ferret](Ferret/ferret_inference.ipynb) — vlm; VLM, grounded-chat
* [FineGrain](FineGrain/finegrainBoxSeg_inference.ipynb) — segmentation-matting; segmentation, box-prompted-segmentation
* [FLAVA](FLAVA/flava_huggingface_inference.ipynb) — retrieval-embedding; multimodal, retrieval, image-text
* [FLUX](FLUX/flux_huggingface_inference.ipynb) — generation; image-generation, diffusion
* [GCL](GCL/gcl-e5_huggingface_inference.ipynb) — retrieval-embedding; retrieval, ranking, contrastive
* [Gemma3](Gemma3/gemma3_huggingface_inference.ipynb) — llm; text-generation, VLM
* [GLIDE](GLIDE/glide_inference.ipynb) — generation; image-generation, diffusion
* [GLIP](GLIP/glip_inference.ipynb) — detection; detection, grounding
* [GroundingDINO](GroundingDINO/groundingdino_huggingface_inference.ipynb) — detection; detection, grounding, open-vocabulary-detection
* [ImageGPT](ImageGPT/imagegpt_huggingface_inference.ipynb) — generation; image-generation, pixel-modeling
* [InternVL](InternVL/internvl_huggingface_inference.ipynb) — vlm; VLM, VQA
* [Janus](Janus/janus_huggingface_inference.ipynb) — vlm; VLM, multimodal-generation
* [Leffa](Leffa/leffa_inference.ipynb) — generation; person-image-generation, virtual-try-on
* [LeViT](LeViT/levit_timm_inference.ipynb) — classification-representation; image-classification
* [LISA](LISA/lisa_inference.ipynb) — segmentation-matting; segmentation, reasoning-segmentation, VLM
* [LLaMA2](LLaMA2/llama2_inference.ipynb) — llm; text-generation, chat
* [LLaVA](LLaVA/llava_huggingface_inference.ipynb) — vlm; VLM, VQA
* [LLaVA-NeXT](LLaVA-NeXT/llavanext_huggingface_inference.ipynb) — vlm; VLM, VQA
* [LLaVA-OneVision](LLaVA-OneVision/llavaonevision_huggingface_inference.ipynb) — vlm; VLM, VQA
* [Mask2Former](Mask2Former/mask2former_huggingface_inference.ipynb) — segmentation-matting; segmentation, panoptic-segmentation
* [OneFormer](OneFormer/oneformer_huggingface_inference.ipynb) — segmentation-matting; segmentation, semantic-segmentation, instance-segmentation, panoptic-segmentation
* [OV-DINO](OV-DINO/ovdino_inference.ipynb) — detection; detection, open-vocabulary-detection
* [OVSeg](OVSeg/ovseg_inference.ipynb) — segmentation-matting; segmentation, open-vocabulary-segmentation
* [OWL-v2](OWL-v2/owlv2_huggingface_inference.ipynb) — detection; detection, open-vocabulary-detection
* [OWL-ViT (owlvit_huggingface_inference.ipynb)](OWL-ViT/owlvit_huggingface_inference.ipynb) — detection; detection, open-vocabulary-detection
* [OWL-ViT (owlvit_inference-2.ipynb)](OWL-ViT/owlvit_inference-2.ipynb) — detection; detection, open-vocabulary-detection
* [PoolFormer](PoolFormer/poolformer_huggingface_inference.ipynb) — classification-representation; image-classification, image-features
* [PromptDepthAnything](PromptDepthAnything/promptdepthanything_huggingface_inference.ipynb) — depth-3d; depth-estimation, prompted-depth
* [QLIP](QLIP/qlip_huggingface_inference.ipynb) — retrieval-embedding; image-features, text-aligned-tokenization
* [SA2VA](SA2VA/sa2va_huggingface_inference.ipynb) — vlm; VLM, segmentation, grounded-understanding
* [SAM](SAM/sam_huggingface_inference.ipynb) — segmentation-matting; segmentation, prompted-segmentation
* [SAM-2](SAM-2/sam2_inference.ipynb) — segmentation-matting; segmentation, prompted-segmentation
* [SAM-3](SAM-3/sam3_inference.ipynb) — segmentation-matting; segmentation, concept-prompted-segmentation
* [SAM-HQ](SAM-HQ/samhq_inference.ipynb) — segmentation-matting; segmentation, high-quality-segmentation
* [SAMRefiner](SAMRefiner/samrefiner_inference.ipynb) — segmentation-matting; segmentation, seg-refinement
* [SAN](SAN/san_inference.ipynb) — segmentation-matting; segmentation, open-vocabulary-segmentation
* [SD2](SD2/sd_huggingface_inference.ipynb) — generation; image-generation, diffusion
* [SegFormer](SegFormer/segformer-clothes_huggingface_inference.ipynb) — segmentation-matting; segmentation, clothes-segmentation
* [SegZero](SegZero/segzero_inference.ipynb) — segmentation-matting; segmentation, reasoning-segmentation
* [SigLIP](SigLIP/siglip_huggingface_inference.ipynb) — retrieval-embedding; contrastive, image-features, text-features, retrieval
* [SmolVLM](SmolVLM/smolvlm_huggingface_inference.ipynb) — vlm; VLM, VQA
* [UNO](UNO/uno_huggingface_inference.ipynb) — generation; image-generation, in-context-generation
* [UperNet](UperNet/upernet_huggingface_inference.ipynb) — segmentation-matting; segmentation, scene-understanding
* [VGGT](VGGT/vggt_inference.ipynb) — depth-3d; 3D, visual-geometry, depth-estimation
* [VisionReasoner](VisionReasoner/visionreasoner_inference.ipynb) — vlm; VLM, visual-reasoning
* [WebSSL](WebSSL/webssl_huggingface_inference.ipynb) — retrieval-embedding; image-features, similarity
* [xLAM](xLAM/xlam_huggingface_inferemce.ipynb) — llm; text-generation, agent-actions
* [YOLO-World](YOLO-World/yolow_inference.ipynb) — detection; detection, open-vocabulary-detection
* [YOLOS4Fashion](YOLOS4Fashion/yolos4fashion_huggingface_inference.ipynb) — detection; detection, fashion-detection

### Index (by category)

**anomaly**
  * [AnomalyCLIP](AnomalyCLIP/anomalyclip_inference.ipynb)

**classification-representation**
  * [DINOv3](DINOv3/dinov3_inference.ipynb)
  * [EoMT](EoMT/eomt_huggingface_inference.ipynb)
  * [EVA](EVA/eva_timm_inference.ipynb)
  * [LeViT](LeViT/levit_timm_inference.ipynb)
  * [PoolFormer](PoolFormer/poolformer_huggingface_inference.ipynb)

**depth-3d**
  * [DepthAnything](DepthAnything/depthanything_huggingface_inference.ipynb)
  * [DepthPro](DepthPro/depthpro_inference.ipynb)
  * [DPT](DPT/dpt_huggingface_inference.ipynb)
  * [PromptDepthAnything](PromptDepthAnything/promptdepthanything_huggingface_inference.ipynb)
  * [VGGT](VGGT/vggt_inference.ipynb)

**detection**
  * [DETR](DETR/detr_huggingface_inference.ipynb)
  * [GLIP](GLIP/glip_inference.ipynb)
  * [GroundingDINO](GroundingDINO/groundingdino_huggingface_inference.ipynb)
  * [OV-DINO](OV-DINO/ovdino_inference.ipynb)
  * [OWL-v2](OWL-v2/owlv2_huggingface_inference.ipynb)
  * [OWL-ViT (owlvit_huggingface_inference.ipynb)](OWL-ViT/owlvit_huggingface_inference.ipynb)
  * [OWL-ViT (owlvit_inference-2.ipynb)](OWL-ViT/owlvit_inference-2.ipynb)
  * [YOLO-World](YOLO-World/yolow_inference.ipynb)
  * [YOLOS4Fashion](YOLOS4Fashion/yolos4fashion_huggingface_inference.ipynb)

**generation**
  * [Alfie](Alfie/alfie_inference.ipynb)
  * [AnimateDiff](AnimateDiff/animatediff_huggingface_inference.ipynb)
  * [AuraSR](AuraSR/aurasr_inference.ipynb)
  * [ControlNet](ControlNet/controlnet_inference.ipynb)
  * [FLUX](FLUX/flux_huggingface_inference.ipynb)
  * [GLIDE](GLIDE/glide_inference.ipynb)
  * [ImageGPT](ImageGPT/imagegpt_huggingface_inference.ipynb)
  * [Leffa](Leffa/leffa_inference.ipynb)
  * [SD2](SD2/sd_huggingface_inference.ipynb)
  * [UNO](UNO/uno_huggingface_inference.ipynb)

**llm**
  * [BART](BART/bart_huggingface_inference.ipynb)
  * [BERT-deepset](BERT-deepset/bert-deepset_haystack_inference.ipynb)
  * [EssentialAI](EssentialAI/essentialai_huggingface_inference.ipynb)
  * [Gemma3](Gemma3/gemma3_huggingface_inference.ipynb)
  * [LLaMA2](LLaMA2/llama2_inference.ipynb)
  * [xLAM](xLAM/xlam_huggingface_inferemce.ipynb)

**retrieval-embedding**
  * [CLIP](CLIP/clip_huggingface_inference.ipynb)
  * [FLAVA](FLAVA/flava_huggingface_inference.ipynb)
  * [GCL](GCL/gcl-e5_huggingface_inference.ipynb)
  * [QLIP](QLIP/qlip_huggingface_inference.ipynb)
  * [SigLIP](SigLIP/siglip_huggingface_inference.ipynb)
  * [WebSSL](WebSSL/webssl_huggingface_inference.ipynb)

**segmentation-matting**
  * [AEMatter](AEMatter/aematter_inference.ipynb)
  * [BEN2](BEN2/ben2_huggingface_inference.ipynb)
  * [BiRefNet](BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb)
  * [CAT-Seg](CAT-Seg/catseg_inference.ipynb)
  * [CLIPseg](CLIPseg/clipseg_huggingface_inference.ipynb)
  * [DiffDIS](DiffDIS/diffdis_inference.ipynb)
  * [FaceParsing](FaceParsing/faceparsing_huggingface_inference.ipynb)
  * [FineGrain](FineGrain/finegrainBoxSeg_inference.ipynb)
  * [LISA](LISA/lisa_inference.ipynb)
  * [Mask2Former](Mask2Former/mask2former_huggingface_inference.ipynb)
  * [OneFormer](OneFormer/oneformer_huggingface_inference.ipynb)
  * [OVSeg](OVSeg/ovseg_inference.ipynb)
  * [SAM](SAM/sam_huggingface_inference.ipynb)
  * [SAM-2](SAM-2/sam2_inference.ipynb)
  * [SAM-3](SAM-3/sam3_inference.ipynb)
  * [SAM-HQ](SAM-HQ/samhq_inference.ipynb)
  * [SAMRefiner](SAMRefiner/samrefiner_inference.ipynb)
  * [SAN](SAN/san_inference.ipynb)
  * [SegFormer](SegFormer/segformer-clothes_huggingface_inference.ipynb)
  * [SegZero](SegZero/segzero_inference.ipynb)
  * [UperNet](UperNet/upernet_huggingface_inference.ipynb)

**vlm**
  * [BLIP](BLIP/blip_huggingface_inference.ipynb)
  * [CogVLM](CogVLM/cogvlm_inference.ipynb)
  * [Ferret](Ferret/ferret_inference.ipynb)
  * [InternVL](InternVL/internvl_huggingface_inference.ipynb)
  * [Janus](Janus/janus_huggingface_inference.ipynb)
  * [LLaVA](LLaVA/llava_huggingface_inference.ipynb)
  * [LLaVA-NeXT](LLaVA-NeXT/llavanext_huggingface_inference.ipynb)
  * [LLaVA-OneVision](LLaVA-OneVision/llavaonevision_huggingface_inference.ipynb)
  * [SA2VA](SA2VA/sa2va_huggingface_inference.ipynb)
  * [SmolVLM](SmolVLM/smolvlm_huggingface_inference.ipynb)
  * [VisionReasoner](VisionReasoner/visionreasoner_inference.ipynb)

### Index (by task)

* **3D**: [VGGT](VGGT/vggt_inference.ipynb)
* **agent-actions**: [xLAM](xLAM/xlam_huggingface_inferemce.ipynb)
* **anomaly-detection**: [AnomalyCLIP](AnomalyCLIP/anomalyclip_inference.ipynb)
* **box-prompted-segmentation**: [FineGrain](FineGrain/finegrainBoxSeg_inference.ipynb)
* **captioning**: [BLIP](BLIP/blip_huggingface_inference.ipynb)
* **chat**: [LLaMA2](LLaMA2/llama2_inference.ipynb)
* **clothes-segmentation**: [SegFormer](SegFormer/segformer-clothes_huggingface_inference.ipynb)
* **concept-prompted-segmentation**: [SAM-3](SAM-3/sam3_inference.ipynb)
* **conditioned-generation**: [ControlNet](ControlNet/controlnet_inference.ipynb)
* **contrastive**: [CLIP](CLIP/clip_huggingface_inference.ipynb), [GCL](GCL/gcl-e5_huggingface_inference.ipynb), [SigLIP](SigLIP/siglip_huggingface_inference.ipynb)
* **depth-estimation**: [DepthAnything](DepthAnything/depthanything_huggingface_inference.ipynb), [DepthPro](DepthPro/depthpro_inference.ipynb), [DPT](DPT/dpt_huggingface_inference.ipynb), [PromptDepthAnything](PromptDepthAnything/promptdepthanything_huggingface_inference.ipynb), [VGGT](VGGT/vggt_inference.ipynb)
* **detection**: [DETR](DETR/detr_huggingface_inference.ipynb), [GLIP](GLIP/glip_inference.ipynb), [GroundingDINO](GroundingDINO/groundingdino_huggingface_inference.ipynb), [OV-DINO](OV-DINO/ovdino_inference.ipynb), [OWL-v2](OWL-v2/owlv2_huggingface_inference.ipynb), [OWL-ViT (owlvit_huggingface_inference.ipynb)](OWL-ViT/owlvit_huggingface_inference.ipynb), [OWL-ViT (owlvit_inference-2.ipynb)](OWL-ViT/owlvit_inference-2.ipynb), [YOLO-World](YOLO-World/yolow_inference.ipynb), [YOLOS4Fashion](YOLOS4Fashion/yolos4fashion_huggingface_inference.ipynb)
* **diffusion**: [AnimateDiff](AnimateDiff/animatediff_huggingface_inference.ipynb), [ControlNet](ControlNet/controlnet_inference.ipynb), [FLUX](FLUX/flux_huggingface_inference.ipynb), [GLIDE](GLIDE/glide_inference.ipynb), [SD2](SD2/sd_huggingface_inference.ipynb)
* **DIS**: [BEN2](BEN2/ben2_huggingface_inference.ipynb), [BiRefNet](BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb), [DiffDIS](DiffDIS/diffdis_inference.ipynb)
* **face-parsing**: [FaceParsing](FaceParsing/faceparsing_huggingface_inference.ipynb)
* **fashion-detection**: [YOLOS4Fashion](YOLOS4Fashion/yolos4fashion_huggingface_inference.ipynb)
* **grounded-chat**: [Ferret](Ferret/ferret_inference.ipynb)
* **grounded-understanding**: [SA2VA](SA2VA/sa2va_huggingface_inference.ipynb)
* **grounding**: [GLIP](GLIP/glip_inference.ipynb), [GroundingDINO](GroundingDINO/groundingdino_huggingface_inference.ipynb)
* **high-quality-segmentation**: [SAM-HQ](SAM-HQ/samhq_inference.ipynb)
* **HR-seg**: [BEN2](BEN2/ben2_huggingface_inference.ipynb), [DiffDIS](DiffDIS/diffdis_inference.ipynb)
* **image-classification**: [EVA](EVA/eva_timm_inference.ipynb), [LeViT](LeViT/levit_timm_inference.ipynb), [PoolFormer](PoolFormer/poolformer_huggingface_inference.ipynb)
* **image-features**: [CLIP](CLIP/clip_huggingface_inference.ipynb), [DINOv3](DINOv3/dinov3_inference.ipynb), [EoMT](EoMT/eomt_huggingface_inference.ipynb), [EVA](EVA/eva_timm_inference.ipynb), [PoolFormer](PoolFormer/poolformer_huggingface_inference.ipynb), [QLIP](QLIP/qlip_huggingface_inference.ipynb), [SigLIP](SigLIP/siglip_huggingface_inference.ipynb), [WebSSL](WebSSL/webssl_huggingface_inference.ipynb)
* **image-generation**: [Alfie](Alfie/alfie_inference.ipynb), [AuraSR](AuraSR/aurasr_inference.ipynb), [ControlNet](ControlNet/controlnet_inference.ipynb), [FLUX](FLUX/flux_huggingface_inference.ipynb), [GLIDE](GLIDE/glide_inference.ipynb), [ImageGPT](ImageGPT/imagegpt_huggingface_inference.ipynb), [SD2](SD2/sd_huggingface_inference.ipynb), [UNO](UNO/uno_huggingface_inference.ipynb)
* **image-text**: [FLAVA](FLAVA/flava_huggingface_inference.ipynb)
* **image-text-retrieval**: [BLIP](BLIP/blip_huggingface_inference.ipynb)
* **in-context-generation**: [UNO](UNO/uno_huggingface_inference.ipynb)
* **instance-segmentation**: [OneFormer](OneFormer/oneformer_huggingface_inference.ipynb)
* **matting**: [AEMatter](AEMatter/aematter_inference.ipynb), [BiRefNet](BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb)
* **metric-depth**: [DepthPro](DepthPro/depthpro_inference.ipynb)
* **multimodal**: [FLAVA](FLAVA/flava_huggingface_inference.ipynb)
* **multimodal-generation**: [Janus](Janus/janus_huggingface_inference.ipynb)
* **open-vocabulary-detection**: [GroundingDINO](GroundingDINO/groundingdino_huggingface_inference.ipynb), [OV-DINO](OV-DINO/ovdino_inference.ipynb), [OWL-v2](OWL-v2/owlv2_huggingface_inference.ipynb), [OWL-ViT (owlvit_huggingface_inference.ipynb)](OWL-ViT/owlvit_huggingface_inference.ipynb), [OWL-ViT (owlvit_inference-2.ipynb)](OWL-ViT/owlvit_inference-2.ipynb), [YOLO-World](YOLO-World/yolow_inference.ipynb)
* **open-vocabulary-segmentation**: [CAT-Seg](CAT-Seg/catseg_inference.ipynb), [OVSeg](OVSeg/ovseg_inference.ipynb), [SAN](SAN/san_inference.ipynb)
* **panoptic-segmentation**: [Mask2Former](Mask2Former/mask2former_huggingface_inference.ipynb), [OneFormer](OneFormer/oneformer_huggingface_inference.ipynb)
* **person-image-generation**: [Leffa](Leffa/leffa_inference.ipynb)
* **pixel-modeling**: [ImageGPT](ImageGPT/imagegpt_huggingface_inference.ipynb)
* **prompted-depth**: [PromptDepthAnything](PromptDepthAnything/promptdepthanything_huggingface_inference.ipynb)
* **prompted-segmentation**: [SAM](SAM/sam_huggingface_inference.ipynb), [SAM-2](SAM-2/sam2_inference.ipynb)
* **question-answering**: [BERT-deepset](BERT-deepset/bert-deepset_haystack_inference.ipynb)
* **ranking**: [GCL](GCL/gcl-e5_huggingface_inference.ipynb)
* **reasoning-segmentation**: [LISA](LISA/lisa_inference.ipynb), [SegZero](SegZero/segzero_inference.ipynb)
* **representation-learning**: [DINOv3](DINOv3/dinov3_inference.ipynb)
* **retrieval**: [CLIP](CLIP/clip_huggingface_inference.ipynb), [FLAVA](FLAVA/flava_huggingface_inference.ipynb), [GCL](GCL/gcl-e5_huggingface_inference.ipynb), [SigLIP](SigLIP/siglip_huggingface_inference.ipynb)
* **rgba-generation**: [Alfie](Alfie/alfie_inference.ipynb)
* **scene-understanding**: [UperNet](UperNet/upernet_huggingface_inference.ipynb)
* **seg-refinement**: [SAMRefiner](SAMRefiner/samrefiner_inference.ipynb)
* **segmentation**: [AEMatter](AEMatter/aematter_inference.ipynb), [BEN2](BEN2/ben2_huggingface_inference.ipynb), [BiRefNet](BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb), [CAT-Seg](CAT-Seg/catseg_inference.ipynb), [CLIPseg](CLIPseg/clipseg_huggingface_inference.ipynb), [DiffDIS](DiffDIS/diffdis_inference.ipynb), [EoMT](EoMT/eomt_huggingface_inference.ipynb), [FaceParsing](FaceParsing/faceparsing_huggingface_inference.ipynb), [FineGrain](FineGrain/finegrainBoxSeg_inference.ipynb), [LISA](LISA/lisa_inference.ipynb), [Mask2Former](Mask2Former/mask2former_huggingface_inference.ipynb), [OneFormer](OneFormer/oneformer_huggingface_inference.ipynb), [OVSeg](OVSeg/ovseg_inference.ipynb), [SA2VA](SA2VA/sa2va_huggingface_inference.ipynb), [SAM](SAM/sam_huggingface_inference.ipynb), [SAM-2](SAM-2/sam2_inference.ipynb), [SAM-3](SAM-3/sam3_inference.ipynb), [SAM-HQ](SAM-HQ/samhq_inference.ipynb), [SAMRefiner](SAMRefiner/samrefiner_inference.ipynb), [SAN](SAN/san_inference.ipynb), [SegFormer](SegFormer/segformer-clothes_huggingface_inference.ipynb), [SegZero](SegZero/segzero_inference.ipynb), [UperNet](UperNet/upernet_huggingface_inference.ipynb)
* **semantic-segmentation**: [OneFormer](OneFormer/oneformer_huggingface_inference.ipynb)
* **seq2seq**: [BART](BART/bart_huggingface_inference.ipynb)
* **similarity**: [WebSSL](WebSSL/webssl_huggingface_inference.ipynb)
* **super-resolution**: [AuraSR](AuraSR/aurasr_inference.ipynb)
* **text-aligned-tokenization**: [QLIP](QLIP/qlip_huggingface_inference.ipynb)
* **text-features**: [CLIP](CLIP/clip_huggingface_inference.ipynb), [SigLIP](SigLIP/siglip_huggingface_inference.ipynb)
* **text-generation**: [BART](BART/bart_huggingface_inference.ipynb), [EssentialAI](EssentialAI/essentialai_huggingface_inference.ipynb), [Gemma3](Gemma3/gemma3_huggingface_inference.ipynb), [LLaMA2](LLaMA2/llama2_inference.ipynb), [xLAM](xLAM/xlam_huggingface_inferemce.ipynb)
* **text-prompted-segmentation**: [CLIPseg](CLIPseg/clipseg_huggingface_inference.ipynb)
* **video-generation**: [AnimateDiff](AnimateDiff/animatediff_huggingface_inference.ipynb)
* **virtual-try-on**: [Leffa](Leffa/leffa_inference.ipynb)
* **visual-geometry**: [VGGT](VGGT/vggt_inference.ipynb)
* **visual-reasoning**: [VisionReasoner](VisionReasoner/visionreasoner_inference.ipynb)
* **VLM**: [BLIP](BLIP/blip_huggingface_inference.ipynb), [CogVLM](CogVLM/cogvlm_inference.ipynb), [Ferret](Ferret/ferret_inference.ipynb), [Gemma3](Gemma3/gemma3_huggingface_inference.ipynb), [InternVL](InternVL/internvl_huggingface_inference.ipynb), [Janus](Janus/janus_huggingface_inference.ipynb), [LISA](LISA/lisa_inference.ipynb), [LLaVA](LLaVA/llava_huggingface_inference.ipynb), [LLaVA-NeXT](LLaVA-NeXT/llavanext_huggingface_inference.ipynb), [LLaVA-OneVision](LLaVA-OneVision/llavaonevision_huggingface_inference.ipynb), [SA2VA](SA2VA/sa2va_huggingface_inference.ipynb), [SmolVLM](SmolVLM/smolvlm_huggingface_inference.ipynb), [VisionReasoner](VisionReasoner/visionreasoner_inference.ipynb)
* **VQA**: [BLIP](BLIP/blip_huggingface_inference.ipynb), [CogVLM](CogVLM/cogvlm_inference.ipynb), [InternVL](InternVL/internvl_huggingface_inference.ipynb), [LLaVA](LLaVA/llava_huggingface_inference.ipynb), [LLaVA-NeXT](LLaVA-NeXT/llavanext_huggingface_inference.ipynb), [LLaVA-OneVision](LLaVA-OneVision/llavaonevision_huggingface_inference.ipynb), [SmolVLM](SmolVLM/smolvlm_huggingface_inference.ipynb)
* **zero-shot**: [AnomalyCLIP](AnomalyCLIP/anomalyclip_inference.ipynb)

### Environment Matrix

| Model | Notebook | Environment | Python | Notes |
| --- | --- | --- | --- | --- |
| AEMatter | [aematter_inference.ipynb](AEMatter/aematter_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| Alfie | [alfie_inference.ipynb](Alfie/alfie_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| AnimateDiff | [animatediff_huggingface_inference.ipynb](AnimateDiff/animatediff_huggingface_inference.ipynb) | `diffusers` (envs/diffusers) | `>=3.10,<3.13` | Diffusers-based text/image/video generation notebooks. |
| AnomalyCLIP | [anomalyclip_inference.ipynb](AnomalyCLIP/anomalyclip_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| AuraSR | [aurasr_inference.ipynb](AuraSR/aurasr_inference.ipynb) | `diffusers` (envs/diffusers) | `>=3.10,<3.13` | Diffusers-based text/image/video generation notebooks. |
| BART | [bart_huggingface_inference.ipynb](BART/bart_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| BEN2 | [ben2_huggingface_inference.ipynb](BEN2/ben2_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| BERT-deepset | [bert-deepset_haystack_inference.ipynb](BERT-deepset/bert-deepset_haystack_inference.ipynb) | `haystack` (envs/haystack) | `>=3.10,<3.13` | Haystack question-answering notebook. |
| BiRefNet | [birefnet-hr-matting_huggingface_inference.ipynb](BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| BLIP | [blip_huggingface_inference.ipynb](BLIP/blip_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| CAT-Seg | [catseg_inference.ipynb](CAT-Seg/catseg_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Requires Detectron2 and project-specific open-vocabulary segmentation dependencies. |
| CLIP | [clip_huggingface_inference.ipynb](CLIP/clip_huggingface_inference.ipynb) | `retrieval` (envs/retrieval) | `>=3.10,<3.13` | Embedding, CLIP/SigLIP, and retrieval notebooks. |
| CLIPseg | [clipseg_huggingface_inference.ipynb](CLIPseg/clipseg_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| CogVLM | [cogvlm_inference.ipynb](CogVLM/cogvlm_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| ControlNet | [controlnet_inference.ipynb](ControlNet/controlnet_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| DepthAnything | [depthanything_huggingface_inference.ipynb](DepthAnything/depthanything_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| DepthPro | [depthpro_inference.ipynb](DepthPro/depthpro_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| DETR | [detr_huggingface_inference.ipynb](DETR/detr_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| DiffDIS | [diffdis_inference.ipynb](DiffDIS/diffdis_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| DINOv3 | [dinov3_inference.ipynb](DINOv3/dinov3_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| DPT | [dpt_huggingface_inference.ipynb](DPT/dpt_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| EoMT | [eomt_huggingface_inference.ipynb](EoMT/eomt_huggingface_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| EssentialAI | [essentialai_huggingface_inference.ipynb](EssentialAI/essentialai_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| EVA | [eva_timm_inference.ipynb](EVA/eva_timm_inference.ipynb) | `timm` (envs/timm) | `>=3.10,<3.13` | timm and lightweight representation model notebooks. |
| FaceParsing | [faceparsing_huggingface_inference.ipynb](FaceParsing/faceparsing_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| Ferret | [ferret_inference.ipynb](Ferret/ferret_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Uses a nested project with pinned dependencies and a git Transformers source. |
| FineGrain | [finegrainBoxSeg_inference.ipynb](FineGrain/finegrainBoxSeg_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| FLAVA | [flava_huggingface_inference.ipynb](FLAVA/flava_huggingface_inference.ipynb) | `retrieval` (envs/retrieval) | `>=3.10,<3.13` | Embedding, CLIP/SigLIP, and retrieval notebooks. |
| FLUX | [flux_huggingface_inference.ipynb](FLUX/flux_huggingface_inference.ipynb) | `diffusers` (envs/diffusers) | `>=3.10,<3.13` | Diffusers-based text/image/video generation notebooks. |
| GCL | [gcl-e5_huggingface_inference.ipynb](GCL/gcl-e5_huggingface_inference.ipynb) | `retrieval` (envs/retrieval) | `>=3.10,<3.13` | Embedding, CLIP/SigLIP, and retrieval notebooks. |
| Gemma3 | [gemma3_huggingface_inference.ipynb](Gemma3/gemma3_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| GLIDE | [glide_inference.ipynb](GLIDE/glide_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| GLIP | [glip_inference.ipynb](GLIP/glip_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook documents a Docker image with CUDA 10.2 and PyTorch 1.9; treat as Docker/model-specific unless ported. |
| GroundingDINO | [groundingdino_huggingface_inference.ipynb](GroundingDINO/groundingdino_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| ImageGPT | [imagegpt_huggingface_inference.ipynb](ImageGPT/imagegpt_huggingface_inference.ipynb) | `diffusers` (envs/diffusers) | `>=3.10,<3.13` | Diffusers-based text/image/video generation notebooks. |
| InternVL | [internvl_huggingface_inference.ipynb](InternVL/internvl_huggingface_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| Janus | [janus_huggingface_inference.ipynb](Janus/janus_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| Leffa | [leffa_inference.ipynb](Leffa/leffa_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| LeViT | [levit_timm_inference.ipynb](LeViT/levit_timm_inference.ipynb) | `timm` (envs/timm) | `>=3.10,<3.13` | timm and lightweight representation model notebooks. |
| LISA | [lisa_inference.ipynb](LISA/lisa_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| LLaMA2 | [llama2_inference.ipynb](LLaMA2/llama2_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Requires external Llama model access/download approval. |
| LLaVA | [llava_huggingface_inference.ipynb](LLaVA/llava_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| LLaVA-NeXT | [llavanext_huggingface_inference.ipynb](LLaVA-NeXT/llavanext_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| LLaVA-OneVision | [llavaonevision_huggingface_inference.ipynb](LLaVA-OneVision/llavaonevision_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| Mask2Former | [mask2former_huggingface_inference.ipynb](Mask2Former/mask2former_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| OneFormer | [oneformer_huggingface_inference.ipynb](OneFormer/oneformer_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| OV-DINO | [ovdino_inference.ipynb](OV-DINO/ovdino_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Requires Detectron2/detrex stack and CUDA-specific Torch pins. |
| OVSeg | [ovseg_inference.ipynb](OVSeg/ovseg_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Requires Detectron2 and the facebookresearch/ov-seg project setup. |
| OWL-v2 | [owlv2_huggingface_inference.ipynb](OWL-v2/owlv2_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| OWL-ViT | [owlvit_huggingface_inference.ipynb](OWL-ViT/owlvit_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| OWL-ViT | [owlvit_inference-2.ipynb](OWL-ViT/owlvit_inference-2.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| PoolFormer | [poolformer_huggingface_inference.ipynb](PoolFormer/poolformer_huggingface_inference.ipynb) | `timm` (envs/timm) | `>=3.10,<3.13` | timm and lightweight representation model notebooks. |
| PromptDepthAnything | [promptdepthanything_huggingface_inference.ipynb](PromptDepthAnything/promptdepthanything_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| QLIP | [qlip_huggingface_inference.ipynb](QLIP/qlip_huggingface_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| SA2VA | [sa2va_huggingface_inference.ipynb](SA2VA/sa2va_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| SAM | [sam_huggingface_inference.ipynb](SAM/sam_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| SAM-2 | [sam2_inference.ipynb](SAM-2/sam2_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| SAM-3 | [sam3_inference.ipynb](SAM-3/sam3_inference.ipynb) | `sam3` (envs/sam3) | `>=3.12,<3.13` | Requires Python 3.12, a CUDA-oriented Torch stack, facebookresearch/sam3 editable install, and either local SAM-3 assets or latest Transformers support. |
| SAM-HQ | [samhq_inference.ipynb](SAM-HQ/samhq_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| SAMRefiner | [samrefiner_inference.ipynb](SAMRefiner/samrefiner_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| SAN | [san_inference.ipynb](SAN/san_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| SD2 | [sd_huggingface_inference.ipynb](SD2/sd_huggingface_inference.ipynb) | `diffusers` (envs/diffusers) | `>=3.10,<3.13` | Diffusers-based text/image/video generation notebooks. |
| SegFormer | [segformer-clothes_huggingface_inference.ipynb](SegFormer/segformer-clothes_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| SegZero | [segzero_inference.ipynb](SegZero/segzero_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| SigLIP | [siglip_huggingface_inference.ipynb](SigLIP/siglip_huggingface_inference.ipynb) | `retrieval` (envs/retrieval) | `>=3.10,<3.13` | Embedding, CLIP/SigLIP, and retrieval notebooks. |
| SmolVLM | [smolvlm_huggingface_inference.ipynb](SmolVLM/smolvlm_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| UNO | [uno_huggingface_inference.ipynb](UNO/uno_huggingface_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| UperNet | [upernet_huggingface_inference.ipynb](UperNet/upernet_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| VGGT | [vggt_inference.ipynb](VGGT/vggt_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| VisionReasoner | [visionreasoner_inference.ipynb](VisionReasoner/visionreasoner_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup. |
| WebSSL | [webssl_huggingface_inference.ipynb](WebSSL/webssl_huggingface_inference.ipynb) | `retrieval` (envs/retrieval) | `>=3.10,<3.13` | Embedding, CLIP/SigLIP, and retrieval notebooks. |
| xLAM | [xlam_huggingface_inferemce.ipynb](xLAM/xlam_huggingface_inferemce.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |
| YOLO-World | [yolow_inference.ipynb](YOLO-World/yolow_inference.ipynb) | `model-specific` (model folder setup) | `see setup_notes` | Requires MMDetection/MMEngine stack and model checkpoint. |
| YOLOS4Fashion | [yolos4fashion_huggingface_inference.ipynb](YOLOS4Fashion/yolos4fashion_huggingface_inference.ipynb) | `hf-transformers` (envs/hf-transformers) | `>=3.10,<3.13` | Common Hugging Face Transformers vision, text, and multimodal notebooks. |

### Testing Status

Latest report: 74 notebook entries; 18 passed, 26 failed, 30 blocked.

| Status | Models |
| --- | --- |
| passed | BART, AnimateDiff, BLIP, CLIPseg, DPT, DepthAnything, EVA, EssentialAI, FaceParsing, GCL, LLaVA, LLaVA-NeXT, LLaVA-OneVision, LeViT, PromptDepthAnything, SegFormer, SigLIP, xLAM |
| failed | AuraSR, BEN2, BERT-deepset, BiRefNet, CLIP, DETR, FLAVA, FLUX, Gemma3, GroundingDINO, ImageGPT, Janus, Mask2Former, OWL-ViT (owlvit_huggingface_inference.ipynb), OWL-ViT (owlvit_inference-2.ipynb), OWL-v2, OneFormer, PoolFormer, SA2VA, SAM, SAM-3, SD2, SmolVLM, UperNet, WebSSL, YOLOS4Fashion |
| blocked | AEMatter, Alfie, AnomalyCLIP, CAT-Seg, CogVLM, ControlNet, DINOv3, DepthPro, DiffDIS, EoMT, Ferret, FineGrain, GLIDE, GLIP, InternVL, LISA, LLaMA2, Leffa, OV-DINO, OVSeg, QLIP, SAM-2, SAM-HQ, SAMRefiner, SAN, SegZero, UNO, VGGT, VisionReasoner, YOLO-World |

Notebook execution results are written to `reports/notebook_uv_execution.json` by `tools/execute_notebooks.py`. Source notebook outputs are preserved unless they are explicitly inspected and proven safe to remove.

<!-- AUTO-GENERATED:MODEL-INDEX:END -->

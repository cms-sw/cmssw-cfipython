import FWCore.ParameterSet.Config as cms

def MLPFProducer(*args, **kwargs):
  mod = cms.EDProducer('MLPFProducer',
    src = cms.InputTag('particleFlowBlock'),
    model_path = cms.FileInPath('RecoParticleFlow/PFProducer/data/mlpf/mlpf_5M_attn2x3x256_bm12_relu_checkpoint10_8xmi250_fp32_fused_20250722.onnx'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

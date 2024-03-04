import FWCore.ParameterSet.Config as cms

def MLPFProducer(**kwargs):
  mod = cms.EDProducer('MLPFProducer',
    src = cms.InputTag('particleFlowBlock'),
    model_path = cms.FileInPath('RecoParticleFlow/PFProducer/data/mlpf/mlpf_2021_11_16__no_einsum__all_data_cms-best-of-asha-scikit_20211026_042043_178263.workergpu010.onnx'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

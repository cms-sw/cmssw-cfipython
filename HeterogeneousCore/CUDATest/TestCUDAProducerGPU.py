import FWCore.ParameterSet.Config as cms

def TestCUDAProducerGPU(**kwargs):
  mod = cms.EDProducer('TestCUDAProducerGPU',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

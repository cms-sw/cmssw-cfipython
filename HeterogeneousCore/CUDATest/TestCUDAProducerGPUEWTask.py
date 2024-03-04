import FWCore.ParameterSet.Config as cms

def TestCUDAProducerGPUEWTask(**kwargs):
  mod = cms.EDProducer('TestCUDAProducerGPUEWTask',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

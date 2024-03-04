import FWCore.ParameterSet.Config as cms

def TestCUDAProducerGPUFirst(**kwargs):
  mod = cms.EDProducer('TestCUDAProducerGPUFirst',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TestCUDAProducerCPU(**kwargs):
  mod = cms.EDProducer('TestCUDAProducerCPU',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

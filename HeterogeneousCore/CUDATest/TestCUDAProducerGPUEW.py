import FWCore.ParameterSet.Config as cms

def TestCUDAProducerGPUEW(*args, **kwargs):
  mod = cms.EDProducer('TestCUDAProducerGPUEW',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

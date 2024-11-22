import FWCore.ParameterSet.Config as cms

def TestCUDAProducerGPUtoCPU(*args, **kwargs):
  mod = cms.EDProducer('TestCUDAProducerGPUtoCPU',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

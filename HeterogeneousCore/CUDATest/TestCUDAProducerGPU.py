import FWCore.ParameterSet.Config as cms

def TestCUDAProducerGPU(*args, **kwargs):
  mod = cms.EDProducer('TestCUDAProducerGPU',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

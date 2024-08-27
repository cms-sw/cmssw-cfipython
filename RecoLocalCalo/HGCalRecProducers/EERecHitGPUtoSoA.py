import FWCore.ParameterSet.Config as cms

def EERecHitGPUtoSoA(**kwargs):
  mod = cms.EDProducer('EERecHitGPUtoSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

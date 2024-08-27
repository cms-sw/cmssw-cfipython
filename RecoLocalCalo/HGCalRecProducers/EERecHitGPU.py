import FWCore.ParameterSet.Config as cms

def EERecHitGPU(**kwargs):
  mod = cms.EDProducer('EERecHitGPU',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

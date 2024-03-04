import FWCore.ParameterSet.Config as cms

def HEBRecHitGPU(**kwargs):
  mod = cms.EDProducer('HEBRecHitGPU',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

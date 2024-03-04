import FWCore.ParameterSet.Config as cms

def DTRecHitQuality(**kwargs):
  mod = cms.EDProducer('DTRecHitQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

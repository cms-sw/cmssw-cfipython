import FWCore.ParameterSet.Config as cms

def RandomMultiParticlePGunProducer(**kwargs):
  mod = cms.EDProducer('RandomMultiParticlePGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def FlatRandomMultiParticlePGunProducer(**kwargs):
  mod = cms.EDProducer('FlatRandomMultiParticlePGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

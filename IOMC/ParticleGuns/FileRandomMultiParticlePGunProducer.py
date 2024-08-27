import FWCore.ParameterSet.Config as cms

def FileRandomMultiParticlePGunProducer(**kwargs):
  mod = cms.EDProducer('FileRandomMultiParticlePGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def GEDPhotonCoreProducer(**kwargs):
  mod = cms.EDProducer('GEDPhotonCoreProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

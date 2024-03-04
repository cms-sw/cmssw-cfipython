import FWCore.ParameterSet.Config as cms

def GEDPhotonProducer(**kwargs):
  mod = cms.EDProducer('GEDPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PATGenCandsFromSimTracksProducer(**kwargs):
  mod = cms.EDProducer('PATGenCandsFromSimTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

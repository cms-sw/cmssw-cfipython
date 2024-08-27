import FWCore.ParameterSet.Config as cms

def pfTracksProducer(**kwargs):
  mod = cms.EDProducer('pfTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

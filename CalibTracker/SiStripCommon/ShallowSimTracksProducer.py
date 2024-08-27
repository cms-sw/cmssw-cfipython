import FWCore.ParameterSet.Config as cms

def ShallowSimTracksProducer(**kwargs):
  mod = cms.EDProducer('ShallowSimTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ShallowTracksProducer(**kwargs):
  mod = cms.EDProducer('ShallowTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

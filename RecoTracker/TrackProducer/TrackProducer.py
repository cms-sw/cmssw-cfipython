import FWCore.ParameterSet.Config as cms

def TrackProducer(**kwargs):
  mod = cms.EDProducer('TrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

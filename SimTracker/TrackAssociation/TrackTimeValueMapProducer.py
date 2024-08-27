import FWCore.ParameterSet.Config as cms

def TrackTimeValueMapProducer(**kwargs):
  mod = cms.EDProducer('TrackTimeValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

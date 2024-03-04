import FWCore.ParameterSet.Config as cms

def TrackMCQuality(**kwargs):
  mod = cms.EDProducer('TrackMCQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

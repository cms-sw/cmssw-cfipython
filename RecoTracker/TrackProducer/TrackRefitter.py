import FWCore.ParameterSet.Config as cms

def TrackRefitter(**kwargs):
  mod = cms.EDProducer('TrackRefitter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

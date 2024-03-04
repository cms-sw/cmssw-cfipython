import FWCore.ParameterSet.Config as cms

def TrackExtrapolator(**kwargs):
  mod = cms.EDProducer('TrackExtrapolator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

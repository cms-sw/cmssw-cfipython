import FWCore.ParameterSet.Config as cms

def TrackMCQuality(*args, **kwargs):
  mod = cms.EDProducer('TrackMCQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

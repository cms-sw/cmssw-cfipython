import FWCore.ParameterSet.Config as cms

def TrackFromPVSelector(*args, **kwargs):
  mod = cms.EDProducer('TrackFromPVSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TrackListCombiner(*args, **kwargs):
  mod = cms.EDProducer('TrackListCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

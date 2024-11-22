import FWCore.ParameterSet.Config as cms

def TrackListMerger(*args, **kwargs):
  mod = cms.EDProducer('TrackListMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

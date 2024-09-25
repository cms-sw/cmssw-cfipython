import FWCore.ParameterSet.Config as cms

def DTTrackFinder(*args, **kwargs):
  mod = cms.EDProducer('DTTrackFinder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

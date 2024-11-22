import FWCore.ParameterSet.Config as cms

def HITrackClusterRemover(*args, **kwargs):
  mod = cms.EDProducer('HITrackClusterRemover',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

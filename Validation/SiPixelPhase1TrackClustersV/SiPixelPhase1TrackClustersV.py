import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackClustersV(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackClustersV',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

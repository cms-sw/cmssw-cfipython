import FWCore.ParameterSet.Config as cms

def Phase2TrackerClusterizer(*args, **kwargs):
  mod = cms.EDProducer('Phase2TrackerClusterizer',
    maxClusterSize = cms.uint32(0),
    maxNumberClusters = cms.uint32(0),
    src = cms.InputTag('mix', 'Tracker'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

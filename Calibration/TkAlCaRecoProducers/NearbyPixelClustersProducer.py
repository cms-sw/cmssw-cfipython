import FWCore.ParameterSet.Config as cms

def NearbyPixelClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('NearbyPixelClustersProducer',
    throwBadComponents = cms.bool(False),
    dumpWholeDetIds = cms.bool(False),
    clusterCollection = cms.InputTag('siPixelClusters'),
    trajectoryInput = cms.InputTag('myRefitter'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

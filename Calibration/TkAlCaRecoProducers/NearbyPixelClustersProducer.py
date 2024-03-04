import FWCore.ParameterSet.Config as cms

def NearbyPixelClustersProducer(**kwargs):
  mod = cms.EDProducer('NearbyPixelClustersProducer',
    throwBadComponents = cms.bool(False),
    dumpWholeDetIds = cms.bool(False),
    clusterCollection = cms.InputTag('siPixelClusters'),
    trajectoryInput = cms.InputTag('myRefitter'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

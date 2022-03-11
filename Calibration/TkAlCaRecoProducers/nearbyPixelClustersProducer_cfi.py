import FWCore.ParameterSet.Config as cms

nearbyPixelClustersProducer = cms.EDProducer('NearbyPixelClustersProducer',
  throwBadComponents = cms.bool(False),
  dumpWholeDetIds = cms.bool(False),
  clusterCollection = cms.InputTag('siPixelClusters'),
  trajectoryInput = cms.InputTag('myRefitter'),
  mightGet = cms.optional.untracked.vstring
)

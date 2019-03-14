import FWCore.ParameterSet.Config as cms

hitPairEDProducerDefault = cms.EDProducer('HitPairEDProducer',
  seedingLayers = cms.InputTag('seedingLayersEDProducer'),
  trackingRegions = cms.InputTag('globalTrackingRegionFromBeamSpot'),
  clusterCheck = cms.InputTag('trackerClusterCheck'),
  produceSeedingHitSets = cms.bool(False),
  produceIntermediateHitDoublets = cms.bool(False),
  maxElement = cms.uint32(1000000),
  layerPairs = cms.vuint32(0)
)

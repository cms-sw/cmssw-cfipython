import FWCore.ParameterSet.Config as cms

hitPairEDProducerDefault = cms.EDProducer('HitPairEDProducer',
  seedingLayers = cms.InputTag('seedingLayersEDProducer'),
  trackingRegions = cms.InputTag('globalTrackingRegionFromBeamSpot'),
  trackingRegionsSeedingLayers = cms.InputTag(''),
  clusterCheck = cms.InputTag('trackerClusterCheck'),
  produceSeedingHitSets = cms.bool(False),
  produceIntermediateHitDoublets = cms.bool(False),
  maxElement = cms.uint32(1000000),
  maxElementTotal = cms.uint32(50000000),
  layerPairs = cms.vuint32(0)
)

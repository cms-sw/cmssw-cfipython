import FWCore.ParameterSet.Config as cms

def HitPairEDProducer(**kwargs):
  mod = cms.EDProducer('HitPairEDProducer',
    seedingLayers = cms.InputTag('seedingLayersEDProducer'),
    trackingRegions = cms.InputTag('globalTrackingRegionFromBeamSpot'),
    trackingRegionsSeedingLayers = cms.InputTag(''),
    clusterCheck = cms.InputTag('trackerClusterCheck'),
    produceSeedingHitSets = cms.bool(False),
    produceIntermediateHitDoublets = cms.bool(False),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(50000000),
    putEmptyIfMaxElementReached = cms.bool(False),
    layerPairs = cms.vuint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
import FWCore.ParameterSet.Config as cms

SiStripClusters2ApproxClusters = cms.EDProducer('SiStripClusters2ApproxClusters',
  inputClusters = cms.InputTag('siStripClusters'),
  maxSaturatedStrips = cms.uint32(3),
  clusterShapeHitFilterLabel = cms.string('ClusterShapeHitFilter'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  mightGet = cms.optional.untracked.vstring
)

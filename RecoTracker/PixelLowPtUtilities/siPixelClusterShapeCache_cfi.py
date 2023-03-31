import FWCore.ParameterSet.Config as cms

siPixelClusterShapeCache = cms.EDProducer('SiPixelClusterShapeCacheProducer',
  src = cms.InputTag('siPixelClusters'),
  onDemand = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

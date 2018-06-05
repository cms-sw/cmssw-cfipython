import FWCore.ParameterSet.Config as cms

clusterShapeTrackFilter = cms.EDProducer('ClusterShapeTrackFilterProducer',
  clusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
  ptMin = cms.double(0),
  ptMax = cms.double(999999)
)

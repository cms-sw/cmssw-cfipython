import FWCore.ParameterSet.Config as cms

hiPixelTrackFilter = cms.EDProducer('HIPixelTrackFilterProducer',
  clusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
  VertexCollection = cms.InputTag('hiSelectedPixelVertex'),
  ptMin = cms.double(1.5),
  ptMax = cms.double(999999),
  tipMax = cms.double(0),
  nSigmaTipMaxTolerance = cms.double(6),
  lipMax = cms.double(0.3),
  nSigmaLipMaxTolerance = cms.double(0),
  chi2 = cms.double(1000),
  useClusterShape = cms.bool(False)
)

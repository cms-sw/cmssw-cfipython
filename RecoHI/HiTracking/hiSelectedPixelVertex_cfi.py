import FWCore.ParameterSet.Config as cms

hiSelectedPixelVertex = cms.EDProducer('HIBestVertexProducer',
  beamSpotLabel = cms.InputTag('offlineBeamSpot'),
  adaptiveVertexCollection = cms.InputTag('hiBestAdaptiveVertex'),
  medianVertexCollection = cms.InputTag('hiPixelMedianVertex'),
  useFinalAdaptiveVertexCollection = cms.bool(False),
  finalAdaptiveVertexCollection = cms.InputTag('hiBestOfflinePrimaryVertex')
)

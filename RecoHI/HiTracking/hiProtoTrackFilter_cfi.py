import FWCore.ParameterSet.Config as cms

hiProtoTrackFilter = cms.EDProducer('HIProtoTrackFilterProducer',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  siPixelRecHits = cms.InputTag('siPixelRecHits'),
  ptMin = cms.double(1),
  tipMax = cms.double(1),
  chi2 = cms.double(1000),
  doVariablePtMin = cms.bool(True)
)

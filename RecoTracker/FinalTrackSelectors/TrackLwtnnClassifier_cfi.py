import FWCore.ParameterSet.Config as cms

TrackLwtnnClassifier = cms.EDProducer('TrackLwtnnClassifier',
  src = cms.InputTag(''),
  beamspot = cms.InputTag('offlineBeamSpot'),
  vertices = cms.InputTag('firstStepPrimaryVertices'),
  ignoreVertices = cms.bool(False),
  qualityCuts = cms.vdouble(
    -0.7,
    0.1,
    0.7
  ),
  mva = cms.PSet(
    lwtnnLabel = cms.string('trackSelectionLwtnn')
  )
)

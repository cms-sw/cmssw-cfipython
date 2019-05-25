import FWCore.ParameterSet.Config as cms

TrackMVAClassifierDetached = cms.EDProducer('TrackMVAClassifierDetached',
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
    GBRForestLabel = cms.string(''),
    GBRForestFileName = cms.string('')
  )
)

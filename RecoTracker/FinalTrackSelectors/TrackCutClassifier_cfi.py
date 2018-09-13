import FWCore.ParameterSet.Config as cms

TrackCutClassifier = cms.EDProducer('TrackCutClassifier',
  src = cms.InputTag(''),
  beamspot = cms.InputTag('offlineBeamSpot'),
  vertices = cms.InputTag('firstStepPrimaryVertices'),
  GBRForestLabel = cms.string(''),
  GBRForestFileName = cms.string(''),
  qualityCuts = cms.vdouble(
    -0.7,
    0.1,
    0.7
  ),
  mva = cms.PSet(
    minPixelHits = cms.vint32(
      0,
      0,
      1
    ),
    minLayers = cms.vint32(
      3,
      4,
      5
    ),
    min3DLayers = cms.vint32(
      1,
      2,
      3
    ),
    maxLostLayers = cms.vint32(
      99,
      3,
      3
    ),
    maxChi2 = cms.vdouble(
      9999,
      25,
      16
    ),
    maxChi2n = cms.vdouble(
      9999,
      1,
      0.4
    ),
    maxDz = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    ),
    maxDr = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    )
  )
)

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
    isHLT = cms.bool(False),
    minHits4pass = cms.vint32(
      2147483647,
      2147483647,
      2147483647
    ),
    minHits = cms.vint32(
      0,
      0,
      1
    ),
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
    maxRelPtErr = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    ),
    minNdof = cms.vdouble(
      -1,
      -1,
      -1
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
    minNVtxTrk = cms.int32(2),
    maxDz = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    ),
    maxDzWrtBS = cms.vdouble(
      3.4028234663852886e+38,
      24,
      15
    ),
    maxDr = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    ),
    dz_par = cms.PSet(
      dz_exp = cms.vint32(
        2147483647,
        2147483647,
        2147483647
      ),
      dz_par1 = cms.vdouble(
        3.4028234663852886e+38,
        3.4028234663852886e+38,
        3.4028234663852886e+38
      ),
      dz_par2 = cms.vdouble(
        3.4028234663852886e+38,
        3.4028234663852886e+38,
        3.4028234663852886e+38
      ),
      dzWPVerr_par = cms.vdouble(
        3.4028234663852886e+38,
        3.4028234663852886e+38,
        3.4028234663852886e+38
      )
    ),
    dr_par = cms.PSet(
      dr_exp = cms.vint32(
        2147483647,
        2147483647,
        2147483647
      ),
      dr_par1 = cms.vdouble(
        3.4028234663852886e+38,
        3.4028234663852886e+38,
        3.4028234663852886e+38
      ),
      dr_par2 = cms.vdouble(
        3.4028234663852886e+38,
        3.4028234663852886e+38,
        3.4028234663852886e+38
      ),
      d0err = cms.vdouble(
        0.003,
        0.003,
        0.003
      ),
      d0err_par = cms.vdouble(
        0.001,
        0.001,
        0.001
      ),
      drWPVerr_par = cms.vdouble(
        3.4028234663852886e+38,
        3.4028234663852886e+38,
        3.4028234663852886e+38
      )
    )
  )
)

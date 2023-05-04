import FWCore.ParameterSet.Config as cms

hgcalGeometryNewCornersTest = cms.EDAnalyzer('HGCalGeometryNewCornersTest',
  detectorName = cms.string('HGCalHESiliconSensitive'),
  layers = cms.vint32(
    27,
    28,
    29,
    30,
    31,
    32
  ),
  waferUs = cms.vint32(
    -2,
    -3,
    1,
    -8,
    2,
    8
  ),
  waferVs = cms.vint32(
    0,
    -2,
    3,
    0,
    9,
    0
  ),
  types = cms.vint32(
    0,
    0,
    0,
    2,
    2,
    2
  ),
  debugFlag = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

hgcalGeometryRotCheck = cms.EDAnalyzer('HGCalGeometryRotCheck',
  detectorName = cms.string('HGCalHESiliconSensitive'),
  layers = cms.vint32(
    27,
    28,
    29,
    30,
    31,
    32,
    33
  ),
  mightGet = cms.optional.untracked.vstring
)

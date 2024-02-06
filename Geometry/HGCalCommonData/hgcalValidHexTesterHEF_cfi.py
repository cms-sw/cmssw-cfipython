import FWCore.ParameterSet.Config as cms

hgcalValidHexTesterHEF = cms.EDAnalyzer('HGCalValidHexTester',
  NameDevice = cms.string('HGCal HE Silicon'),
  NameSense = cms.string('HGCalHESiliconSensitive'),
  Layers = cms.vint32(
    21,
    21,
    22,
    22
  ),
  ModuleU = cms.vint32(
    3,
    -3,
    3,
    -3
  ),
  ModuleV = cms.vint32(
    6,
    -6,
    6,
    -6
  ),
  Types = cms.vint32(
    2,
    2,
    2,
    2
  ),
  mightGet = cms.optional.untracked.vstring
)

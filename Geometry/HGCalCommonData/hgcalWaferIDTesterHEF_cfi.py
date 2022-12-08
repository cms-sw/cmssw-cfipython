import FWCore.ParameterSet.Config as cms

hgcalWaferIDTesterHEF = cms.EDAnalyzer('HGCalWaferIDTester',
  nameSense = cms.string('HGCalHESiliconSensitive'),
  fileName = cms.string('cellIDHEF.txt'),
  mode = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)

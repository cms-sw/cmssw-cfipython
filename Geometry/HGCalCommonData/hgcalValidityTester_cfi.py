import FWCore.ParameterSet.Config as cms

hgcalValidityTester = cms.EDAnalyzer('HGCalValidityTester',
  nameDetectors = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'HGCalHEScintillatorSensitive'
  ),
  fileName = cms.string('missD88.txt'),
  mightGet = cms.optional.untracked.vstring
)

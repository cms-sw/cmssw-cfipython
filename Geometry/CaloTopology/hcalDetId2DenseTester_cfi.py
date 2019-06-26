import FWCore.ParameterSet.Config as cms

hcalDetId2DenseTester = cms.EDAnalyzer('HcalDetId2DenseTester',
  fileName = cms.untracked.string(''),
  testCalib = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)

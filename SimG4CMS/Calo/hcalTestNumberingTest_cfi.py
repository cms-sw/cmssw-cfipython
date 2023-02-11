import FWCore.ParameterSet.Config as cms

hcalTestNumberingTest = cms.EDAnalyzer('HcalTestNumberingTester',
  mightGet = cms.optional.untracked.vstring
)

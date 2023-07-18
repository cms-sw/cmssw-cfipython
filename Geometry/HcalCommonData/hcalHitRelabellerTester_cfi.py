import FWCore.ParameterSet.Config as cms

hcalHitRelabellerTester = cms.EDAnalyzer('HcalHitRelabellerTester',
  neutralDensity = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)

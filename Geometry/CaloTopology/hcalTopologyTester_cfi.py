import FWCore.ParameterSet.Config as cms

hcalTopologyTester = cms.EDAnalyzer('HcalTopologyTester',
  mightGet = cms.optional.untracked.vstring
)

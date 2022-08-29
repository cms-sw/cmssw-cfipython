import FWCore.ParameterSet.Config as cms

fastTimeTopologyTester = cms.EDAnalyzer('FastTimeTopologyTester',
  mightGet = cms.optional.untracked.vstring
)

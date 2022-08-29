import FWCore.ParameterSet.Config as cms

testAlpakaAnalyzer = cms.EDAnalyzer('TestAlpakaAnalyzer',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

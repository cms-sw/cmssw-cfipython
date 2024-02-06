import FWCore.ParameterSet.Config as cms

testAlpakaObjectAnalyzer = cms.EDAnalyzer('TestAlpakaObjectAnalyzer',
  source = cms.required.InputTag,
  expectBackend = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

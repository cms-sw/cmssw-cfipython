import FWCore.ParameterSet.Config as cms

testAlpakaAnalyzer = cms.EDAnalyzer('TestAlpakaAnalyzer',
  source = cms.required.InputTag,
  expectSize = cms.int32(-1),
  expectBackend = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

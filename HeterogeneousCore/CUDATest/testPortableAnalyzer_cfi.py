import FWCore.ParameterSet.Config as cms

testPortableAnalyzer = cms.EDAnalyzer('TestPortableAnalyzer',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

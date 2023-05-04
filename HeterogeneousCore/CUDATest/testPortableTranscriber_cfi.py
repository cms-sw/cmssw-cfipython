import FWCore.ParameterSet.Config as cms

testPortableTranscriber = cms.EDProducer('TestPortableTranscriber',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

l1tZDCAnalyzer = cms.EDAnalyzer('L1TZDCAnalyzer',
  etSumTag = cms.InputTag('etSumZdcProducer'),
  mightGet = cms.optional.untracked.vstring
)

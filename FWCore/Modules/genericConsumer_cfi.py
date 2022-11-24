import FWCore.ParameterSet.Config as cms

genericConsumer = cms.EDAnalyzer('GenericConsumer',
  eventProducts = cms.untracked.vstring(),
  lumiProducts = cms.untracked.vstring(),
  runProducts = cms.untracked.vstring(),
  mightGet = cms.optional.untracked.vstring
)

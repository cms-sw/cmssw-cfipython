import FWCore.ParameterSet.Config as cms

ClassifierMerger = cms.EDProducer('ClassifierMerger',
  inputClassifiers = cms.vstring(),
  mightGet = cms.optional.untracked.vstring
)

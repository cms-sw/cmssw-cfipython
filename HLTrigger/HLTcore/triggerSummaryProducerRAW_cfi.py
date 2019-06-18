import FWCore.ParameterSet.Config as cms

triggerSummaryProducerRAW = cms.EDProducer('TriggerSummaryProducerRAW',
  processName = cms.string('@'),
  mightGet = cms.optional.untracked.vstring
)

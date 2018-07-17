import FWCore.ParameterSet.Config as cms

triggerSummaryProducerAOD = cms.EDProducer('TriggerSummaryProducerAOD',
  throw = cms.bool(False),
  processName = cms.string('@'),
  moduleLabelPatternsToMatch = cms.vstring('hlt*'),
  moduleLabelPatternsToSkip = cms.vstring()
)

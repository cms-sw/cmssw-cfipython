import FWCore.ParameterSet.Config as cms

def TriggerSummaryProducerAOD(**kwargs):
  mod = cms.EDProducer('TriggerSummaryProducerAOD',
    throw = cms.bool(False),
    processName = cms.string('@'),
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

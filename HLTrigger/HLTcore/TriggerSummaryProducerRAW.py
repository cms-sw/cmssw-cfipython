import FWCore.ParameterSet.Config as cms

def TriggerSummaryProducerRAW(**kwargs):
  mod = cms.EDProducer('TriggerSummaryProducerRAW',
    processName = cms.string('@'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TriggerSummaryProducerRAW(*args, **kwargs):
  mod = cms.EDProducer('TriggerSummaryProducerRAW',
    processName = cms.string('@'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

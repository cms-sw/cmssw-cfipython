import FWCore.ParameterSet.Config as cms

def P2GTTriggerResultsConverter(*args, **kwargs):
  mod = cms.EDProducer('P2GTTriggerResultsConverter',
    src = cms.required.InputTag,
    prefix = cms.string('L1_'),
    decision = cms.string('final'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

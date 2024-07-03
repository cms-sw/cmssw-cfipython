import FWCore.ParameterSet.Config as cms

def P2GTTriggerResultsConverter(**kwargs):
  mod = cms.EDProducer('P2GTTriggerResultsConverter',
    src = cms.required.InputTag,
    prefix = cms.string('L1_'),
    decision = cms.string('final'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

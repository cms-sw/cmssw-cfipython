import FWCore.ParameterSet.Config as cms

def APVCyclePhaseProducerFromL1TS(*args, **kwargs):
  mod = cms.EDProducer('APVCyclePhaseProducerFromL1TS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

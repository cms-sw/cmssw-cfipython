import FWCore.ParameterSet.Config as cms

def APVCyclePhaseProducerFromL1TS(**kwargs):
  mod = cms.EDProducer('APVCyclePhaseProducerFromL1TS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

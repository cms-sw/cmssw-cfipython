import FWCore.ParameterSet.Config as cms

def APVCyclePhaseProducerFromL1ABC(**kwargs):
  mod = cms.EDProducer('APVCyclePhaseProducerFromL1ABC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

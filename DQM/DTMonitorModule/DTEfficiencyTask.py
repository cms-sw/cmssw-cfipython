import FWCore.ParameterSet.Config as cms

def DTEfficiencyTask(**kwargs):
  mod = cms.EDProducer('DTEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

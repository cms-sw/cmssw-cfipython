import FWCore.ParameterSet.Config as cms

def DTTnPEfficiencyTask(**kwargs):
  mod = cms.EDProducer('DTTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

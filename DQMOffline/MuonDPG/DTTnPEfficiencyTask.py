import FWCore.ParameterSet.Config as cms

def DTTnPEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('DTTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

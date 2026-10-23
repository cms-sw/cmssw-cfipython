import FWCore.ParameterSet.Config as cms

def DTEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('DTEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

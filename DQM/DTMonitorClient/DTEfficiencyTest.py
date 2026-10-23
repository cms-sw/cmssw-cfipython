import FWCore.ParameterSet.Config as cms

def DTEfficiencyTest(*args, **kwargs):
  mod = cms.EDProducer('DTEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

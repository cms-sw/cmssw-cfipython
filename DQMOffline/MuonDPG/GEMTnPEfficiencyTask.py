import FWCore.ParameterSet.Config as cms

def GEMTnPEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('GEMTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

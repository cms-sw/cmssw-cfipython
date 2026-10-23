import FWCore.ParameterSet.Config as cms

def DTChamberEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('DTChamberEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

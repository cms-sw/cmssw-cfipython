import FWCore.ParameterSet.Config as cms

def DTChamberEfficiencyTest(*args, **kwargs):
  mod = cms.EDProducer('DTChamberEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DTChamberEfficiency(*args, **kwargs):
  mod = cms.EDProducer('DTChamberEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

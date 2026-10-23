import FWCore.ParameterSet.Config as cms

def DTTFFEDSim(*args, **kwargs):
  mod = cms.EDProducer('DTTFFEDSim',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

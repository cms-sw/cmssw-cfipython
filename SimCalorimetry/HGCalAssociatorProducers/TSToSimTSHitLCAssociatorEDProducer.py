import FWCore.ParameterSet.Config as cms

def TSToSimTSHitLCAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('TSToSimTSHitLCAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

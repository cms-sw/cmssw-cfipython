import FWCore.ParameterSet.Config as cms

def TSToSCAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('TSToSCAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

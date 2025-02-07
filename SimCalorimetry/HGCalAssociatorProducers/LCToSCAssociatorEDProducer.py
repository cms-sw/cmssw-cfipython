import FWCore.ParameterSet.Config as cms

def LCToSCAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('LCToSCAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

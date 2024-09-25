import FWCore.ParameterSet.Config as cms

def MCToCPAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MCToCPAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

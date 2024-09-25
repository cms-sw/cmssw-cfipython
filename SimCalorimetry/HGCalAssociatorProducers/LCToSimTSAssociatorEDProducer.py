import FWCore.ParameterSet.Config as cms

def LCToSimTSAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('LCToSimTSAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

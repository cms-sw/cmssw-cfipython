import FWCore.ParameterSet.Config as cms

def LCToSCAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('LCToSCAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def LCToCPAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('LCToCPAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

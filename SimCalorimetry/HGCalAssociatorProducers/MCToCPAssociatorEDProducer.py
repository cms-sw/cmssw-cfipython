import FWCore.ParameterSet.Config as cms

def MCToCPAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MCToCPAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

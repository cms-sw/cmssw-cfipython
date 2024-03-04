import FWCore.ParameterSet.Config as cms

def TSToSCAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('TSToSCAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

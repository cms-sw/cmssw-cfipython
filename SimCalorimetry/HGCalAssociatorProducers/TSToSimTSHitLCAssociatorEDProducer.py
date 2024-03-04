import FWCore.ParameterSet.Config as cms

def TSToSimTSHitLCAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('TSToSimTSHitLCAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

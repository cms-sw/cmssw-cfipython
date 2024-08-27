import FWCore.ParameterSet.Config as cms

def LCToSimTSAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('LCToSimTSAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

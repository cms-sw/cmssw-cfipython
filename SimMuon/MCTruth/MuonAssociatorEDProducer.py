import FWCore.ParameterSet.Config as cms

def MuonAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MuonAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

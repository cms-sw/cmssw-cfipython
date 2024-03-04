import FWCore.ParameterSet.Config as cms

def LCToSimTSAssociatorByEnergyScoreProducer(**kwargs):
  mod = cms.EDProducer('LCToSimTSAssociatorByEnergyScoreProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

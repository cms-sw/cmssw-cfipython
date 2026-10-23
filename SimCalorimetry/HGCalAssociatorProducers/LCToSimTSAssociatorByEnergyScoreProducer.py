import FWCore.ParameterSet.Config as cms

def LCToSimTSAssociatorByEnergyScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('LCToSimTSAssociatorByEnergyScoreProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def MuonSpecialVariables(**kwargs):
  mod = cms.EDProducer('MuonSpecialVariables',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

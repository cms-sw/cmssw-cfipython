import FWCore.ParameterSet.Config as cms

def MuonSpecialVariables(*args, **kwargs):
  mod = cms.EDProducer('MuonSpecialVariables',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

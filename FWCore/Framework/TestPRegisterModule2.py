import FWCore.ParameterSet.Config as cms

def TestPRegisterModule2(**kwargs):
  mod = cms.EDProducer('TestPRegisterModule2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

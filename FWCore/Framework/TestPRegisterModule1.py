import FWCore.ParameterSet.Config as cms

def TestPRegisterModule1(**kwargs):
  mod = cms.EDProducer('TestPRegisterModule1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

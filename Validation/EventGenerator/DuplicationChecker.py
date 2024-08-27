import FWCore.ParameterSet.Config as cms

def DuplicationChecker(**kwargs):
  mod = cms.EDProducer('DuplicationChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

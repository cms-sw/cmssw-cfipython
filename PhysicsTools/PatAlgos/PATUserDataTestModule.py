import FWCore.ParameterSet.Config as cms

def PATUserDataTestModule(**kwargs):
  mod = cms.EDProducer('PATUserDataTestModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

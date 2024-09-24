import FWCore.ParameterSet.Config as cms

def PATUserDataTestModule(*args, **kwargs):
  mod = cms.EDProducer('PATUserDataTestModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DuplicationChecker(*args, **kwargs):
  mod = cms.EDProducer('DuplicationChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

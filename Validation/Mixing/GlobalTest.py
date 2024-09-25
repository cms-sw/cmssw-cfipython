import FWCore.ParameterSet.Config as cms

def GlobalTest(*args, **kwargs):
  mod = cms.EDProducer('GlobalTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

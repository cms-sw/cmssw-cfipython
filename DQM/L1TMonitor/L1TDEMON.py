import FWCore.ParameterSet.Config as cms

def L1TDEMON(*args, **kwargs):
  mod = cms.EDProducer('L1TDEMON',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

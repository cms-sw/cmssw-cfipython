import FWCore.ParameterSet.Config as cms

def L1RCTTPGProvider(*args, **kwargs):
  mod = cms.EDProducer('L1RCTTPGProvider',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

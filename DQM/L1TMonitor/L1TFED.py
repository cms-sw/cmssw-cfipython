import FWCore.ParameterSet.Config as cms

def L1TFED(*args, **kwargs):
  mod = cms.EDProducer('L1TFED',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

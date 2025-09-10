import FWCore.ParameterSet.Config as cms

def MuBxSelector(*args, **kwargs):
  mod = cms.EDProducer('MuBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

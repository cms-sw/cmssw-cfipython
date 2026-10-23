import FWCore.ParameterSet.Config as cms

def TestInterProcessProd(*args, **kwargs):
  mod = cms.EDProducer('TestInterProcessProd',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

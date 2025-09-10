import FWCore.ParameterSet.Config as cms

def FastSimProducer(*args, **kwargs):
  mod = cms.EDProducer('FastSimProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

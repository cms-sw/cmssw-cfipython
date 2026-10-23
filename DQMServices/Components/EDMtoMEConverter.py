import FWCore.ParameterSet.Config as cms

def EDMtoMEConverter(*args, **kwargs):
  mod = cms.EDProducer('EDMtoMEConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

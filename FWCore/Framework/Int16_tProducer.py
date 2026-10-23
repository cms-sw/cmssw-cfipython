import FWCore.ParameterSet.Config as cms

def Int16_tProducer(*args, **kwargs):
  mod = cms.EDProducer('Int16_tProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

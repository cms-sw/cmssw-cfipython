import FWCore.ParameterSet.Config as cms

def GenMETProducer(*args, **kwargs):
  mod = cms.EDProducer('GenMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

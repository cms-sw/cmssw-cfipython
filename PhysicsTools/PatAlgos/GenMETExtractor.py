import FWCore.ParameterSet.Config as cms

def GenMETExtractor(*args, **kwargs):
  mod = cms.EDProducer('GenMETExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

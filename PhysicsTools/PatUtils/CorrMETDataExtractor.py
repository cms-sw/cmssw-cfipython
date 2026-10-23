import FWCore.ParameterSet.Config as cms

def CorrMETDataExtractor(*args, **kwargs):
  mod = cms.EDProducer('CorrMETDataExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

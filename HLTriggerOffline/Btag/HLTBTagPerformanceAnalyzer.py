import FWCore.ParameterSet.Config as cms

def HLTBTagPerformanceAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HLTBTagPerformanceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

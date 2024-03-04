import FWCore.ParameterSet.Config as cms

def HLTBTagPerformanceAnalyzer(**kwargs):
  mod = cms.EDProducer('HLTBTagPerformanceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

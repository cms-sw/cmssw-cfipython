import FWCore.ParameterSet.Config as cms

def BTagPerformanceAnalyzerOnData(**kwargs):
  mod = cms.EDProducer('BTagPerformanceAnalyzerOnData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

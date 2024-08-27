import FWCore.ParameterSet.Config as cms

def BTagPerformanceAnalyzerMC(**kwargs):
  mod = cms.EDProducer('BTagPerformanceAnalyzerMC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

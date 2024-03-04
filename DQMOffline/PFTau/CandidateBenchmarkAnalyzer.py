import FWCore.ParameterSet.Config as cms

def CandidateBenchmarkAnalyzer(**kwargs):
  mod = cms.EDProducer('CandidateBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

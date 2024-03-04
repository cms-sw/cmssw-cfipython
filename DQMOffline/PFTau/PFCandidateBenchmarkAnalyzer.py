import FWCore.ParameterSet.Config as cms

def PFCandidateBenchmarkAnalyzer(**kwargs):
  mod = cms.EDProducer('PFCandidateBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

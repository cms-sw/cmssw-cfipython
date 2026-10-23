import FWCore.ParameterSet.Config as cms

def PFCandidateBenchmarkAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PFCandidateBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

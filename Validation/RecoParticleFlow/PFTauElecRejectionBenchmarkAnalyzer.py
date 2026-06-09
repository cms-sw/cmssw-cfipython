import FWCore.ParameterSet.Config as cms

def PFTauElecRejectionBenchmarkAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PFTauElecRejectionBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

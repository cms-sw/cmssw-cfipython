import FWCore.ParameterSet.Config as cms

def PFTauElecRejectionBenchmarkAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PFTauElecRejectionBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

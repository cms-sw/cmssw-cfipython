import FWCore.ParameterSet.Config as cms

def GammaJetAnalysis(**kwargs):
  mod = cms.EDAnalyzer('GammaJetAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

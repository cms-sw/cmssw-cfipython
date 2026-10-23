import FWCore.ParameterSet.Config as cms

def GammaJetAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('GammaJetAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

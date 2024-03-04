import FWCore.ParameterSet.Config as cms

def PileupJetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PileupJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

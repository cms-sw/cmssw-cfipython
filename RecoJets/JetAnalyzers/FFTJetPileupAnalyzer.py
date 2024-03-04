import FWCore.ParameterSet.Config as cms

def FFTJetPileupAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('FFTJetPileupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

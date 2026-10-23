import FWCore.ParameterSet.Config as cms

def FFTJetPileupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('FFTJetPileupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

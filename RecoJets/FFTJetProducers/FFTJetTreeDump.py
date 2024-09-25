import FWCore.ParameterSet.Config as cms

def FFTJetTreeDump(*args, **kwargs):
  mod = cms.EDAnalyzer('FFTJetTreeDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

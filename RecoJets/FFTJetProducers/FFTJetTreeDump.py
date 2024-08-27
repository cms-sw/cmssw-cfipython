import FWCore.ParameterSet.Config as cms

def FFTJetTreeDump(**kwargs):
  mod = cms.EDAnalyzer('FFTJetTreeDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

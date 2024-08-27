import FWCore.ParameterSet.Config as cms

def printGenJetRatio(**kwargs):
  mod = cms.EDAnalyzer('printGenJetRatio',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

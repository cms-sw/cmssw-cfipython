import FWCore.ParameterSet.Config as cms

def makeSignals(**kwargs):
  mod = cms.EDAnalyzer('makeSignals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

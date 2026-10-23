import FWCore.ParameterSet.Config as cms

def makeSignals(*args, **kwargs):
  mod = cms.EDAnalyzer('makeSignals',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

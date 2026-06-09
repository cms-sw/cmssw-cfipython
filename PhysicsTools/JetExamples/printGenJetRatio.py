import FWCore.ParameterSet.Config as cms

def printGenJetRatio(*args, **kwargs):
  mod = cms.EDAnalyzer('printGenJetRatio',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

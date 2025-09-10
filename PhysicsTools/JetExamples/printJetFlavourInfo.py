import FWCore.ParameterSet.Config as cms

def printJetFlavourInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('printJetFlavourInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def printJetFlavour(*args, **kwargs):
  mod = cms.EDAnalyzer('printJetFlavour',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

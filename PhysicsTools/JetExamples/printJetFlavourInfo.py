import FWCore.ParameterSet.Config as cms

def printJetFlavourInfo(**kwargs):
  mod = cms.EDAnalyzer('printJetFlavourInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

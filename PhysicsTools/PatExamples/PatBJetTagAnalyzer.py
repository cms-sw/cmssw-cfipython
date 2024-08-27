import FWCore.ParameterSet.Config as cms

def PatBJetTagAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatBJetTagAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

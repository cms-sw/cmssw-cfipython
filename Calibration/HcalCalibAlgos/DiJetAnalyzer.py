import FWCore.ParameterSet.Config as cms

def DiJetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DiJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

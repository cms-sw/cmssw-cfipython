import FWCore.ParameterSet.Config as cms

def DijetRatioCaloJets(**kwargs):
  mod = cms.EDAnalyzer('DijetRatioCaloJets',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def MCvsRecoVerticesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MCvsRecoVerticesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

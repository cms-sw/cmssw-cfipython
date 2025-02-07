import FWCore.ParameterSet.Config as cms

def MCvsRecoVerticesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MCvsRecoVerticesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

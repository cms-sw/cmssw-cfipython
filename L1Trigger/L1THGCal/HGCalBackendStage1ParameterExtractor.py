import FWCore.ParameterSet.Config as cms

def HGCalBackendStage1ParameterExtractor(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalBackendStage1ParameterExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

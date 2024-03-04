import FWCore.ParameterSet.Config as cms

def HGCalBackendStage1ParameterExtractor(**kwargs):
  mod = cms.EDAnalyzer('HGCalBackendStage1ParameterExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

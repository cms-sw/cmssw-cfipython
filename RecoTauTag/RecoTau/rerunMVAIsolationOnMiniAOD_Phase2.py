import FWCore.ParameterSet.Config as cms

def rerunMVAIsolationOnMiniAOD_Phase2(**kwargs):
  mod = cms.EDAnalyzer('rerunMVAIsolationOnMiniAOD_Phase2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

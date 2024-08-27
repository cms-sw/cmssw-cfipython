import FWCore.ParameterSet.Config as cms

def rerunMVAIsolationOnMiniAOD(**kwargs):
  mod = cms.EDAnalyzer('rerunMVAIsolationOnMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

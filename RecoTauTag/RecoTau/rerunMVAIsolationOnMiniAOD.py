import FWCore.ParameterSet.Config as cms

def rerunMVAIsolationOnMiniAOD(*args, **kwargs):
  mod = cms.EDAnalyzer('rerunMVAIsolationOnMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

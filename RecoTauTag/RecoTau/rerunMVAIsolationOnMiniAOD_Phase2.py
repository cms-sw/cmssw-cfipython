import FWCore.ParameterSet.Config as cms

def rerunMVAIsolationOnMiniAOD_Phase2(*args, **kwargs):
  mod = cms.EDAnalyzer('rerunMVAIsolationOnMiniAOD_Phase2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

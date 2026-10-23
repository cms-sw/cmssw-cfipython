import FWCore.ParameterSet.Config as cms

def SurveyToTransforms(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyToTransforms',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

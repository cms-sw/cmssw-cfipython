import FWCore.ParameterSet.Config as cms

def CreateSurveyRcds(*args, **kwargs):
  mod = cms.EDAnalyzer('CreateSurveyRcds',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

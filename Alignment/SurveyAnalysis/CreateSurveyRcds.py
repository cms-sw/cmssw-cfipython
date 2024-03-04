import FWCore.ParameterSet.Config as cms

def CreateSurveyRcds(**kwargs):
  mod = cms.EDAnalyzer('CreateSurveyRcds',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

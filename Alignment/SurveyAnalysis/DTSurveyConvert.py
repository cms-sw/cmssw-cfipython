import FWCore.ParameterSet.Config as cms

def DTSurveyConvert(**kwargs):
  mod = cms.EDAnalyzer('DTSurveyConvert',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

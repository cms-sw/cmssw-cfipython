import FWCore.ParameterSet.Config as cms

def SurveyDBUploader(**kwargs):
  mod = cms.EDAnalyzer('SurveyDBUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

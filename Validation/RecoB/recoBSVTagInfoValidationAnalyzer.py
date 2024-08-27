import FWCore.ParameterSet.Config as cms

def recoBSVTagInfoValidationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('recoBSVTagInfoValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

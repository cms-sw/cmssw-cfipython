import FWCore.ParameterSet.Config as cms

def SVTagInfoValidationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SVTagInfoValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

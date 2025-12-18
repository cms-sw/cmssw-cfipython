import FWCore.ParameterSet.Config as cms

def recoBSVTagInfoValidationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('recoBSVTagInfoValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def SVTagInfoValidationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SVTagInfoValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

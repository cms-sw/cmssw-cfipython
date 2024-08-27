import FWCore.ParameterSet.Config as cms

def BuiltinIntTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('BuiltinIntTestAnalyzer',
    valueMustMatch = cms.required.untracked.int32,
    moduleLabel = cms.required.untracked.InputTag,
    valueMustBeMissing = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

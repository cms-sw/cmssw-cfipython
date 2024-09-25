import FWCore.ParameterSet.Config as cms

def BuiltinIntTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('BuiltinIntTestAnalyzer',
    valueMustMatch = cms.required.untracked.int32,
    moduleLabel = cms.required.untracked.InputTag,
    valueMustBeMissing = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

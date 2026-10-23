import FWCore.ParameterSet.Config as cms

def IntTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('IntTestAnalyzer',
    valueMustMatch = cms.required.untracked.int32,
    moduleLabel = cms.required.untracked.InputTag,
    valueMustBeMissing = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

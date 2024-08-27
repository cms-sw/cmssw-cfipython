import FWCore.ParameterSet.Config as cms

def IntTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('IntTestAnalyzer',
    valueMustMatch = cms.required.untracked.int32,
    moduleLabel = cms.required.untracked.InputTag,
    valueMustBeMissing = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TestParentage(*args, **kwargs):
  mod = cms.EDAnalyzer('TestParentage',
    inputTag = cms.required.InputTag,
    expectedAncestors = cms.required.vstring,
    callGetProvenance = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

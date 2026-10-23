import FWCore.ParameterSet.Config as cms

def SimpleViewAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SimpleViewAnalyzer',
    checkSize = cms.untracked.bool(True),
    sizeMustMatch = cms.required.untracked.uint32,
    label = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

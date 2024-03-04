import FWCore.ParameterSet.Config as cms

def SimpleViewAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SimpleViewAnalyzer',
    checkSize = cms.untracked.bool(True),
    sizeMustMatch = cms.required.untracked.uint32,
    label = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

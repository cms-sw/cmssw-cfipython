import FWCore.ParameterSet.Config as cms

def ThinnedRefFromTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ThinnedRefFromTestAnalyzer',
    parentTag = cms.required.InputTag,
    thinnedTag = cms.required.InputTag,
    unrelatedTag = cms.required.InputTag,
    trackTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

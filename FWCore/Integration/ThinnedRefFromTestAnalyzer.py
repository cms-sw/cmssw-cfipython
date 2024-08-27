import FWCore.ParameterSet.Config as cms

def ThinnedRefFromTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ThinnedRefFromTestAnalyzer',
    parentTag = cms.required.InputTag,
    thinnedTag = cms.required.InputTag,
    unrelatedTag = cms.required.InputTag,
    trackTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

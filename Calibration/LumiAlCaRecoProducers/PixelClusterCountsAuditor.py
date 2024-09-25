import FWCore.ParameterSet.Config as cms

def PixelClusterCountsAuditor(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelClusterCountsAuditor',
    counts = cms.required.untracked.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

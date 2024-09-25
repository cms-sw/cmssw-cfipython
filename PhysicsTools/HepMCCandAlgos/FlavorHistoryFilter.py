import FWCore.ParameterSet.Config as cms

def FlavorHistoryFilter(*args, **kwargs):
  mod = cms.EDFilter('FlavorHistoryFilter',
    bsrc = cms.required.InputTag,
    csrc = cms.required.InputTag,
    pathToSelect = cms.int32(-1),
    dr = cms.required.double,
    verbose = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

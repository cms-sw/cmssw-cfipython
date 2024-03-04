import FWCore.ParameterSet.Config as cms

def FlavorHistoryFilter(**kwargs):
  mod = cms.EDFilter('FlavorHistoryFilter',
    bsrc = cms.required.InputTag,
    csrc = cms.required.InputTag,
    pathToSelect = cms.int32(-1),
    dr = cms.required.double,
    verbose = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

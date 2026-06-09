import FWCore.ParameterSet.Config as cms

def PtMinCandViewCloneSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinCandViewCloneSelector',
    src = cms.InputTag(''),
    ptMin = cms.double(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def LargestPtTrackSelector(*args, **kwargs):
  mod = cms.EDFilter('LargestPtTrackSelector',
    src = cms.InputTag(''),
    maxNumber = cms.uint32(1),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

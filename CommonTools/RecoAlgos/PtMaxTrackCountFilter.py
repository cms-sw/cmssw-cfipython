import FWCore.ParameterSet.Config as cms

def PtMaxTrackCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PtMaxTrackCountFilter',
    src = cms.InputTag('tracks'),
    minNumber = cms.uint32(1),
    ptMax = cms.double(999),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

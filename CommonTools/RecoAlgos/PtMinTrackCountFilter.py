import FWCore.ParameterSet.Config as cms

def PtMinTrackCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PtMinTrackCountFilter',
    src = cms.InputTag('tracks'),
    minNumber = cms.uint32(1),
    ptMin = cms.double(0),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

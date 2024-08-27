import FWCore.ParameterSet.Config as cms

def PtMinTrackCountFilter(**kwargs):
  mod = cms.EDFilter('PtMinTrackCountFilter',
    src = cms.InputTag('tracks'),
    minNumber = cms.uint32(1),
    ptMin = cms.double(0),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PtMinMuonCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PtMinMuonCountFilter',
    src = cms.InputTag(''),
    ptMin = cms.double(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

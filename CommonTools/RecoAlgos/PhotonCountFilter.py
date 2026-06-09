import FWCore.ParameterSet.Config as cms

def PhotonCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PhotonCountFilter',
    src = cms.InputTag(''),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

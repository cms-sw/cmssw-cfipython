import FWCore.ParameterSet.Config as cms

def PhotonGenFilter(*args, **kwargs):
  mod = cms.EDFilter('PhotonGenFilter',
    MaxEta = cms.untracked.double(2.4),
    MinEta = cms.untracked.double(-2.4),
    MinPt = cms.untracked.double(20),
    drMin = cms.untracked.double(0.1),
    ptThreshold = cms.untracked.double(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

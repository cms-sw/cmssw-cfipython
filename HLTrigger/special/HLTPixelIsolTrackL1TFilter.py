import FWCore.ParameterSet.Config as cms

def HLTPixelIsolTrackL1TFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixelIsolTrackL1TFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltIsolPixelTrackProd'),
    MaxPtNearby = cms.double(2),
    MinEnergyTrack = cms.double(12),
    MinPtTrack = cms.double(3.5),
    MaxEtaTrack = cms.double(1.15),
    MinEtaTrack = cms.double(0),
    filterTrackEnergy = cms.bool(True),
    NMaxTrackCandidates = cms.int32(10),
    DropMultiL2Event = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

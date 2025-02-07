import FWCore.ParameterSet.Config as cms

def PackedCandidateMuonSelectorProducer(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidateMuonSelectorProducer',
    muons = cms.InputTag('muons'),
    candidates = cms.InputTag('packedPFCandidates'),
    lostTracks = cms.InputTag('lostTracks'),
    muonSelectors = cms.vstring(
      'AllTrackerMuons',
      'TMOneStationTight'
    ),
    muonIDs = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

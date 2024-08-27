import FWCore.ParameterSet.Config as cms

def PackedCandidateMuonSelectorProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

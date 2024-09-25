import FWCore.ParameterSet.Config as cms

def HLTTrackMETProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTTrackMETProducer',
    usePt = cms.bool(True),
    useTracks = cms.bool(False),
    usePFRecTracks = cms.bool(False),
    usePFCandidatesCharged = cms.bool(True),
    usePFCandidates = cms.bool(False),
    excludePFMuons = cms.bool(False),
    minNJet = cms.int32(0),
    minPtJet = cms.double(0),
    maxEtaJet = cms.double(999),
    jetsLabel = cms.InputTag('hltAntiKT4PFJets'),
    tracksLabel = cms.InputTag('hltL3Muons'),
    pfRecTracksLabel = cms.InputTag('hltLightPFTracks'),
    pfCandidatesLabel = cms.InputTag('hltParticleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

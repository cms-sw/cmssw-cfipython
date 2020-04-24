import FWCore.ParameterSet.Config as cms

mergedMuonsNoCuts = cms.EDProducer('PATMuonMerger',
  muonCut = cms.string(''),
  otherTracks = cms.InputTag('lostTracks'),
  pfCandidates = cms.InputTag('packedPFCandidates'),
  pfCandidatesCut = cms.string(''),
  muons = cms.InputTag('slimmedMuons'),
  lostTrackCut = cms.string('')
)

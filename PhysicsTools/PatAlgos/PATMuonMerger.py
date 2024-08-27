import FWCore.ParameterSet.Config as cms

def PATMuonMerger(**kwargs):
  mod = cms.EDProducer('PATMuonMerger',
    muonCut = cms.string(''),
    otherTracks = cms.InputTag('lostTracks'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    pfCandidatesCut = cms.string(''),
    muons = cms.InputTag('slimmedMuons'),
    lostTrackCut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PATMuonMerger(*args, **kwargs):
  mod = cms.EDProducer('PATMuonMerger',
    muonCut = cms.string(''),
    otherTracks = cms.InputTag('lostTracks'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    pfCandidatesCut = cms.string(''),
    muons = cms.InputTag('slimmedMuons'),
    lostTrackCut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

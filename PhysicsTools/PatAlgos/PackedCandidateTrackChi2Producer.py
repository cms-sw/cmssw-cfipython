import FWCore.ParameterSet.Config as cms

def PackedCandidateTrackChi2Producer(**kwargs):
  mod = cms.EDProducer('PackedCandidateTrackChi2Producer',
    candidates = cms.InputTag('packedPFCandidates'),
    trackCollection = cms.InputTag('generalTracks'),
    doLostTracks = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

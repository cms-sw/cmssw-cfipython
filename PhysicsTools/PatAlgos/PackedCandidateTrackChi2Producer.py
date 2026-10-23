import FWCore.ParameterSet.Config as cms

def PackedCandidateTrackChi2Producer(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidateTrackChi2Producer',
    candidates = cms.InputTag('packedPFCandidates'),
    trackCollection = cms.InputTag('generalTracks'),
    doLostTracks = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

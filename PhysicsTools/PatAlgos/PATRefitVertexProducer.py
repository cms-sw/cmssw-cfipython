import FWCore.ParameterSet.Config as cms

def PATRefitVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('PATRefitVertexProducer',
    srcVertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    srcCands = cms.InputTag('packedPFCandidates'),
    srcLostTracks = cms.InputTag('lostTracks'),
    srcEleKfTracks = cms.InputTag('lostTracks', 'eleTracks'),
    srcBeamSpot = cms.InputTag('offlineBeamSpot'),
    useBeamSpot = cms.bool(True),
    useLostTracks = cms.bool(True),
    useEleKfTracks = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

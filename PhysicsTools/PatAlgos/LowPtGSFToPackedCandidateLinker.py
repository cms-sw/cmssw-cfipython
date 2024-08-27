import FWCore.ParameterSet.Config as cms

def LowPtGSFToPackedCandidateLinker(**kwargs):
  mod = cms.EDProducer('LowPtGSFToPackedCandidateLinker',
    PFCandidates = cms.InputTag('particleFlow'),
    packedCandidates = cms.InputTag('packedPFCandidates'),
    lostTracks = cms.InputTag('lostTracks'),
    tracks = cms.InputTag('generalTracks'),
    gsfToTrack = cms.InputTag('lowPtGsfToTrackLinks'),
    gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
    electrons = cms.InputTag('selectedPatLowPtElectrons'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

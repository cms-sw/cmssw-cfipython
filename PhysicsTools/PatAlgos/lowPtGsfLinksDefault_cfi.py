import FWCore.ParameterSet.Config as cms

lowPtGsfLinksDefault = cms.EDProducer('LowPtGSFToPackedCandidateLinker',
  PFCandidates = cms.InputTag('particleFlow'),
  packedCandidates = cms.InputTag('packedPFCandidates'),
  lostTracks = cms.InputTag('lostTracks'),
  tracks = cms.InputTag('generalTracks'),
  gsfToTrack = cms.InputTag('lowPtGsfToTrackLinks'),
  gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
  electrons = cms.InputTag('selectedPatLowPtElectrons')
)

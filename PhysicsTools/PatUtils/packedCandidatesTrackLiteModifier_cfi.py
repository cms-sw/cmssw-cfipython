import FWCore.ParameterSet.Config as cms

packedCandidatesTrackLiteModifier = cms.EDProducer('PackedCandidatesTrackLiteModifier',
  inputCandidates = cms.InputTag('packedPFCandidates'),
  covSchema = cms.uint32(1025),
  covVersion = cms.uint32(1),
  nHits = cms.uint32(8),
  nPixelHits = cms.uint32(3),
  mightGet = cms.optional.untracked.vstring
)

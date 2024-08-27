import FWCore.ParameterSet.Config as cms

def PackedCandidatesTrackLiteModifier(**kwargs):
  mod = cms.EDProducer('PackedCandidatesTrackLiteModifier',
    inputCandidates = cms.InputTag('packedPFCandidates'),
    covSchema = cms.uint32(1025),
    covVersion = cms.uint32(1),
    nHits = cms.uint32(8),
    nPixelHits = cms.uint32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

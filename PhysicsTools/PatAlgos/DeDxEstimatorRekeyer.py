import FWCore.ParameterSet.Config as cms

def DeDxEstimatorRekeyer(**kwargs):
  mod = cms.EDProducer('DeDxEstimatorRekeyer',
    tracks = cms.InputTag('generalTracks'),
    dedxHits = cms.InputTag('dedxHitInfo'),
    packedCandidates = cms.VInputTag(
      'packedPFCandidates',
      'lostTracks',
      'lostTracks:eleTracks'
    ),
    dedxEstimators = cms.VInputTag(
      'dedxHarmonic2',
      'dedxPixelHarmonic2'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

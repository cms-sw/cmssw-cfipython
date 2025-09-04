import FWCore.ParameterSet.Config as cms

def DeDxEstimatorRekeyer(*args, **kwargs):
  mod = cms.EDProducer('DeDxEstimatorRekeyer',
    tracks = cms.InputTag('generalTracks'),
    dedxHits = cms.InputTag('dedxHitInfo'),
    dedxMomentum = cms.InputTag('dedxHitInfo', 'momentumAtHit'),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

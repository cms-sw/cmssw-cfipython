import FWCore.ParameterSet.Config as cms

L1TEGammaFilteredCollectionProducer = cms.EDProducer('L1TEGammaFilteredCollectionProducer',
  inputTag = cms.InputTag('L1EGammaClusterEmuProducer'),
  quality = cms.int32(2),
  qualIsMask = cms.bool(True),
  applyQual = cms.bool(True),
  minBX = cms.int32(-1),
  maxBX = cms.int32(1),
  minPt = cms.double(5),
  scalings = cms.vdouble(
    2.6604,
    1.06077,
    0
  ),
  mightGet = cms.optional.untracked.vstring
)

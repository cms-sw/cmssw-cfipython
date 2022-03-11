import FWCore.ParameterSet.Config as cms

pixelVerticesCUDA = cms.EDProducer('PixelVertexProducerCUDA',
  onGPU = cms.bool(True),
  oneKernel = cms.bool(True),
  useDensity = cms.bool(True),
  useDBSCAN = cms.bool(False),
  useIterative = cms.bool(False),
  minT = cms.int32(2),
  eps = cms.double(0.07),
  errmax = cms.double(0.01),
  chi2max = cms.double(9),
  PtMin = cms.double(0.5),
  pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)

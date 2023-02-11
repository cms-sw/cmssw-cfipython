import FWCore.ParameterSet.Config as cms

pixelVertexProducerCUDAPhase1 = cms.EDProducer('PixelVertexProducerCUDAPhase1',
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
  PtMax = cms.double(75),
  pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)

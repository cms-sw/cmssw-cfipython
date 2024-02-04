import FWCore.ParameterSet.Config as cms

pixelVertexProducerAlpakaPhase1 = cms.EDProducer('PixelVertexProducerAlpakaPhase1@alpaka',
  oneKernel = cms.bool(True),
  useDensity = cms.bool(True),
  useDBSCAN = cms.bool(False),
  useIterative = cms.bool(False),
  doSplitting = cms.bool(True),
  minT = cms.int32(2),
  eps = cms.double(0.07),
  errmax = cms.double(0.01),
  chi2max = cms.double(9),
  PtMin = cms.double(0.5),
  PtMax = cms.double(75),
  pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
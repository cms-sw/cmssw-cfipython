import FWCore.ParameterSet.Config as cms

ctppsLocalTrackLiteDefaultProducer = cms.EDProducer('CTPPSLocalTrackLiteProducer',
  includeStrips = cms.bool(False),
  tagSiStripTrack = cms.InputTag('totemRPLocalTrackFitter'),
  includeDiamonds = cms.bool(False),
  tagDiamondTrack = cms.InputTag('ctppsDiamondLocalTracks'),
  includePixels = cms.bool(False),
  tagPixelTrack = cms.InputTag('ctppsPixelLocalTracks'),
  doNothing = cms.bool(False),
  pixelTrackTxMin = cms.double(-10),
  pixelTrackTxMax = cms.double(10),
  pixelTrackTyMin = cms.double(-10),
  pixelTrackTyMax = cms.double(10)
)

import FWCore.ParameterSet.Config as cms

ctppsLocalTrackLiteDefaultProducer = cms.EDProducer('CTPPSLocalTrackLiteProducer',
  includeStrips = cms.bool(True),
  tagSiStripTrack = cms.InputTag('totemRPLocalTrackFitter'),
  includeDiamonds = cms.bool(True),
  tagDiamondTrack = cms.InputTag('ctppsDiamondLocalTracks'),
  includePixels = cms.bool(True),
  tagPixelTrack = cms.InputTag('ctppsPixelLocalTracks'),
  doNothing = cms.bool(True),
  pixelTrackTxMin = cms.double(-10),
  pixelTrackTxMax = cms.double(10),
  pixelTrackTyMin = cms.double(-10),
  pixelTrackTyMax = cms.double(10)
)

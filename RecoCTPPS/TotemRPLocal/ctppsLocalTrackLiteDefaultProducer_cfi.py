import FWCore.ParameterSet.Config as cms

ctppsLocalTrackLiteDefaultProducer = cms.EDProducer('CTPPSLocalTrackLiteProducer',
  includeStrips = cms.bool(True),
  tagSiStripTrack = cms.InputTag('totemRPLocalTrackFitter'),
  includeDiamonds = cms.bool(True),
  tagDiamondTrack = cms.InputTag('ctppsDiamondLocalTracks'),
  includePixels = cms.bool(True),
  tagPixelTrack = cms.InputTag('ctppsPixelLocalTracks'),
  doNothing = cms.bool(True),
  pixelTrackTxRange = cms.vdouble(
    -0.03,
    0.03
  ),
  pixelTrackTyRange = cms.vdouble(
    -0.04,
    0.04
  )
)

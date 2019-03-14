import FWCore.ParameterSet.Config as cms

ctppsLocalTrackLiteDefaultProducer = cms.EDProducer('CTPPSLocalTrackLiteProducer',
  tagSiStripTrack = cms.InputTag('totemRPLocalTrackFitter'),
  tagDiamondTrack = cms.InputTag('ctppsDiamondLocalTracks'),
  tagPixelTrack = cms.InputTag('ctppsPixelLocalTracks'),
  doNothing = cms.bool(True)
)

import FWCore.ParameterSet.Config as cms

ctppsLocalTrackLiteDefaultProducer = cms.EDProducer('CTPPSLocalTrackLiteProducer',
  tagSiStripTrack = cms.InputTag('totemRPLocalTrackFitter'),
  tagDiamondTrack = cms.InputTag('ctppsDiamondLocalTracks'),
  doNothing = cms.bool(True)
)

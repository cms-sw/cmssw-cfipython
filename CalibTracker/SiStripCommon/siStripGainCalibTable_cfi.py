import FWCore.ParameterSet.Config as cms

siStripGainCalibTable = cms.EDProducer('SiStripGainCalibTableProducer',
  name = cms.string('cluster'),
  doc = cms.string(''),
  extension = cms.bool(False),
  Tracks = cms.InputTag('generalTracks'),
  mightGet = cms.optional.untracked.vstring
)

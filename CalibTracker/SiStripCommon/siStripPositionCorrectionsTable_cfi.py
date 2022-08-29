import FWCore.ParameterSet.Config as cms

siStripPositionCorrectionsTable = cms.EDProducer('SiStripPositionCorrectionsTableProducer',
  name = cms.string('cluster'),
  doc = cms.string('On-track cluster properties for Lorentz angle and backplane correction measurement'),
  extension = cms.bool(False),
  Tracks = cms.InputTag('generalTracks'),
  mightGet = cms.optional.untracked.vstring
)

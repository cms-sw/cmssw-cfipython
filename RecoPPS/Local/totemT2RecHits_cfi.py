import FWCore.ParameterSet.Config as cms

totemT2RecHits = cms.EDProducer('TotemT2RecHitProducer',
  digiTag = cms.InputTag('totemT2Digis', 'TotemT2'),
  timingCalibrationTag = cms.string('GlobalTag:TotemT2TimingCalibration'),
  timeSliceNs = cms.double(0.0244140625),
  applyCalibration = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

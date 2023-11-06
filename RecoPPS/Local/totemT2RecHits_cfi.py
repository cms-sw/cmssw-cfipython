import FWCore.ParameterSet.Config as cms

totemT2RecHits = cms.EDProducer('TotemT2RecHitProducer',
  digiTag = cms.InputTag('totemT2Digis', 'TotemT2'),
  timeSliceNs = cms.double(6.25),
  applyCalibration = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

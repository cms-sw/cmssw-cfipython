import FWCore.ParameterSet.Config as cms

def TotemT2RecHitProducer(**kwargs):
  mod = cms.EDProducer('TotemT2RecHitProducer',
    digiTag = cms.InputTag('totemT2Digis', 'TotemT2'),
    timeSliceNs = cms.double(6.25),
    applyCalibration = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

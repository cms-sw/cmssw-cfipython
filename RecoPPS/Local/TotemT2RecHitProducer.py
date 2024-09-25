import FWCore.ParameterSet.Config as cms

def TotemT2RecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('TotemT2RecHitProducer',
    digiTag = cms.InputTag('totemT2Digis', 'TotemT2'),
    timeSliceNs = cms.double(6.25),
    applyCalibration = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

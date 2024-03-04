import FWCore.ParameterSet.Config as cms

def TkTransientTrackingRecHitBuilderESProducer(**kwargs):
  mod = cms.ESProducer('TkTransientTrackingRecHitBuilderESProducer',
    ComponentName = cms.string('Fake'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    StripCPE = cms.string('Fake'),
    PixelCPE = cms.string('Fake'),
    Matcher = cms.string('Fake'),
    Phase2StripCPE = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

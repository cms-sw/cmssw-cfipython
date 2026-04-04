import FWCore.ParameterSet.Config as cms

def TkTransientTrackingRecHitBuilderESProducer(*args, **kwargs):
  mod = cms.ESProducer('TkTransientTrackingRecHitBuilderESProducer',
    ComponentName = cms.string('Fake'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    StripCPE = cms.string('Fake'),
    PixelCPE = cms.string('Fake'),
    Matcher = cms.string('Fake'),
    Phase2StripCPE = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TrackingParticleConversionRefSelector(*args, **kwargs):
  mod = cms.EDProducer('TrackingParticleConversionRefSelector',
    src = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

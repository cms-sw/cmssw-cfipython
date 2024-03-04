import FWCore.ParameterSet.Config as cms

def TrackingParticleConversionRefSelector(**kwargs):
  mod = cms.EDProducer('TrackingParticleConversionRefSelector',
    src = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

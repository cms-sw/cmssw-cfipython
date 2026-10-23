import FWCore.ParameterSet.Config as cms

def TrackingParticleSelectorByGen(*args, **kwargs):
  mod = cms.EDProducer('TrackingParticleSelectorByGen',
    trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
    genParticles = cms.InputTag('genParticles'),
    select = cms.required.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

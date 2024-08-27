import FWCore.ParameterSet.Config as cms

def TrackingParticleSelectorByGen(**kwargs):
  mod = cms.EDProducer('TrackingParticleSelectorByGen',
    trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
    genParticles = cms.InputTag('genParticles'),
    select = cms.required.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

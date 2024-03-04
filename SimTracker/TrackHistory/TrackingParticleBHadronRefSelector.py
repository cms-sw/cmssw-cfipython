import FWCore.ParameterSet.Config as cms

def TrackingParticleBHadronRefSelector(**kwargs):
  mod = cms.EDProducer('TrackingParticleBHadronRefSelector',
    src = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

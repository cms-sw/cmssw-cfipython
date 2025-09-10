import FWCore.ParameterSet.Config as cms

def PhotonSeedGainProducer(*args, **kwargs):
  mod = cms.EDProducer('PhotonSeedGainProducer',
    src = cms.required.InputTag,
    recHitsEB = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
    recHitsEE = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

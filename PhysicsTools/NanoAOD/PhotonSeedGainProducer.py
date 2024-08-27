import FWCore.ParameterSet.Config as cms

def PhotonSeedGainProducer(**kwargs):
  mod = cms.EDProducer('PhotonSeedGainProducer',
    src = cms.required.InputTag,
    recHitsEB = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
    recHitsEE = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

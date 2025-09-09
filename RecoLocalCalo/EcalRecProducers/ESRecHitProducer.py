import FWCore.ParameterSet.Config as cms

def ESRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('ESRecHitProducer',
    ESrechitCollection = cms.string('EcalRecHitsES'),
    ESdigiCollection = cms.InputTag('ecalPreshowerDigis'),
    algo = cms.string('ESRecHitWorker'),
    ESRecoAlgo = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

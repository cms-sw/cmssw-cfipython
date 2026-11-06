import FWCore.ParameterSet.Config as cms

def EtlLocalRecoSoAValidation(*args, **kwargs):
  mod = cms.EDProducer('EtlLocalRecoSoAValidation',
    folder = cms.string('MTD/ETL/LocalRecoSoA'),
    recHitsSoATag = cms.InputTag('etlRecHitsSoA'),
    baseRecHitsSoATag = cms.InputTag('etlBaseRecHitsSoA'),
    simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsEndcap'),
    trkHitTag = cms.InputTag('mtdTrackingRecHits'),
    hitMinimumEnergy2Dis = cms.double(0.001),
    optionalPlots = cms.bool(False),
    BaseRecHitsPlots = cms.bool(False),
    HitMinimumAmplitude = cms.double(0.33),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

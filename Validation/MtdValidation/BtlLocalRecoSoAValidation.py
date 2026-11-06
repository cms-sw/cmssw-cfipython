import FWCore.ParameterSet.Config as cms

def BtlLocalRecoSoAValidation(*args, **kwargs):
  mod = cms.EDProducer('BtlLocalRecoSoAValidation',
    folder = cms.string('MTD/BTL/LocalRecoSoA'),
    recHitsSoATag = cms.InputTag('btlRecHitsSoA'),
    baseRecHitsSoATag = cms.InputTag('btlBaseRecHitsSoA'),
    simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
    HitMinimumEnergy = cms.double(0.001),
    optionalPlots = cms.bool(False),
    BaseRecHitsPlots = cms.bool(False),
    HitMinimumAmplitude = cms.double(2285),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

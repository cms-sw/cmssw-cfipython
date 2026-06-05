import FWCore.ParameterSet.Config as cms

def EcalMIPRecHitFilter(*args, **kwargs):
  mod = cms.EDFilter('EcalMIPRecHitFilter',
    EcalRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    AmpMinSeed = cms.untracked.double(0.045),
    AmpMin2 = cms.untracked.double(0.045),
    SingleAmpMin = cms.untracked.double(0.108),
    maskedChannels = cms.untracked.vint32(),
    side = cms.untracked.int32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

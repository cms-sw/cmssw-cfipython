import FWCore.ParameterSet.Config as cms

def EcalMIPRecHitFilter(**kwargs):
  mod = cms.EDFilter('EcalMIPRecHitFilter',
    EcalRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    AmpMinSeed = cms.untracked.double(0.045),
    AmpMin2 = cms.untracked.double(0.045),
    SingleAmpMin = cms.untracked.double(0.108),
    maskedChannels = cms.untracked.vint32(),
    side = cms.untracked.int32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

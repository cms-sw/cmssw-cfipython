import FWCore.ParameterSet.Config as cms

def EcalSimpleUncalibRecHitFilter(*args, **kwargs):
  mod = cms.EDFilter('EcalSimpleUncalibRecHitFilter',
    EcalUncalibRecHitCollection = cms.InputTag('ecalWeightUncalibRecHit', 'EcalUncalibRecHitsEB'),
    adcCut = cms.untracked.double(12),
    maskedChannels = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

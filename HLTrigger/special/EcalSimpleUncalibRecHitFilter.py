import FWCore.ParameterSet.Config as cms

def EcalSimpleUncalibRecHitFilter(**kwargs):
  mod = cms.EDFilter('EcalSimpleUncalibRecHitFilter',
    EcalUncalibRecHitCollection = cms.InputTag('ecalWeightUncalibRecHit', 'EcalUncalibRecHitsEB'),
    adcCut = cms.untracked.double(12),
    maskedChannels = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalRecHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitsValidation',
    verbose = cms.untracked.bool(False),
    moduleLabelMC = cms.string('generatorSmeared'),
    hitsProducer = cms.string('g4SimHits'),
    EBrechitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EBuncalibrechitCollection = cms.InputTag('ecalMultiFitUncalibRecHit', 'EcalUncalibRecHitsEB'),
    enableEndcaps = cms.untracked.bool(True),
    EErechitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    ESrechitCollection = cms.InputTag('ecalPreshowerRecHit', 'EcalRecHitsES'),
    EEuncalibrechitCollection = cms.InputTag('ecalMultiFitUncalibRecHit', 'EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

hcalDumpHits = cms.EDAnalyzer('HcalDumpHits',
  simHitSource = cms.InputTag('g4SimHits', 'HcalHits'),
  hbheDigiSource = cms.InputTag('hcalDigis'),
  hfDigiSource = cms.InputTag('hcalDigis'),
  hoDigiSource = cms.InputTag('hcalDigis'),
  hbheRecHitSource = cms.InputTag('hbhereco'),
  hfRecHitSource = cms.InputTag('hfreco'),
  hoRecHitSource = cms.InputTag('horeco')
)

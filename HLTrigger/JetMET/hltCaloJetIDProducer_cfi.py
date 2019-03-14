import FWCore.ParameterSet.Config as cms

hltCaloJetIDProducer = cms.EDProducer('HLTCaloJetIDProducer',
  min_N90 = cms.int32(-2),
  min_N90hits = cms.int32(2),
  min_EMF = cms.double(1e-06),
  max_EMF = cms.double(999),
  jetsInput = cms.InputTag('hltAntiKT4CaloJets'),
  JetIDParams = cms.PSet(
    useRecHits = cms.bool(True),
    hbheRecHitsColl = cms.InputTag('hltHbhereco'),
    hoRecHitsColl = cms.InputTag('hltHoreco'),
    hfRecHitsColl = cms.InputTag('hltHfreco'),
    ebRecHitsColl = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
    eeRecHitsColl = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE')
  )
)

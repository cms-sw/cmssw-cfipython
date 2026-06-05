import FWCore.ParameterSet.Config as cms

def HLTCaloJetIDProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTCaloJetIDProducer',
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
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

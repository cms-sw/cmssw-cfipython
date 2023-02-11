import FWCore.ParameterSet.Config as cms

hltJetTimingProducerRecoPFJet = cms.EDProducer('HLTPFJetTimingProducer',
  jets = cms.InputTag(''),
  barrelJets = cms.bool(False),
  endcapJets = cms.bool(False),
  ecalCellEnergyThresh = cms.double(0.5),
  ecalCellTimeThresh = cms.double(12.5),
  ecalCellTimeErrorThresh = cms.double(100),
  matchingRadius = cms.double(0.4),
  ebRecHitsColl = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
  eeRecHitsColl = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE'),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

hltRecHitInAllL1RegionsProducerEcalUncalibratedRecHit = cms.EDProducer('HLTEcalUncalibratedRecHitInAllL1RegionsProducer',
  productLabels = cms.vstring(
    'EcalRegionalRecHitsEB',
    'EcalRegionalRecHitsEE'
  ),
  recHitLabels = cms.VInputTag(
    'hltEcalRegionalEgammaRecHit:EcalRecHitsEB',
    'hltEcalRegionalEgammaRecHit:EcalRecHitsEE',
    'hltESRegionalEgammaRecHit:EcalRecHitsES'
  ),
  l1InputRegions = cms.VPSet(
    cms.PSet(
      inputColl = cms.InputTag('hltL1extraParticles', 'NonIsolated'),
      maxEt = cms.double(999),
      minEt = cms.double(5),
      regionEtaMargin = cms.double(0.14),
      regionPhiMargin = cms.double(0.4),
      type = cms.string('L1EmParticle')
    ),
    cms.PSet(
      inputColl = cms.InputTag('hltL1extraParticles', 'Isolated'),
      maxEt = cms.double(999),
      minEt = cms.double(5),
      regionEtaMargin = cms.double(0.14),
      regionPhiMargin = cms.double(0.4),
      type = cms.string('L1EmParticle')
    ),
    cms.PSet(
      inputColl = cms.InputTag('hltCaloStage2Digis'),
      maxEt = cms.double(999),
      minEt = cms.double(5),
      regionEtaMargin = cms.double(0.4),
      regionPhiMargin = cms.double(0.5),
      type = cms.string('EGamma')
    ),
    cms.PSet(
      inputColl = cms.InputTag('hltCaloStage2Digis'),
      maxEt = cms.double(999),
      minEt = cms.double(200),
      regionEtaMargin = cms.double(0.4),
      regionPhiMargin = cms.double(0.5),
      type = cms.string('EGamma')
    )
  ),
  mightGet = cms.optional.untracked.vstring
)

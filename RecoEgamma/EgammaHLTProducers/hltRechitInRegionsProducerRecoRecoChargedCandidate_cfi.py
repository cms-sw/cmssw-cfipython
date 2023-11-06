import FWCore.ParameterSet.Config as cms

hltRechitInRegionsProducerRecoRecoChargedCandidate = cms.EDProducer('MuonHLTRechitInRegionsProducer',
  productLabels = cms.vstring(
    'EcalRegionalRecHitsEB',
    'EcalRegionalRecHitsEE'
  ),
  ecalhitLabels = cms.VInputTag(
    'hltEcalRegionalEgammaRecHit:EcalRecHitsEB',
    'hltEcalRegionalEgammaRecHit:EcalRecHitsEE',
    'hltESRegionalEgammaRecHit:EcalRecHitsES'
  ),
  l1TagIsolated = cms.InputTag('l1extraParticles', 'Isolated'),
  l1TagNonIsolated = cms.InputTag('l1extraParticles', 'NonIsolated'),
  useUncalib = cms.bool(True),
  doIsolated = cms.bool(True),
  l1LowerThr = cms.double(5),
  l1UpperThr = cms.double(999),
  l1LowerThrIgnoreIsolation = cms.double(0),
  regionEtaMargin = cms.double(0.14),
  regionPhiMargin = cms.double(0.4),
  mightGet = cms.optional.untracked.vstring
)

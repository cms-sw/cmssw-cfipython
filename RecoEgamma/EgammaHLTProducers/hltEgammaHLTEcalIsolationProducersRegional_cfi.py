import FWCore.ParameterSet.Config as cms

hltEgammaHLTEcalIsolationProducersRegional = cms.EDProducer('EgammaHLTEcalIsolationProducersRegional',
  bcBarrelProducer = cms.InputTag(''),
  bcEndcapProducer = cms.InputTag(''),
  scIslandBarrelProducer = cms.InputTag(''),
  scIslandEndcapProducer = cms.InputTag(''),
  recoEcalCandidateProducer = cms.InputTag(''),
  egEcalIsoEtMin = cms.double(0),
  egEcalIsoConeSize = cms.double(0.3),
  SCAlgoType = cms.int32(1)
)

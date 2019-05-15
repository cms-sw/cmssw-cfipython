import FWCore.ParameterSet.Config as cms

interestingGedEgammaIsoHCALDetId = cms.EDProducer('EgammaIsoHcalDetIdCollectionProducer',
  recHitsLabel = cms.InputTag('hbhereco'),
  elesLabel = cms.InputTag('gedGsfElectrons'),
  phosLabel = cms.InputTag('gedPhotons'),
  superClustersLabel = cms.InputTag('particleFlowEGamma'),
  minSCEt = cms.double(20),
  minEleEt = cms.double(20),
  minPhoEt = cms.double(20),
  interestingDetIdCollection = cms.string(''),
  hitSelection = cms.PSet(
    maxDIEta = cms.int32(5),
    maxDIPhi = cms.int32(5),
    minEnergyHB = cms.double(0.8),
    minEnergyHEDepth1 = cms.double(0.1),
    minEnergyHEDefault = cms.double(0.2)
  )
)

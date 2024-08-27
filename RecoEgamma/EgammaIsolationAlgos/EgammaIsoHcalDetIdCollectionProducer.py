import FWCore.ParameterSet.Config as cms

def EgammaIsoHcalDetIdCollectionProducer(**kwargs):
  mod = cms.EDProducer('EgammaIsoHcalDetIdCollectionProducer',
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
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

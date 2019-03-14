import FWCore.ParameterSet.Config as cms

egammaHcalPFClusterIsolationProducerRecoGsfElectron = cms.EDProducer('ElectronHcalPFClusterIsolationProducer',
  candidateProducer = cms.InputTag('gedGsfElectrons'),
  pfClusterProducerHCAL = cms.InputTag('particleFlowClusterHCAL'),
  useHF = cms.bool(False),
  pfClusterProducerHFEM = cms.InputTag(''),
  pfClusterProducerHFHAD = cms.InputTag(''),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0),
  etaStripBarrel = cms.double(0),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  useEt = cms.bool(True)
)

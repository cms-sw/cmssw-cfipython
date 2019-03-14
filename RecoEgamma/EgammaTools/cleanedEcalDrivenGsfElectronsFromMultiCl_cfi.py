import FWCore.ParameterSet.Config as cms

cleanedEcalDrivenGsfElectronsFromMultiCl = cms.EDProducer('HGCalElectronFilter',
  inputGsfElectrons = cms.InputTag('ecalDrivenGsfElectronsFromMultiCl'),
  cleanBarrel = cms.bool(False),
  outputCollection = cms.string('')
)

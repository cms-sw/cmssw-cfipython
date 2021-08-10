import FWCore.ParameterSet.Config as cms

cleanedEcalDrivenGsfElectronsHGC = cms.EDProducer('HGCalElectronFilter',
  inputGsfElectrons = cms.InputTag('ecalDrivenGsfElectronsHGC'),
  cleanBarrel = cms.bool(False),
  outputCollection = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

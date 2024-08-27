import FWCore.ParameterSet.Config as cms

def HGCalElectronFilter(**kwargs):
  mod = cms.EDProducer('HGCalElectronFilter',
    inputGsfElectrons = cms.InputTag('ecalDrivenGsfElectronsHGC'),
    cleanBarrel = cms.bool(False),
    outputCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

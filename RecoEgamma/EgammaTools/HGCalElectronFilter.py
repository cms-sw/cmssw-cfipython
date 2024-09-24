import FWCore.ParameterSet.Config as cms

def HGCalElectronFilter(*args, **kwargs):
  mod = cms.EDProducer('HGCalElectronFilter',
    inputGsfElectrons = cms.InputTag('ecalDrivenGsfElectronsHGC'),
    cleanBarrel = cms.bool(False),
    outputCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

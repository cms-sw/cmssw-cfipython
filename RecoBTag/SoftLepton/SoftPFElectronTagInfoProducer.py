import FWCore.ParameterSet.Config as cms

def SoftPFElectronTagInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('SoftPFElectronTagInfoProducer',
    primaryVertex = cms.required.InputTag,
    jets = cms.required.InputTag,
    electrons = cms.required.InputTag,
    DeltaRElectronJet = cms.required.double,
    MaxSip3Dsig = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

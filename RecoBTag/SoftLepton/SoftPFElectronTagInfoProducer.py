import FWCore.ParameterSet.Config as cms

def SoftPFElectronTagInfoProducer(**kwargs):
  mod = cms.EDProducer('SoftPFElectronTagInfoProducer',
    primaryVertex = cms.required.InputTag,
    jets = cms.required.InputTag,
    electrons = cms.required.InputTag,
    DeltaRElectronJet = cms.required.double,
    MaxSip3Dsig = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

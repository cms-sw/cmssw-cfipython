import FWCore.ParameterSet.Config as cms

def ElectronJetVarProducer(**kwargs):
  mod = cms.EDProducer('ElectronJetVarProducer',
    srcJet = cms.required.InputTag,
    srcLep = cms.required.InputTag,
    srcVtx = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

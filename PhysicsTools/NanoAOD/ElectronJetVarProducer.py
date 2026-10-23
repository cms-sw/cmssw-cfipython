import FWCore.ParameterSet.Config as cms

def ElectronJetVarProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronJetVarProducer',
    srcJet = cms.required.InputTag,
    srcLep = cms.required.InputTag,
    srcVtx = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

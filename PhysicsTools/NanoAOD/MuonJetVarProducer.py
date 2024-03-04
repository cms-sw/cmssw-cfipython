import FWCore.ParameterSet.Config as cms

def MuonJetVarProducer(**kwargs):
  mod = cms.EDProducer('MuonJetVarProducer',
    srcJet = cms.required.InputTag,
    srcLep = cms.required.InputTag,
    srcVtx = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

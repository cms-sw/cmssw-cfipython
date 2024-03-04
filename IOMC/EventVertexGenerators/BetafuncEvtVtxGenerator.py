import FWCore.ParameterSet.Config as cms

def BetafuncEvtVtxGenerator(**kwargs):
  mod = cms.EDProducer('BetafuncEvtVtxGenerator',
    X0 = cms.double(0),
    Y0 = cms.double(0),
    Z0 = cms.double(0),
    SigmaZ = cms.double(0),
    BetaStar = cms.double(0),
    Emittance = cms.double(0),
    Alpha = cms.double(0),
    Phi = cms.double(0),
    TimeOffset = cms.double(0),
    src = cms.required.InputTag,
    readDB = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

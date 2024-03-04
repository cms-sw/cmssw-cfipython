import FWCore.ParameterSet.Config as cms

def HFFilter(**kwargs):
  mod = cms.EDFilter('HFFilter',
    genJetsCollName = cms.required.InputTag,
    ptMin = cms.required.double,
    etaMax = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

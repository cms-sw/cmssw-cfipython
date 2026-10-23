import FWCore.ParameterSet.Config as cms

def HFFilter(*args, **kwargs):
  mod = cms.EDFilter('HFFilter',
    genJetsCollName = cms.required.InputTag,
    ptMin = cms.required.double,
    etaMax = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

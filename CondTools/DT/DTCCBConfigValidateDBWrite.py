import FWCore.ParameterSet.Config as cms

def DTCCBConfigValidateDBWrite(**kwargs):
  mod = cms.EDAnalyzer('DTCCBConfigValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

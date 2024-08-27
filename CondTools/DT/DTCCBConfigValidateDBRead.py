import FWCore.ParameterSet.Config as cms

def DTCCBConfigValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTCCBConfigValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

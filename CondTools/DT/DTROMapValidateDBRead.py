import FWCore.ParameterSet.Config as cms

def DTROMapValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTROMapValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

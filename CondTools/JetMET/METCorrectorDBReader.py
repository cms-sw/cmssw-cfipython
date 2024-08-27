import FWCore.ParameterSet.Config as cms

def METCorrectorDBReader(**kwargs):
  mod = cms.EDAnalyzer('METCorrectorDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

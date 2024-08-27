import FWCore.ParameterSet.Config as cms

def METCorrectorDBWriter(**kwargs):
  mod = cms.EDAnalyzer('METCorrectorDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

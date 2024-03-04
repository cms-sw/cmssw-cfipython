import FWCore.ParameterSet.Config as cms

def JetCorrectorDBWriter(**kwargs):
  mod = cms.EDAnalyzer('JetCorrectorDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

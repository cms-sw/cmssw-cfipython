import FWCore.ParameterSet.Config as cms

def writeBlob(**kwargs):
  mod = cms.EDAnalyzer('writeBlob',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

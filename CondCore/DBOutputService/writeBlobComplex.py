import FWCore.ParameterSet.Config as cms

def writeBlobComplex(**kwargs):
  mod = cms.EDAnalyzer('writeBlobComplex',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

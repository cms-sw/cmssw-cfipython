import FWCore.ParameterSet.Config as cms

def PFIsoReaderDemo(**kwargs):
  mod = cms.EDAnalyzer('PFIsoReaderDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
